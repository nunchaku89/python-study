# Book Management API

FastAPI를 이용하여 도서를 등록하고 조회하는 REST API 프로젝트입니다.

이 프로젝트는 FastAPI 기본 과정에서 학습한 내용을 실제 프로젝트 구조에 적용하기 위해 진행합니다.

---

## Phase 1 학습 목표

- FastAPI 프로젝트 구조를 분리한다.
- `APIRouter`를 이용하여 도서 API를 별도 파일로 관리한다.
- Pydantic 모델을 별도 파일로 분리한다.
- 도서 등록 및 전체 조회 API를 구현한다.
- 중복된 도서 ID가 등록되지 않도록 검증한다.

---

## 프로젝트 구조

```text
book-management-api/
├── main.py
├── models.py
└── routers/
    ├── __init__.py
    └── books.py
```

### 파일별 역할

| 파일 | 역할 |
|---|---|
| `main.py` | FastAPI 애플리케이션 생성 및 Router 등록 |
| `models.py` | 도서 데이터 모델 정의 |
| `routers/books.py` | 도서 관련 API와 처리 로직 |
| `routers/__init__.py` | `routers` 디렉터리를 Python 패키지로 구성 |

---

## Book 모델

```python
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
```

---

## APIRouter

도서 관련 API를 하나의 Router로 묶었다.

```python
router = APIRouter(
    prefix="/books",
    tags=["books"]
)
```

### `prefix`

`prefix="/books"`를 설정하면 Router 내부의 모든 경로 앞에 `/books`가 자동으로 붙는다.

```python
@router.get("")
```

실제 경로:

```http
GET /books
```

### `tags`

Swagger 문서에서 도서 API를 `books` 그룹으로 표시한다.

---

## Router 등록

`main.py`에서 도서 Router를 FastAPI 애플리케이션에 등록한다.

```python
app.include_router(books.router)
```

Router를 구현하더라도 `include_router()`로 등록하지 않으면 해당 API를 사용할 수 없다.

---

## 구현한 API

### 도서 등록

```http
POST /books
```

Request Body:

```json
{
  "id": 1,
  "title": "Python Study",
  "author": "Wayne"
}
```

Response:

```json
{
  "message": "Book Created",
  "book": {
    "id": 1,
    "title": "Python Study",
    "author": "Wayne"
  }
}
```

---

### 전체 도서 조회

```http
GET /books
```

Response:

```json
[
  {
    "id": 1,
    "title": "Python Study",
    "author": "Wayne"
  },
  {
    "id": 2,
    "title": "FastAPI Study",
    "author": "Wayne"
  }
]
```

---

## 중복 ID 검증

이미 등록된 ID가 다시 요청되면 새로운 도서를 추가하지 않는다.

```python
@router.post("")
def create_book(book: Book):

    for item in books:
        if item.id == book.id:
            return {
                "message": "Book Id Already Exists"
            }

    books.append(book)

    return {
        "message": "Book Created",
        "book": book
    }
```

중복 ID 요청 결과:

```json
{
  "message": "Book Id Already Exists"
}
```

---

## 데이터 저장 방식

Phase 1에서는 Python List를 메모리 저장소로 사용한다.

```python
books: list[Book] = []
```

서버가 종료되거나 다시 시작되면 저장된 데이터는 초기화된다.

---

## 새롭게 배운 내용

- `APIRouter`를 사용하여 API를 기능별로 분리할 수 있다.
- `prefix`를 이용하면 반복되는 URL 경로를 줄일 수 있다.
- `tags`를 사용하여 Swagger 문서를 기능별로 정리할 수 있다.
- `include_router()`를 이용하여 분리한 Router를 애플리케이션에 연결한다.
- Pydantic 모델을 별도 파일에서 관리할 수 있다.
- 중복 ID 검증과 같은 비즈니스 규칙을 구현할 수 있다.
- 프로젝트 구조를 분리하면 기능 확장과 유지보수가 쉬워진다.

---

## Phase 1 완료 기능

- [x] 프로젝트 폴더 구조 생성
- [x] Pydantic `Book` 모델 작성
- [x] `APIRouter` 생성
- [x] Router와 FastAPI 애플리케이션 연결
- [x] `POST /books` 구현
- [x] `GET /books` 구현
- [x] 도서 2권 등록 테스트
- [x] 전체 조회 테스트
- [x] 중복 ID 검증 구현

---

## 다음 단계

Phase 2에서는 다음 내용을 구현한다.

- 도서 단건 조회
- 도서 수정
- 도서 삭제
- `HTTPException`
- 올바른 HTTP 상태 코드


# Book Management API

FastAPI를 이용하여 도서를 등록하고 조회·수정·삭제하는 REST API 프로젝트입니다.

FastAPI 기본 과정에서 학습한 내용을 실제 프로젝트 구조에 적용하고, 단계적으로 실무에 가까운 구조로 개선하는 것을 목표로 합니다.

---

## 기술 스택

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## 프로젝트 구조

```text
book-management-api/
├── main.py
├── models.py
└── routers/
    ├── __init__.py
    └── books.py
```

### 파일별 역할

| 파일 | 역할 |
|---|---|
| `main.py` | FastAPI 애플리케이션 생성 및 Router 등록 |
| `models.py` | 도서 데이터 모델 정의 |
| `routers/books.py` | 도서 관련 API 및 처리 로직 |
| `routers/__init__.py` | `routers` 디렉터리를 Python 패키지로 구성 |

---

## 실행 방법

프로젝트 폴더로 이동한다.

```powershell
cd fastapi\mini-project\book-management-api
```

서버를 실행한다.

```powershell
uvicorn main:app --reload
```

Swagger 문서:

```text
http://127.0.0.1:8000/docs
```

---

## 데이터 모델

```python
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
```

---

## 데이터 저장 방식

현재는 Python List를 메모리 저장소로 사용한다.

```python
books: list[Book] = []
```

서버가 종료되거나 다시 실행되면 저장된 데이터는 초기화된다.

---

# Phase 1 - Project Structure and APIRouter

## 학습 목표

- FastAPI 프로젝트 구조를 분리한다.
- `APIRouter`를 이용하여 도서 API를 별도 파일로 관리한다.
- Pydantic 모델을 별도 파일로 분리한다.
- 도서 등록 및 전체 조회 API를 구현한다.
- 중복된 도서 ID가 등록되지 않도록 검증한다.

## APIRouter

```python
router = APIRouter(
    prefix="/books",
    tags=["books"]
)
```

`prefix="/books"`를 설정하면 Router 내부 경로 앞에 `/books`가 자동으로 추가된다.

```python
@router.get("")
```

실제 URL:

```http
GET /books
```

`tags=["books"]`는 Swagger에서 도서 API를 하나의 그룹으로 표시한다.

## Router 등록

`main.py`에서 Router를 FastAPI 애플리케이션에 등록한다.

```python
app.include_router(books.router)
```

`include_router()`로 등록하지 않으면 Router에 작성한 API를 사용할 수 없다.

## Phase 1 구현 기능

- `POST /books`
- `GET /books`
- 중복 ID 검증
- Router 분리
- Pydantic 모델 분리

---

# Phase 2 - CRUD and HTTPException

## 학습 목표

- 전체 CRUD API를 구현한다.
- `HTTPException`을 이용하여 오류를 처리한다.
- 상황에 맞는 HTTP 상태 코드를 반환한다.
- `HTTPStatus`를 사용하여 상태 코드의 의미를 명확하게 표현한다.

---

## 구현한 API

| 기능 | Method | URL | 성공 상태 |
|---|---|---|---|
| 전체 도서 조회 | GET | `/books` | 200 OK |
| 단건 도서 조회 | GET | `/books/{book_id}` | 200 OK |
| 도서 등록 | POST | `/books` | 200 OK |
| 도서 수정 | PUT | `/books/{book_id}` | 200 OK |
| 도서 삭제 | DELETE | `/books/{book_id}` | 200 OK |

현재 생성 API는 기본 상태 코드인 `200 OK`를 사용한다. 이후 단계에서 `201 Created`로 개선할 수 있다.

---

## 전체 도서 조회

```python
@router.get("")
def get_books():
    return books
```

---

## 단건 도서 조회

```python
@router.get("/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )
```

도서가 존재하지 않으면 다음 상태를 반환한다.

```text
404 Not Found
```

응답 예시:

```json
{
  "detail": "Book Not Found"
}
```

---

## 도서 등록

```python
@router.post("")
def create_book(book: Book):
    for saved_book in books:
        if saved_book.id == book.id:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Book ID Already Exists"
            )

    books.append(book)

    return {
        "message": "Book Created",
        "book": book
    }
```

이미 존재하는 ID를 등록하면 다음 상태를 반환한다.

```text
409 Conflict
```

응답 예시:

```json
{
  "detail": "Book ID Already Exists"
}
```

---

## 도서 수정

```python
@router.put("/{book_id}")
def update_book(book_id: int, book: Book):
    for index, saved_book in enumerate(books):
        if saved_book.id == book_id:
            books[index] = book

            return {
                "message": "Book Updated",
                "book": book
            }

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )
```

`enumerate()`를 사용하여 리스트의 인덱스와 도서 객체를 함께 조회한다.

```python
for index, saved_book in enumerate(books):
```

수정 대상은 Request Body의 ID가 아니라 URL의 `book_id`를 기준으로 검색한다.

```python
if saved_book.id == book_id:
```

---

## 도서 삭제

```python
@router.delete("/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)

            return {
                "message": "Book Deleted"
            }

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )
```

존재하지 않는 도서를 삭제하면 `404 Not Found`를 반환한다.

---

## HTTPException

단순히 오류 메시지를 정상 응답으로 반환하지 않고, 상황에 맞는 HTTP 상태 코드를 전달한다.

기존 방식:

```python
return {
    "message": "Book Not Found"
}
```

이 방식은 응답 상태가 `200 OK`이기 때문에 클라이언트가 실패 여부를 정확히 판단하기 어렵다.

개선된 방식:

```python
raise HTTPException(
    status_code=HTTPStatus.NOT_FOUND,
    detail="Book Not Found"
)
```

---

## HTTP 상태 코드

| 상태 코드 | 이름 | 사용 상황 |
|---|---|---|
| 200 | OK | 정상 조회·수정·삭제 |
| 404 | Not Found | 요청한 도서가 존재하지 않음 |
| 409 | Conflict | 이미 존재하는 도서 ID와 충돌 |

---

## HTTPStatus

숫자 상태 코드 대신 Python 표준 라이브러리의 `HTTPStatus`를 사용하였다.

```python
from http import HTTPStatus
```

```python
HTTPStatus.NOT_FOUND
HTTPStatus.CONFLICT
```

다음 두 코드는 동일하게 동작한다.

```python
status_code=404
```

```python
status_code=HTTPStatus.NOT_FOUND
```

`HTTPStatus`를 사용하면 상태 코드의 의미가 코드에 명확하게 드러난다.

---

## Phase 2에서 배운 내용

- CRUD API의 전체 흐름
- Path Parameter와 Request Body의 조합
- `enumerate()`를 이용한 리스트 데이터 수정
- `remove()`를 이용한 데이터 삭제
- `HTTPException`을 이용한 예외 처리
- `404 Not Found`의 사용 상황
- `409 Conflict`의 사용 상황
- `HTTPStatus`를 이용한 가독성 개선
- 성공 시 즉시 `return`하여 예외 코드가 실행되지 않도록 하는 흐름
- URL의 `book_id`를 기준으로 수정 대상을 찾는 방식

---

## 프로젝트 진행 현황

### Phase 1

- [x] 프로젝트 구조 생성
- [x] Pydantic 모델 분리
- [x] `APIRouter` 적용
- [x] Router 등록
- [x] 도서 등록
- [x] 전체 도서 조회
- [x] 중복 ID 검증

### Phase 2

- [x] 단건 도서 조회
- [x] 도서 수정
- [x] 도서 삭제
- [x] `HTTPException` 적용
- [x] `HTTPStatus` 적용
- [x] `404 Not Found` 처리
- [x] `409 Conflict` 처리
- [x] Swagger CRUD 테스트

---

## 다음 단계

Phase 3에서는 Router 내부의 데이터 처리와 비즈니스 로직을 Service 계층으로 분리한다.

현재 구조:

```text
Router
├── HTTP 요청 처리
├── 데이터 검색
├── 중복 검사
├── 데이터 수정
└── 데이터 삭제
```

Phase 3 목표 구조:

```text
Router
   │
   ▼
Service
   │
   ▼
Memory Data
```

Router는 요청과 응답을 담당하고, Service는 조회·등록·수정·삭제 등의 비즈니스 로직을 담당하도록 개선한다.


# Phase 3 - Service Layer

## 학습 목표

- Router에 있던 비즈니스 로직을 Service 계층으로 분리한다.
- 데이터 저장 위치를 별도 모듈로 분리한다.
- Router, Service, Data 계층의 역할을 구분한다.
- 각 함수에 반환 타입을 작성한다.
- 기존 CRUD 기능을 유지하면서 프로젝트 구조를 개선한다.

---

## 프로젝트 구조

Phase 3에서는 다음 구조로 확장하였다.

```text
book-management-api/
├── main.py
├── models.py
├── data/
│   ├── __init__.py
│   └── books.py
├── routers/
│   ├── __init__.py
│   └── books.py
└── services/
    ├── __init__.py
    └── book_service.py
```

### 계층별 역할

| 계층 | 파일 | 역할 |
|---|---|---|
| Router | `routers/books.py` | HTTP 요청 수신, Service 호출, 응답 구성 |
| Service | `services/book_service.py` | 조회·등록·수정·삭제 및 예외 처리 |
| Data | `data/books.py` | 메모리 기반 도서 데이터 보관 |
| Model | `models.py` | Pydantic 데이터 모델 정의 |

---

## Data 계층

도서 목록을 Router에서 분리하여 `data/books.py`에서 관리한다.

```python
from models import Book


books: list[Book] = []
```

현재는 Python List를 메모리 저장소로 사용하므로 서버를 재시작하면 저장된 데이터가 초기화된다.

---

## Service 계층

`book_service.py`는 도서 관련 비즈니스 로직을 담당한다.

```python
from http import HTTPStatus

from fastapi import HTTPException

from data.books import books
from models import Book
```

---

## 전체 도서 조회

```python
def get_books() -> list[Book]:
    return books
```

모든 도서를 리스트 형태로 반환한다.

---

## 단건 도서 조회

```python
def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )
```

도서가 존재하지 않으면 `404 Not Found` 예외를 발생시킨다.

---

## 도서 등록

```python
def create_book(book: Book) -> Book:
    for saved_book in books:
        if saved_book.id == book.id:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Book ID Already Exists"
            )

    books.append(book)
    return book
```

중복된 ID가 존재하면 `409 Conflict`를 반환한다.

등록에 성공하면 저장된 `Book` 객체를 반환한다.

---

## 도서 수정

```python
def update_book(book_id: int, book: Book) -> Book:
    for index, saved_book in enumerate(books):
        if saved_book.id == book_id:
            books[index] = book
            return book

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )
```

URL의 `book_id`를 기준으로 수정 대상을 찾는다.

`enumerate()`를 사용하여 리스트의 인덱스와 객체를 함께 조회한다.

---

## 도서 삭제

```python
def delete_book(book_id: int) -> None:
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )
```

삭제 성공 시 반환값이 없으므로 반환 타입을 `None`으로 작성하였다.

---

## Router 리팩터링

Router가 더 이상 `books` 리스트를 직접 사용하지 않도록 수정하였다.

```python
from fastapi import APIRouter

from models import Book
from services import book_service
```

---

## 전체 조회 Router

```python
@router.get("")
def get_books():
    return book_service.get_books()
```

---

## 단건 조회 Router

```python
@router.get("/{book_id}")
def get_book(book_id: int):
    return book_service.get_book(book_id)
```

---

## 등록 Router

```python
@router.post("")
def create_book(book: Book):
    created_book = book_service.create_book(book)

    return {
        "message": "Book Created",
        "book": created_book
    }
```

중복 확인과 저장은 Service가 담당하고, Router는 응답 형식을 구성한다.

---

## 수정 Router

```python
@router.put("/{book_id}")
def update_book(book_id: int, book: Book):
    updated_book = book_service.update_book(book_id, book)

    return {
        "message": "Book Updated",
        "book": updated_book
    }
```

---

## 삭제 Router

```python
@router.delete("/{book_id}")
def delete_book(book_id: int):
    book_service.delete_book(book_id)

    return {
        "message": "Book Deleted"
    }
```

---

## 역할 분리

### Router

Router는 HTTP 요청과 응답을 담당한다.

```text
URL 정의
Path Parameter 수신
Request Body 수신
Service 호출
Response 구성
```

### Service

Service는 비즈니스 로직을 담당한다.

```text
도서 검색
중복 ID 확인
도서 등록
도서 수정
도서 삭제
예외 처리
```

### Data

Data 계층은 데이터를 보관한다.

```text
books: list[Book]
```

---

## 리팩터링 전후 비교

### Phase 2

```text
Router
├── 요청 처리
├── 데이터 검색
├── 중복 검사
├── 데이터 등록
├── 데이터 수정
├── 데이터 삭제
└── 예외 처리
```

### Phase 3

```text
Router
   │
   ▼
Service
   │
   ▼
Data
```

Router와 비즈니스 로직을 분리하여 각 파일의 책임이 명확해졌다.

---

## Service Layer의 장점

### 관심사 분리

HTTP 요청 처리와 데이터 처리 로직을 분리할 수 있다.

### 코드 재사용

Router가 아닌 다른 코드에서도 Service 함수를 재사용할 수 있다.

### 유지보수성 향상

조회·등록·수정·삭제 로직을 수정할 때 Service 파일만 확인하면 된다.

### 테스트 용이성

HTTP 요청 없이 Service 함수만 독립적으로 테스트할 수 있다.

### 데이터베이스 전환에 유리

현재 메모리 List를 데이터베이스로 변경하더라도 Router 구조를 크게 수정하지 않아도 된다.

---

## 사용하지 않는 Import 정리

Service 분리 후 Router에서는 다음 항목을 직접 사용하지 않는다.

```python
HTTPException
HTTPStatus
```

따라서 Router의 import는 다음처럼 정리할 수 있다.

```python
from fastapi import APIRouter

from models import Book
from services import book_service
```

사용하지 않는 import를 제거하면 코드의 의존 관계가 명확해진다.

---

## 타입 힌트

Service 함수에 반환 타입을 작성하였다.

```python
def get_books() -> list[Book]:
```

```python
def get_book(book_id: int) -> Book:
```

```python
def create_book(book: Book) -> Book:
```

```python
def update_book(book_id: int, book: Book) -> Book:
```

```python
def delete_book(book_id: int) -> None:
```

타입 힌트는 함수의 입력값과 반환값을 명확하게 보여주며, IDE의 자동 완성과 정적 분석에도 도움이 된다.

---

## Phase 3에서 배운 내용

- Service Layer의 개념
- 계층형 프로젝트 구조
- Router와 비즈니스 로직 분리
- 데이터 저장 모듈 분리
- 모듈 단위 import
- Service 함수 호출
- 반환 타입 작성
- 사용하지 않는 import 정리
- 관심사 분리
- 유지보수 가능한 코드 구조
- 데이터베이스 연동을 고려한 구조 설계

---

## Phase 3 완료 조건

- [x] `data` 디렉터리 생성
- [x] `services` 디렉터리 생성
- [x] `data/books.py`에 도서 리스트 분리
- [x] `book_service.py` 생성
- [x] 전체 조회 Service 구현
- [x] 단건 조회 Service 구현
- [x] 등록 Service 구현
- [x] 수정 Service 구현
- [x] 삭제 Service 구현
- [x] Service에서 404 예외 처리
- [x] Service에서 409 예외 처리
- [x] Service 함수 반환 타입 작성
- [x] Router에서 직접 데이터 접근 제거
- [x] Router에서 Service 호출
- [x] 기존 CRUD 기능 유지
- [x] 사용하지 않는 Router import 확인

---

## 다음 단계

Phase 4에서는 메모리 기반 저장소를 실제 데이터베이스로 교체한다.

현재 구조:

```text
Router
   │
   ▼
Service
   │
   ▼
Memory Data
```

Phase 4 목표 구조:

```text
Router
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
SQLite Database
```

Phase 4에서는 다음 내용을 학습한다.

- SQLite
- SQLAlchemy ORM
- 데이터베이스 연결
- 테이블 생성
- Session 관리
- 데이터베이스 기반 CRUD
- Repository 계층
- 서버 재시작 후 데이터 유지
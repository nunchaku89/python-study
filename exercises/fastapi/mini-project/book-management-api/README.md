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


# Phase 4 - Database Integration

Phase 4에서는 Python List 기반의 메모리 저장소를 SQLite 데이터베이스로 교체한다.

전체 과정은 다음 단계로 나누어 진행한다.

```text
Phase 4-1  SQLite·SQLAlchemy 환경 구성
Phase 4-2  Repository 계층과 조회·등록
Phase 4-3  수정·삭제 및 전체 CRUD 전환
Phase 4-4  데이터베이스 세션 의존성 개선
```

---

# Phase 4-1 - SQLite and SQLAlchemy Setup

## 학습 목표

- SQLAlchemy를 설치하고 SQLite 연결을 구성한다.
- SQLAlchemy Engine과 Session Factory를 생성한다.
- ORM Entity를 정의한다.
- Python 클래스를 데이터베이스 테이블과 연결한다.
- 애플리케이션 실행 시 테이블을 생성한다.
- SQLite 데이터베이스 파일 생성을 확인한다.

---

## 프로젝트 구조

Phase 4-1을 완료한 프로젝트 구조는 다음과 같다.

```text
book-management-api/
├── main.py
├── database.py
├── entities.py
├── models.py
├── books.db
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

현재 `books.db`는 생성되었지만, 기존 CRUD API는 아직 메모리 List를 사용한다.

다음 단계에서 Repository 계층을 추가하여 실제 데이터베이스를 사용하도록 변경한다.

---

## SQLAlchemy 설치

가상환경이 활성화된 상태에서 다음 명령으로 SQLAlchemy를 설치한다.

```powershell
pip install sqlalchemy
```

설치 확인:

```powershell
pip show sqlalchemy
```

---

## 데이터베이스 연결 설정

`database.py`에서 SQLite 연결과 SQLAlchemy 기반 설정을 정의하였다.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = "sqlite:///./books.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass
```

---

## DATABASE_URL

```python
DATABASE_URL = "sqlite:///./books.db"
```

구성 요소의 의미는 다음과 같다.

```text
sqlite       SQLite 데이터베이스 사용
:///         상대경로 파일 사용
./books.db   현재 실행 위치에 데이터베이스 파일 생성
```

---

## Engine

```python
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
```

Engine은 애플리케이션과 데이터베이스 사이의 연결을 관리한다.

```text
FastAPI
   │
   ▼
SQLAlchemy Engine
   │
   ▼
SQLite
```

SQLite를 FastAPI 요청 환경에서 사용하기 위해 다음 옵션을 설정하였다.

```python
connect_args={"check_same_thread": False}
```

---

## SessionLocal

```python
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
```

`SessionLocal`은 데이터베이스 작업에 사용할 Session 객체를 생성한다.

이후 Repository 계층에서 다음과 같은 방식으로 사용한다.

```python
db = SessionLocal()
```

Session은 데이터베이스의 조회·등록·수정·삭제와 트랜잭션 처리를 담당한다.

---

## DeclarativeBase

```python
class Base(DeclarativeBase):
    pass
```

`Base`는 SQLAlchemy Entity가 상속하는 공통 기반 클래스이다.

```python
class BookEntity(Base):
    ...
```

Entity가 `Base`를 상속하면 해당 클래스의 테이블 정보가 SQLAlchemy Metadata에 등록된다.

---

## Pydantic Model과 SQLAlchemy Entity

프로젝트에는 역할이 다른 두 종류의 모델이 존재한다.

| 구분 | 클래스 | 파일 | 역할 |
|---|---|---|---|
| Pydantic Model | `Book` | `models.py` | API 요청 데이터 검증 |
| SQLAlchemy Entity | `BookEntity` | `entities.py` | 데이터베이스 테이블 매핑 |

### Pydantic Model

```python
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
```

주요 역할:

```text
Request Body 검증
Python 타입 검증
Swagger 문서 생성
API 데이터 구조 표현
```

### SQLAlchemy Entity

```python
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class BookEntity(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    author: Mapped[str] = mapped_column(String(100))
```

주요 역할:

```text
books 테이블 정의
Python 객체와 데이터베이스 행 연결
컬럼 타입과 제약조건 정의
```

---

## 테이블 이름

```python
__tablename__ = "books"
```

데이터베이스에 생성되는 테이블 이름은 `books`이다.

---

## 기본키

```python
id: Mapped[int] = mapped_column(primary_key=True)
```

`id`는 각 도서 데이터를 고유하게 구분하는 기본키이다.

기본키는 중복될 수 없다.

---

## 문자열 컬럼

```python
title: Mapped[str] = mapped_column(String(200))
author: Mapped[str] = mapped_column(String(100))
```

컬럼별 최대 길이는 다음과 같다.

```text
title   200자
author  100자
```

---

## 테이블 생성

`main.py`에서 SQLAlchemy Metadata를 이용해 테이블을 생성한다.

```python
from fastapi import FastAPI

import entities
from database import Base, engine
from routers import books


Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(books.router)
```

---

## Entity import가 필요한 이유

```python
import entities
```

이 코드는 변수나 함수를 직접 사용하기 위한 import가 아니다.

`entities.py`가 실행되어야 `BookEntity`가 SQLAlchemy Metadata에 등록된다.

실행 흐름은 다음과 같다.

```text
entities.py import
        │
        ▼
BookEntity 클래스 실행
        │
        ▼
books 테이블 정보 등록
        │
        ▼
Base.metadata.create_all()
        │
        ▼
SQLite books 테이블 생성
```

---

## 데이터베이스 파일 생성 확인

서버를 실행하였다.

```powershell
uvicorn main:app --reload
```

실행 후 프로젝트 디렉터리에 다음 파일이 생성된 것을 확인하였다.

```text
books.db
```

이 결과는 다음 구성이 정상적으로 동작했다는 의미이다.

```text
SQLite 연결                ✅
SQLAlchemy Engine 생성     ✅
BookEntity 등록            ✅
Metadata 테이블 생성       ✅
books.db 파일 생성         ✅
```

---

## 현재 데이터 흐름

현재 SQLite 연결과 테이블은 생성되었지만, CRUD 기능은 아직 메모리 저장소를 사용한다.

```text
Router
   │
   ▼
Service
   │
   ▼
Python List
```

현재 Service에서는 다음 데이터에 접근한다.

```python
from data.books import books
```

Phase 4-2에서 Repository 계층을 만들고 데이터 흐름을 다음처럼 변경한다.

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
SQLAlchemy Session
   │
   ▼
SQLite
```

---

## Git에서 데이터베이스 파일 제외

`books.db`는 로컬 실행 과정에서 생성되는 테스트 데이터 파일이므로 Git에서 제외한다.

`.gitignore`:

```gitignore
# Python cache
__pycache__/
*.pyc

# Virtual environment
.venv/

# SQLite database
*.db
```

테이블 구조와 Entity 코드는 Git에 포함하지만, 로컬 테스트 데이터는 포함하지 않는다.

---

## Phase 4-1에서 배운 내용

- SQLite 데이터베이스의 기본 개념
- SQLAlchemy Engine
- `sessionmaker`
- 데이터베이스 Session
- `DeclarativeBase`
- SQLAlchemy ORM Entity
- `Mapped`
- `mapped_column`
- 기본키
- 문자열 컬럼
- Pydantic Model과 ORM Entity의 차이
- SQLAlchemy Metadata
- `Base.metadata.create_all()`
- Entity import와 테이블 등록 과정
- SQLite 데이터베이스 파일 생성
- 로컬 DB 파일의 Git 제외

---

## Phase 4-1 완료 조건

- [x] SQLAlchemy 설치
- [x] `database.py` 생성
- [x] SQLite 연결 URL 작성
- [x] SQLAlchemy Engine 생성
- [x] `SessionLocal` 생성
- [x] `DeclarativeBase` 정의
- [x] `entities.py` 생성
- [x] `BookEntity` 정의
- [x] `books` 테이블 이름 지정
- [x] `id` 기본키 설정
- [x] `title` 컬럼 설정
- [x] `author` 컬럼 설정
- [x] `main.py`에서 Entity import
- [x] `Base.metadata.create_all()` 실행
- [x] `books.db` 생성 확인
- [ ] `.gitignore`에 `*.db` 추가 확인

---

## 다음 단계

Phase 4-2에서는 Repository 계층을 추가하고 도서 등록과 조회 기능을 SQLite로 전환한다.

추가될 구조:

```text
book-management-api/
└── repositories/
    ├── __init__.py
    └── book_repository.py
```

구현할 기능:

```text
BookEntity 생성
데이터베이스 INSERT
전체 도서 SELECT
ID를 이용한 단건 SELECT
Session commit
Session refresh
```

Phase 4-2 완료 후에는 등록한 도서가 서버를 다시 실행해도 유지된다.


# Phase 4-2 - Repository and Read/Create

## 학습 목표

- Repository 계층의 역할을 이해한다.
- SQLAlchemy Session을 이용해 데이터를 조회하고 등록한다.
- SQLAlchemy Entity와 Pydantic Model을 변환한다.
- Service와 데이터베이스 접근 로직을 분리한다.
- 도서 조회와 등록 기능을 SQLite 기반으로 전환한다.
- 서버 재시작 후에도 데이터가 유지되는지 확인한다.

---

## 프로젝트 구조

```text
book-management-api/
├── main.py
├── database.py
├── entities.py
├── models.py
├── books.db
├── repositories/
│   ├── __init__.py
│   └── book_repository.py
├── routers/
│   ├── __init__.py
│   └── books.py
└── services/
    ├── __init__.py
    └── book_service.py
```

---

## 계층 구조

Phase 4-2부터 데이터베이스 접근을 전담하는 Repository 계층을 사용한다.

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
SQLAlchemy Session
   │
   ▼
SQLite
```

각 계층의 역할은 다음과 같다.

| 계층 | 역할 |
|---|---|
| Router | HTTP 요청 수신과 응답 구성 |
| Service | 비즈니스 규칙과 예외 처리 |
| Repository | 데이터베이스 조회와 저장 |
| Entity | 데이터베이스 테이블 매핑 |
| Pydantic Model | API 데이터 검증과 직렬화 |

---

## Pydantic ORM 변환 설정

`models.py`:

```python
from pydantic import BaseModel, ConfigDict


class Book(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    author: str
```

다음 설정을 추가하였다.

```python
model_config = ConfigDict(from_attributes=True)
```

이 설정을 사용하면 SQLAlchemy Entity의 속성을 읽어 Pydantic 모델을 생성할 수 있다.

```python
book = Book.model_validate(book_entity)
```

변환 대상은 다음과 같다.

```text
book_entity.id
book_entity.title
book_entity.author
```

---

## Pydantic Model과 Entity

프로젝트에서는 역할이 다른 두 개의 도서 클래스를 사용한다.

```text
Book
API 요청·응답 모델

BookEntity
데이터베이스 테이블 모델
```

### API 요청에서 데이터베이스로 저장

```text
JSON
 ↓
Book
 ↓
BookEntity
 ↓
SQLite
```

### 데이터베이스 조회 결과를 API로 반환

```text
SQLite
 ↓
BookEntity
 ↓
Book
 ↓
JSON
```

---

## Repository 계층

`repositories/book_repository.py`:

```python
from sqlalchemy import select

from database import SessionLocal
from entities import BookEntity


def get_books() -> list[BookEntity]:
    with SessionLocal() as db:
        statement = select(BookEntity)
        books = db.scalars(statement).all()

        return list(books)


def get_book(book_id: int) -> BookEntity | None:
    with SessionLocal() as db:
        return db.get(BookEntity, book_id)


def create_book(book_entity: BookEntity) -> BookEntity:
    with SessionLocal() as db:
        db.add(book_entity)
        db.commit()
        db.refresh(book_entity)

        return book_entity
```

Repository는 FastAPI의 HTTP 요청이나 상태 코드를 알지 못한다.

Repository의 책임은 다음과 같다.

```text
SQL 작성
Session 관리
데이터 조회
데이터 등록
Entity 반환
```

---

## 전체 도서 조회

```python
def get_books() -> list[BookEntity]:
    with SessionLocal() as db:
        statement = select(BookEntity)
        books = db.scalars(statement).all()

        return list(books)
```

다음 코드는 `BookEntity`를 대상으로 SELECT 문을 생성한다.

```python
statement = select(BookEntity)
```

개념적으로 다음 SQL에 해당한다.

```sql
SELECT id, title, author
FROM books;
```

다음 코드는 조회 결과의 각 행을 `BookEntity` 객체로 반환한다.

```python
db.scalars(statement).all()
```

---

## 단건 조회

```python
def get_book(book_id: int) -> BookEntity | None:
    with SessionLocal() as db:
        return db.get(BookEntity, book_id)
```

`db.get()`은 기본키를 기준으로 데이터를 조회한다.

```python
db.get(BookEntity, book_id)
```

반환 결과:

```text
도서 존재      BookEntity
도서 없음      None
```

Repository는 데이터가 없는 경우에도 `HTTPException`을 발생시키지 않는다.

데이터가 없다는 사실을 어떤 HTTP 상태로 표현할지는 Service가 결정한다.

---

## 도서 등록

```python
def create_book(book_entity: BookEntity) -> BookEntity:
    with SessionLocal() as db:
        db.add(book_entity)
        db.commit()
        db.refresh(book_entity)

        return book_entity
```

### `add()`

```python
db.add(book_entity)
```

Entity를 현재 Session의 관리 대상으로 등록한다.

### `commit()`

```python
db.commit()
```

트랜잭션의 변경 내용을 데이터베이스에 반영한다.

### `refresh()`

```python
db.refresh(book_entity)
```

데이터베이스에 저장된 최신 데이터를 Entity에 다시 반영한다.

---

## Service 계층 전환

`services/book_service.py`:

```python
from http import HTTPStatus

from fastapi import HTTPException

from entities import BookEntity
from models import Book
from repositories import book_repository


def get_books() -> list[Book]:
    book_entities = book_repository.get_books()

    return [
        Book.model_validate(book_entity)
        for book_entity in book_entities
    ]


def get_book(book_id: int) -> Book:
    book_entity = book_repository.get_book(book_id)

    if book_entity is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Book Not Found"
        )

    return Book.model_validate(book_entity)


def create_book(book: Book) -> Book:
    saved_book = book_repository.get_book(book.id)

    if saved_book is not None:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail="Book ID Already Exists"
        )

    book_entity = BookEntity(
        id=book.id,
        title=book.title,
        author=book.author
    )

    created_entity = book_repository.create_book(book_entity)

    return Book.model_validate(created_entity)
```

Service는 다음 역할을 담당한다.

```text
중복 ID 검사
404 예외 처리
409 예외 처리
Book과 BookEntity 변환
Repository 호출
```

---

## 전체 조회 흐름

```text
GET /books
      │
      ▼
Router
      │
      ▼
Service.get_books()
      │
      ▼
Repository.get_books()
      │
      ▼
SELECT
      │
      ▼
list[BookEntity]
      │
      ▼
list[Book]
      │
      ▼
JSON Response
```

Repository가 반환한 Entity 목록을 다음 코드로 변환한다.

```python
return [
    Book.model_validate(book_entity)
    for book_entity in book_entities
]
```

---

## 단건 조회 흐름

```text
GET /books/{book_id}
      │
      ▼
Repository.get_book()
      │
      ├── BookEntity
      │        ↓
      │      Book으로 변환
      │
      └── None
               ↓
          404 Not Found
```

Service가 `None`을 HTTP 오류로 변환한다.

```python
if book_entity is None:
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )
```

---

## 등록 흐름

```text
POST /books
      │
      ▼
Book 요청 모델
      │
      ▼
동일 ID 조회
      │
      ├── 존재함 → 409 Conflict
      │
      └── 존재하지 않음
                  │
                  ▼
            BookEntity 생성
                  │
                  ▼
            Repository 저장
                  │
                  ▼
              SQLite INSERT
                  │
                  ▼
            Book으로 변환
```

Entity 생성:

```python
book_entity = BookEntity(
    id=book.id,
    title=book.title,
    author=book.author
)
```

중복 ID가 존재하면 다음 오류를 반환한다.

```python
raise HTTPException(
    status_code=HTTPStatus.CONFLICT,
    detail="Book ID Already Exists"
)
```

---

## 메모리 저장소와 SQLite의 차이

### 메모리 저장소

```text
서버 실행
   ↓
데이터 등록
   ↓
Python List 저장
   ↓
서버 종료
   ↓
데이터 소멸
```

### SQLite 저장소

```text
서버 실행
   ↓
데이터 등록
   ↓
books.db 저장
   ↓
서버 종료
   ↓
서버 재실행
   ↓
데이터 유지
```

---

## 영구 저장 검증

다음 순서로 테스트하였다.

```text
1. POST /books로 도서 등록
2. GET /books로 등록 결과 확인
3. 서버 종료
4. 서버 재실행
5. GET /books 재호출
```

서버를 다시 실행한 뒤에도 등록한 도서가 조회되는 것을 확인하였다.

```text
SQLite 데이터 저장         ✅
서버 재시작                ✅
등록 데이터 유지           ✅
```

이 결과를 통해 조회와 등록 기능이 `data/books.py`의 메모리 리스트가 아니라 SQLite의 `books` 테이블을 사용한다는 것을 확인하였다.

---

## Phase 4-2 API

현재 SQLite로 전환된 API는 다음과 같다.

| Method | URL | 기능 |
|---|---|---|
| GET | `/books` | 전체 도서 조회 |
| GET | `/books/{book_id}` | 단건 도서 조회 |
| POST | `/books` | 도서 등록 |

수정과 삭제는 다음 단계에서 SQLite로 전환한다.

---

## Phase 4-2에서 배운 내용

- Repository Pattern
- 계층별 책임 분리
- SQLAlchemy `select()`
- `Session.scalars()`
- `Session.get()`
- `Session.add()`
- `Session.commit()`
- `Session.refresh()`
- Pydantic `ConfigDict`
- `from_attributes=True`
- `Book`과 `BookEntity` 변환
- Repository와 HTTP 예외의 분리
- SQLite 영구 저장 검증

---

## Phase 4-2 완료 조건

- [x] `models.py`에 `from_attributes=True` 설정
- [x] `repositories` 패키지 생성
- [x] 전체 조회 Repository 구현
- [x] 단건 조회 Repository 구현
- [x] 등록 Repository 구현
- [x] Service 전체 조회 전환
- [x] Service 단건 조회 전환
- [x] Service 등록 전환
- [x] `BookEntity`를 `Book`으로 변환
- [x] `Book`을 `BookEntity`로 변환
- [x] 없는 ID에 대해 404 처리
- [x] 중복 ID에 대해 409 처리
- [x] SQLite 데이터 등록 확인
- [x] 서버 재시작 후 데이터 유지 확인

---

## 다음 단계

Phase 4-3에서는 수정과 삭제 기능을 SQLite 기반으로 전환한다.

추가할 Repository 기능:

```text
update_book()
delete_book()
```

복원할 API:

```text
PUT    /books/{book_id}
DELETE /books/{book_id}
```

Phase 4-3이 완료되면 모든 CRUD 기능이 SQLite를 사용하게 된다.


## Phase 4-4 - Database Session Dependency

### 목표

FastAPI Dependency Injection을 이용하여 요청당 하나의 SQLAlchemy Session을 공유하도록 구조를 개선하였다.

### 변경 사항

- `get_db()` Dependency 추가
- Repository에서 Session 생성 제거
- Repository가 Session을 매개변수로 전달받도록 변경
- Service가 Session을 Repository로 전달
- Router에서 `Depends(get_db)` 사용

### 요청 흐름

Client
↓
Router
↓
Depends(get_db)
↓
Session
↓
Service
↓
Repository
↓
SQLite

### 학습 내용

- FastAPI Dependency Injection
- SQLAlchemy Session Lifecycle
- 요청당 하나의 Session 사용
- Repository Pattern 개선
- 계층 간 의존성 분리


## Request / Response Models

API 요청과 응답 모델을 분리하여 각 모델의 책임을 명확하게 구성했습니다.

### Request Models

- `BookCreate`
- `BookUpdate`

### Response Model

- `BookResponse`

### Entity

- `BookEntity`

```
Client
    │
BookCreate / BookUpdate
    │
Service
    │
Repository
    │
BookEntity
    │
BookResponse
    │
Client
```

### Validation

입력 데이터는 Pydantic `Field()`를 이용하여 검증합니다.

| Field | Validation |
|-------|------------|
| title | 1~200자 |
| author | 2~100자 |
| id | 0보다 큰 정수 |

잘못된 입력은 FastAPI가 자동으로 `422 Unprocessable Entity`를 반환합니다.

### Response Model

모든 API는 `response_model`을 사용하여 응답 형식을 검증하고 Swagger 문서를 자동 생성합니다.


## Input Validation

모든 입력 데이터는 Pydantic Validation을 통해 검증됩니다.

### Field Validation

| Field | Rule |
|------|------|
| title | 1~200자 |
| author | 2~100자 |
| id | 0보다 큰 정수(Response Model) |

### Custom Validation

`BookBase`에서 `field_validator`를 사용하여 공백만 입력되는 문자열을 차단합니다.

```python
@field_validator("title", "author")
@classmethod
def validate_not_blank(cls, value: str) -> str:
    value = value.strip()

    if not value:
        raise ValueError("must not be blank")

    return value
```

입력 예시

❌ 허용되지 않는 입력

```json
{
  "title": "     ",
  "author": "Wayne"
}
```

✅ 허용되는 입력

```json
{
  "title": "   Clean Code   ",
  "author": "  Robert C. Martin "
}
```

저장 시 자동으로 앞뒤 공백이 제거됩니다.



## PATCH Support (Preparation)

부분 수정(HTTP PATCH)을 지원하기 위해 `BookPatch` 모델을 추가했습니다.

### BookPatch

```python
class BookPatch(BaseModel):
    title: str | None
    author: str | None
```

### 특징

- 모든 필드가 Optional
- 전달된 필드만 수정 가능
- Custom Validator를 통해 공백 문자열 차단
- `None`은 허용하여 부분 수정 지원

PATCH 구현은 다음 단계에서 `exclude_unset=True`를 사용하여 완료합니다.
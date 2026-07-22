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
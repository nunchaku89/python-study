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
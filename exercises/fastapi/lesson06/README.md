# Lesson 06 - CRUD API

## 학습 목표

- CRUD(Create, Read, Update, Delete)의 개념을 이해한다.
- HTTP Method(GET, POST, PUT, DELETE)를 활용한다.
- 메모리(List)를 이용하여 간단한 CRUD API를 구현한다.
- Path Parameter와 Request Body를 함께 사용하는 방법을 익힌다.

---

## 학습 내용

### CRUD란?

CRUD는 대부분의 웹 서비스가 제공하는 기본 기능이다.

| 기능 | HTTP Method |
|------|-------------|
| Create | POST |
| Read | GET |
| Update | PUT |
| Delete | DELETE |

---

## 메모리 저장소

이번 실습에서는 데이터베이스 대신 Python List를 사용하였다.

```python
books = []
```

프로그램이 실행되는 동안만 데이터가 유지되며, 서버를 재시작하면 초기화된다.

---

## 구현한 API

### Create

```http
POST /books
```

새로운 책을 등록한다.

---

### Read (전체 조회)

```http
GET /books
```

등록된 모든 책을 조회한다.

---

### Read (단건 조회)

```http
GET /books/{book_id}
```

ID로 책을 조회한다.

존재하지 않는 경우

```json
{
  "message": "Book Not Found"
}
```

를 반환한다.

---

### Update

```http
PUT /books/{book_id}
```

기존 책 정보를 수정한다.

`enumerate()`를 이용하여 리스트의 index를 찾아 수정하였다.

---

### Delete

```http
DELETE /books/{book_id}
```

책을 삭제한다.

삭제 후에는 다시 조회하면 존재하지 않는다.

---

## 새롭게 배운 내용

- Python List를 메모리 저장소처럼 사용할 수 있다.
- enumerate()를 이용하여 리스트 요소를 수정할 수 있다.
- remove()를 이용하여 리스트 요소를 삭제할 수 있다.
- CRUD는 데이터베이스를 사용하더라도 동일한 흐름으로 동작한다.
- 존재하지 않는 데이터에 대한 예외 처리가 필요하다.

---

## 다음 학습

Mini Project

Book Management API
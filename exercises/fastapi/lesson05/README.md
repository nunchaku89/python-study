# Lesson 05 - Request Body

## 학습 목표

- HTTP Request Body의 개념을 이해한다.
- POST Method를 이용하여 데이터를 생성한다.
- Pydantic Model을 Request Body로 사용한다.
- FastAPI의 자동 Validation을 이해한다.

---

## 학습 내용

### Request Body

Request Body는 클라이언트가 서버에 전달하는 데이터이다.

FastAPI는 Request Body의 JSON을 Pydantic 객체로 자동 변환한다.

예시

```json
{
  "id": 1,
  "name": "Wayne",
  "job": "AI Developer"
}
```

↓

```python
User(
    id=1,
    name="Wayne",
    job="AI Developer"
)
```

---

### POST API

```python
@app.post("/users")
def create_user(user: User):
    return {
        "message": "User Created",
        "user": user
    }
```

---

## 구현한 API

- POST /users
- POST /books
- POST /students
- POST /movies

---

## Validation

Pydantic은 요청 데이터를 자동으로 검증한다.

예시

```json
{
    "id": "ABC",
    "title": "Python",
    "author": "Wayne"
}
```

↓

HTTP Status

```
422 Unprocessable Entity
```

오류

```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": ["body", "id"],
      "msg": "Input should be a valid integer",
      "input": "ABC"
    }
  ]
}
```

---

## 새롭게 배운 내용

- Request Body는 JSON 형태로 전달된다.
- FastAPI는 JSON을 Pydantic 객체로 변환한다.
- 타입 검증은 자동으로 수행된다.
- Validation 실패 시 422 오류를 반환한다.
- Validation 오류는 어떤 필드에서 발생했는지 알려준다.

---

## 다음 학습

- CRUD API
- PUT
- DELETE
- 메모리 기반 데이터 관리
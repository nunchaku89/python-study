# Lesson 02 - Path Parameter

## 학습 목표

- Path Parameter의 개념을 이해한다.
- URL을 통해 데이터를 전달하는 방법을 학습한다.
- FastAPI에서 Path Parameter를 사용하는 방법을 익힌다.

---

## 학습 내용

### Path Parameter

Path Parameter는 URL 경로의 일부를 변수처럼 사용하는 방식이다.

예시
GET /users/1
GET /books/10
GET /students/5

여기서 `1`, `10`, `5`가 Path Parameter이다.

FastAPI에서는 함수의 매개변수와 자동으로 연결된다.

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id
    }

실습

구현한 API

GET /
GET /users/{user_id}
GET /books/{book_id}
GET /students/{student_id}
GET /users/{user_id}/posts/{post_id}

실행 결과
{
    "id": 1,
    "name": "Wayne",
    "job": "AI Developer"
}
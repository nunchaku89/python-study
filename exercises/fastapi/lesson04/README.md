# Lesson 04 - Response Model (Pydantic)

## 학습 목표

- Pydantic의 역할을 이해한다.
- Response Model을 사용하는 이유를 이해한다.
- BaseModel을 이용하여 응답 형식을 정의한다.
- FastAPI가 응답 데이터를 자동으로 검증하는 과정을 이해한다.

---

## 학습 내용

### Pydantic

Pydantic은 데이터의 구조와 타입을 정의하고 검증하는 라이브러리이다.

FastAPI는 Pydantic을 이용하여 Request와 Response를 검증한다.

---

### Response Model

Response Model은 API가 반환하는 데이터의 구조를 정의한다.

```python
class Book(BaseModel):
    id: int
    title: str
    author: str
# Lesson 03 - Query Parameter

## 학습 목표

- Query Parameter의 개념을 이해한다.
- Path Parameter와 Query Parameter의 차이를 이해한다.
- 검색 API를 구현한다.
- 기본값(Default Value)을 활용한다.

---

## 학습 내용

### Query Parameter

Query Parameter는 URL 뒤에 `?`를 사용하여 검색 조건을 전달하는 방식이다.

예시

- GET /movies?title=Inception
- GET /students?name=Hong&grade=3
- GET /products?page=2&size=20

FastAPI에서는 함수의 매개변수와 자동으로 연결된다.

```python
@app.get("/movies")
def get_movies(title: str):
    return {"title": title}
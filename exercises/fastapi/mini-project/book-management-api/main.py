from fastapi import FastAPI
from routers import books

app = FastAPI(
    title="Book Management API",
    description="도서를 등록하고 관리하는 API",
    version="1.0.0"
)

app.include_router(books.router)

@app.get("/")
def root():
    return {
        "message": "Book Management API"
    }
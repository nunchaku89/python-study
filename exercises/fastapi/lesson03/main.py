from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello FastAPI!"
    }

@app.get("/users")
def get_users(name: str = "Guest"):
    return {
        "name": name
    }

@app.get("/books")
def get_books(title: str, author: str):
    return {
        "title": title,
        "author": author
    }

@app.get("/movies")
def get_movies(title: str):
    return {
        "title": title
    }

@app.get("/students")
def get_students(name: str, grade: int):
    return {
        "name": name,
        "grade": grade
    }

@app.get("/products")
def get_products(page: int = 1, size: int = 10):
    return {
        "page": page,
        "size": size
    }

@app.get("/search")
def search(keyword: str, sort: str, page: int):
    return {
        "keyword": keyword,
        "sort": sort,
        "page": page
    }
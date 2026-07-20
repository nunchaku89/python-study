from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello FastAPI!"
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "Wayne",
        "job": "AI Developer"
    }

@app.get("/books/{book_id}")
def get_book(book_id: int):
    return {
        "id": book_id,
        "title": "Python Study",
        "author": "Wayne"
    }

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "id": student_id,
        "name": "Hong",
        "grade": 3
    }

@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):
    return {
        "user_id": user_id,
        "post_id": post_id
    }
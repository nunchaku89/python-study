from fastapi import FastAPI
from model import User, Book, Student, Movie

app = FastAPI()

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User Created",
        "user": user
    }

@app.post("/books")
def create_book(book: Book):
    return {
        "message": "Book Created",
        "book": book
    }

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student Created",
        "student": student
    }

@app.post("/movies")
def create_movie(movie: Movie):
    return {
        "message": "Movie Created",
        "movie": movie
    }
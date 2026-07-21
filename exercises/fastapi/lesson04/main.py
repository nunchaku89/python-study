from fastapi import FastAPI
from models import User
from models import Book
from models import Student
from models import Movie

app = FastAPI()

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "Wayne",
        "job": "AI Developer"
    }

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    return {
        "id": book_id,
        "title": "Python",
        "author": "Monty",
        "price": 3000
    }

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    return {
        "id": student_id,
        "name": "Wayne",
        "grade": "4"
    }

@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    return {
        "id": movie_id,
        "title": "Inception",
        "director": "Christopher",
        "year": 2020
    }
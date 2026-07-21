from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    job: str

class Book(BaseModel):
    id: int
    title: str
    author: str

class Student(BaseModel):
    id: int
    name: str
    grade: int

class Movie(BaseModel):
    id: int
    title: str
    director: str
    year: int
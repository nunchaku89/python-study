from fastapi import APIRouter
from models import Book

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

books: list[Book] = []

@router.get("")
def get_books():
    return books

@router.post("")
def create_book(book: Book):

    for saved_book in books:
        if saved_book.id == book.id:
            return {
                "message": "Book Id Already Exists"
            }

    books.append(book)

    return {
        "message": "Book Created",
        "book": book
    }
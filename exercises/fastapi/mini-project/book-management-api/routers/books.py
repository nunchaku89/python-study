from fastapi import APIRouter, HTTPException
from models import Book
from http import HTTPStatus

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

books: list[Book] = []

@router.get("")
def get_books():
    return books

@router.get("/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )

@router.post("")
def create_book(book: Book):

    for saved_book in books:
        if saved_book.id == book.id:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Book ID Already Exists"
            )

    books.append(book)

    return {
        "message": "Book Created",
        "book": book
    }

@router.put("/{book_id}")
def update_book(book_id: int, book: Book):
    for index, saved_book in enumerate(books):
        if saved_book.id == book_id:
           books[index] = book
           return {
               "message": "Book Updated",
               "book": book
           }

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )

@router.delete("/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {
                "message": "Book Deleted"
            }
    
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )
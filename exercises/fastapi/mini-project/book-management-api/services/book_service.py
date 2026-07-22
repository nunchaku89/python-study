from http import HTTPStatus
from fastapi import HTTPException
from data.books import books
from models import Book

def get_books() -> list[Book]:
    return books

def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )

def create_book(book: Book) -> Book:
    for saved_book in books:
        if saved_book.id == book.id:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Book ID Already Exists"
            )

    books.append(book)

    return book

def update_book(book_id: int, book: Book) -> Book:
    for index, saved_book in enumerate(books):
        if saved_book.id == book_id:
            books[index] = book

            return book

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )

def delete_book(book_id: int) -> None:
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Book Not Found"
    )
from http import HTTPStatus

from fastapi import HTTPException

from entities import BookEntity
from models import Book
from repositories import book_repository

def get_books() -> list[Book]:
    book_entities = book_repository.get_books()

    return [
        Book.model_validate(book_entity)
        for book_entity in book_entities
    ]

def get_book(book_id: int) -> Book:
    book_entity = book_repository.get_book(book_id)

    if book_entity is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Book Not Found"
        )

    return Book.model_validate(book_entity)

def create_book(book: Book) -> Book:
    saved_book = book_repository.get_book(book.id)

    if saved_book is not None:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail="Book ID Already Exists"
        )

    book_entity = BookEntity(
        id=book.id,
        title=book.title,
        author=book.author
    )

    created_entity = book_repository.create_book(book_entity)

    return Book.model_validate(created_entity)
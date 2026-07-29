from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.orm import Session

from entities import BookEntity
from models import Book
from repositories import book_repository

def get_books(db: Session) -> list[Book]:
    book_entities = book_repository.get_books(db)

    return [
        Book.model_validate(book_entity)
        for book_entity in book_entities
    ]


def get_book(
        db: Session,
        book_id: int
) -> Book:
    book_entity = book_repository.get_book(db, book_id)

    if book_entity is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Book Not Found"
        )

    return Book.model_validate(book_entity)


def create_book(
        db: Session,
        book: Book
) -> Book:
    saved_book = book_repository.get_book(db, book.id)

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

    created_entity = book_repository.create_book(db, book_entity)

    return Book.model_validate(created_entity)


def update_book(
        db: Session,
        book_id: int,
        book: Book
) -> Book:
    saved_entity = book_repository.get_book(db, book_id)

    if saved_entity is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Book Not Found"
        )

    updated_entity = book_repository.update_book(
        db=db,
        book_entity=saved_entity,
        title=book.title,
        author=book.author
    )

    return Book.model_validate(updated_entity)


def delete_book(
        db: Session,
        book_id: int
) -> None:
    saved_book = book_repository.get_book(db, book_id)

    if saved_book is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Book Not Found"
        )

    book_repository.delete_book(db, saved_book)
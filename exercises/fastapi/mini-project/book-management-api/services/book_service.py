from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from entities import BookEntity
from models import BookCreate, BookUpdate, BookPatch, BookResponse
from repositories import book_repository

def get_books(db: Session) -> list[BookResponse]:
    book_entities = book_repository.get_books(db)

    return [
        BookResponse.model_validate(book_entity)
        for book_entity in book_entities
    ]


def get_book(
        db: Session,
        book_id: int
) -> BookResponse:
    book_entity = book_repository.get_book(db, book_id)

    if book_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book Not Found"
        )

    return BookResponse.model_validate(book_entity)


def create_book(
        db: Session,
        book: BookCreate
) -> BookResponse:
    book_entity = BookEntity(
        title=book.title,
        author=book.author
    )

    created_entity = book_repository.create_book(
        db=db,
        book_entity=book_entity
    )

    return BookResponse.model_validate(created_entity)


def update_book(
        db: Session,
        book_id: int,
        book: BookUpdate
) -> BookResponse:
    saved_entity = book_repository.get_book(db, book_id)

    if saved_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book Not Found"
        )

    updated_entity = book_repository.update_book(
        db=db,
        book_entity=saved_entity,
        title=book.title,
        author=book.author
    )

    return BookResponse.model_validate(updated_entity)


def patch_book(
        db: Session,
        book_id: int,
        book: BookPatch
) -> BookResponse:
    saved_entity = book_repository.get_book(
        db=db,
        book_id=book_id
    )

    if saved_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book Not Found"
        )

    updated_data = book.model_dump(
        exclude_unset=True
    )
    
    updated_entity = book_repository.patch_book(
        db=db,
        book_entity=saved_entity,
        update_data=updated_data
    )

    return BookResponse.model_validate(updated_entity)

def delete_book(
        db: Session,
        book_id: int
) -> None:
    saved_entity = book_repository.get_book(db, book_id)

    if saved_entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book Not Found"
        )

    book_repository.delete_book(db, saved_entity)
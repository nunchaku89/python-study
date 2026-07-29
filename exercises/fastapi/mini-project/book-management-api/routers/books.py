from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Book
from services import book_service


router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.get("")
def get_books(
    db: Session = Depends(get_db)
):
    return book_service.get_books(db)


@router.get("/{book_id}")
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return book_service.get_book(
        db,
        book_id
    )


@router.post("")
def create_book(
    book: Book,
    db: Session = Depends(get_db)
):
    created_book = book_service.create_book(
        db,
        book
    )

    return {
        "message": "Book Created",
        "book": created_book
    }


@router.put("/{book_id}")
def update_book(
    book_id: int,
    book: Book,
    db: Session = Depends(get_db)
):
    updated_book = book_service.update_book(
        db,
        book_id,
        book
    )

    return {
        "message": "Book Updated",
        "book": updated_book
    }


@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    book_service.delete_book(
        db,
        book_id
    )

    return {
        "message": "Book Deleted"
    }
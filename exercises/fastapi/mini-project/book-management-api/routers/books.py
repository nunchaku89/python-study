from fastapi import APIRouter, HTTPException
from models import Book
from http import HTTPStatus
from services import book_service

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.get("")
def get_books():
    return book_service.get_books()

@router.get("/{book_id}")
def get_book(book_id: int):
    return book_service.get_book(book_id)

@router.post("")
def create_book(book: Book):
    created_book = book_service.create_book(book)

    return {
        "message": "Book Created",
        "book": created_book
    }

@router.put("/{book_id}")
def update_book(book_id: int, book: Book):
    updated_book = book_service.update_book(book_id, book)

    return {
        "message": "Book Updated",
        "book": updated_book
    }

@router.delete("/{book_id}")
def delete_book(book_id: int):
    book_service.delete_book(book_id)

    return {
        "message": "Book Deleted"
    }
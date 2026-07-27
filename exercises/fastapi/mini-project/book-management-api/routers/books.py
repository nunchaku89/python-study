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
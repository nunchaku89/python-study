from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from models import BookCreate, BookUpdate, BookResponse
from services import book_service


router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.get(
        "",
        response_model=list[BookResponse]
)
def get_books(
    db: Session = Depends(get_db)
):
    return book_service.get_books(db)


@router.get(
        "/{book_id}",
        response_model=BookResponse
)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return book_service.get_book(
        db,
        book_id
    )


@router.post(
        "",
        response_model=BookResponse,
        status_code=status.HTTP_201_CREATED
)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    return book_service.create_book(
        db,
        book
    )


@router.put(
        "/{book_id}",
        response_model=BookResponse
)
def update_book(
    book_id: int,
    book: BookUpdate,
    db: Session = Depends(get_db)
):
    return book_service.update_book(
        db,
        book_id,
        book
    )


@router.delete(
        "/{book_id}",
        status_code=status.HTTP_204_NO_CONTENT
)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
) -> None:
    book_service.delete_book(
        db,
        book_id
    )
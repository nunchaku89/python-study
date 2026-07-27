from sqlalchemy import select

from database import SessionLocal
from entities import BookEntity

def get_books() -> list[BookEntity]:
    with SessionLocal() as db:
        statement = select(BookEntity)
        books = db.scalars(statement).all()

        return list(books)

def get_book(book_id: int) -> BookEntity | None:
    with SessionLocal() as db:
        return db.get(BookEntity, book_id)

def create_book(book_entity: BookEntity) -> BookEntity:
    with SessionLocal() as db:
        db.add(book_entity)
        db.commit()
        db.refresh(book_entity)

        return book_entity
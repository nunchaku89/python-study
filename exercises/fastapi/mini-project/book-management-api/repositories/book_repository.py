from sqlalchemy import select

from entities import BookEntity

from sqlalchemy.orm import Session


def get_books(db: Session) -> list[BookEntity]:
    statement = select(BookEntity)
    books = db.scalars(statement).all()

    return list(books)


def get_book(
        db: Session,
        book_id: int
) -> BookEntity | None:
    return db.get(BookEntity, book_id)


def create_book(
        db: Session,
        book_entity: BookEntity
) -> BookEntity:
    db.add(book_entity)
    db.commit()
    db.refresh(book_entity)

    return book_entity


def update_book(
        db: Session,
        book_entity: BookEntity,
        title: str,
        author: str
) -> BookEntity:
    book_entity.title = title
    book_entity.author = author

    db.commit()
    db.refresh(book_entity)

    return book_entity

def patch_book(
        db: Session,
        book_entity: BookEntity,
        update_data: dict[str, str]
) -> BookEntity:
    for field, value in update_data.items():
        setattr(book_entity, field, value)

    db.commit()
    db.refresh(book_entity)

    return book_entity

def delete_book(
        db: Session,
        book_entity: BookEntity
) -> None:
    db.delete(book_entity)
    db.commit()
from fastapi import FastAPI
from models import Book

app = FastAPI()

books = []

@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return {
        "message": "Book Created",
        "book": book
    }

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):

    for book in books:
        if book.id == book_id:
            return book
    
    return {
        "message": "Book Not Found"
    }

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):

    for index, book in enumerate(books):

        if book.id == book_id:
            books[index] = updated_book

            return {
                "message": "Book Updated",
                "book": updated_book
            }
        
    return {
        "message": "Book Not Found"
    }

@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    for book in books:

        if book.id == book_id:

            books.remove(book)

            return {
                "message": "Book Deleted"
            }
        
    return {
        "message": "Book Not Found"
    }
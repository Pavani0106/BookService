from fastapi import APIRouter
from typing import List
from ..Models.book import Book
from ..Schema.book import BookCreate, BookResponse

router = APIRouter(prefix="/books", tags=["books"])

books_db = []

@router.get("/", response_model=List[BookResponse])
def list_books():
    return books_db

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate):
    new_book = Book(**book.dict())
    books_db.append(new_book)
    return new_book

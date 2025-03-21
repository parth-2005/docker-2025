from pydantic import BaseModel, validator
from bson.errors import InvalidId
from bson import ObjectId

class BookCreate(BaseModel):
    title: str
    author: str
    available: bool = True

class Book(BaseModel):
    id: str
    title: str
    author: str
    available: bool

class BorrowRequest(BaseModel):
    book_id: str

    @validator("book_id")
    def validate_book_id(cls, v):
        try:
            ObjectId(v)
            return v
        except InvalidId:
            raise ValueError("Invalid book ID")
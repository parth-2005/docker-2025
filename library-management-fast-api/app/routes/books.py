from fastapi import APIRouter, Depends, HTTPException
from pymongo.collection import Collection
from app.models import Book, BookCreate, BorrowRequest
from app.database import get_books_collection
from bson import ObjectId
from bson.errors import InvalidId

router = APIRouter()

@router.post("/books/", response_model=dict)
def add_book(book: BookCreate, collection: Collection = Depends(get_books_collection)):
    book_dict = book.dict()
    result = collection.insert_one(book_dict)
    return {"message": "Book added", "id": str(result.inserted_id)}

@router.get("/books/", response_model=list[dict])
def get_books(collection: Collection = Depends(get_books_collection)):
    books = []
    for book in collection.find():
        book["_id"] = str(book["_id"])
        books.append(book)
    return books

@router.put("/books/{book_id}", response_model=dict)
def update_book(book_id: str, book: BookCreate, collection: Collection = Depends(get_books_collection)):
    try:
        obj_id = ObjectId(book_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid book ID")
    result = collection.update_one(
        {"_id": obj_id},
        {"$set": book.dict()}
    )
    if result.modified_count == 1:
        return {"message": "Book updated"}
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/books/{book_id}", response_model=dict)
def delete_book(book_id: str, collection: Collection = Depends(get_books_collection)):
    try:
        obj_id = ObjectId(book_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid book ID")
    result = collection.delete_one({"_id": obj_id})
    if result.deleted_count == 1:
        return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

@router.post("/borrow/", response_model=dict)
def borrow_book(request: BorrowRequest, collection: Collection = Depends(get_books_collection)):
    obj_id = ObjectId(request.book_id)
    book = collection.find_one({"_id": obj_id})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    if not book["available"]:
        raise HTTPException(status_code=400, detail="Book not available")
    collection.update_one(
        {"_id": obj_id},
        {"$set": {"available": False}}
    )
    return {"message": "Book borrowed"}

@router.post("/return/", response_model=dict)
def return_book(request: BorrowRequest, collection: Collection = Depends(get_books_collection)):
    obj_id = ObjectId(request.book_id)
    book = collection.find_one({"_id": obj_id})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    if book["available"]:
        raise HTTPException(status_code=400, detail="Book is not borrowed")
    collection.update_one(
        {"_id": obj_id},
        {"$set": {"available": True}}
    )
    return {"message": "Book returned"}
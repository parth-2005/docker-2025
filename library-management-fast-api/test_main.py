import pytest
import httpx
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from bson import ObjectId

# Load environment variables from .env file
load_dotenv()
MONGODB_URL = os.getenv("MONGODB_URL")
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

# Fixture to provide MongoDB connection
@pytest.fixture(scope="module")
def db():
    client = MongoClient(MONGODB_URL)
    db = client.library_db
    yield db
    client.close()

# Fixture to clear the books collection before each test
@pytest.fixture
def clear_books(db):
    db.books.delete_many({})
    yield

# Fixture to provide an HTTP client
@pytest.fixture
def client():
    return httpx.Client(base_url=BASE_URL)

# Test adding a book
def test_add_book(clear_books, client, db):
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "available": True
    }
    response = client.post("/books/", json=book_data)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Book added"
    assert "id" in data
    book_id = data["id"]
    book = db.books.find_one({"_id": ObjectId(book_id)})
    assert book is not None
    assert book["title"] == "Test Book"
    assert book["author"] == "Test Author"
    assert book["available"] is True

# Test retrieving all books
def test_get_books(clear_books, client):
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "available": True
    }
    client.post("/books/", json=book_data)
    response = client.get("/books/")
    assert response.status_code == 200
    books = response.json()
    assert len(books) == 1
    assert books[0]["title"] == "Test Book"
    assert books[0]["author"] == "Test Author"
    assert books[0]["available"] is True
    assert "_id" in books[0]

# Test updating a book
def test_update_book(clear_books, client, db):
    book_data = {
        "title": "Original Title",
        "author": "Original Author",
        "available": True
    }
    response = client.post("/books/", json=book_data)
    book_id = response.json()["id"]
    update_data = {
        "title": "Updated Title",
        "author": "Updated Author",
        "available": False
    }
    response = client.put(f"/books/{book_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Book updated"
    book = db.books.find_one({"_id": ObjectId(book_id)})
    assert book["title"] == "Updated Title"
    assert book["author"] == "Updated Author"
    assert book["available"] is False

# Test deleting a book
def test_delete_book(clear_books, client, db):
    book_data = {
        "title": "To Be Deleted",
        "author": "Author",
        "available": True
    }
    response = client.post("/books/", json=book_data)
    book_id = response.json()["id"]
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted"
    book = db.books.find_one({"_id": ObjectId(book_id)})
    assert book is None

# Test borrowing a book
def test_borrow_book(clear_books, client, db):
    book_data = {
        "title": "Borrowable Book",
        "author": "Author",
        "available": True
    }
    response = client.post("/books/", json=book_data)
    book_id = response.json()["id"]
    borrow_data = {"book_id": book_id}
    response = client.post("/borrow/", json=borrow_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Book borrowed"
    book = db.books.find_one({"_id": ObjectId(book_id)})
    assert book["available"] is False

# Test returning a book
def test_return_book(clear_books, client, db):
    book_data = {
        "title": "Returnable Book",
        "author": "Author",
        "available": True
    }
    response = client.post("/books/", json=book_data)
    book_id = response.json()["id"]
    client.post("/borrow/", json={"book_id": book_id})
    return_data = {"book_id": book_id}
    response = client.post("/return/", json=return_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Book returned"
    book = db.books.find_one({"_id": ObjectId(book_id)})
    assert book["available"] is True

# Test updating a non-existent book
def test_update_nonexistent_book(clear_books, client):
    fake_id = "60af924e5c146f001c8d4e99"  # Assumed non-existent ID
    update_data = {
        "title": "Won't Update",
        "author": "No Author",
        "available": True
    }
    response = client.put(f"/books/{fake_id}", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"

# Test borrowing an unavailable book
def test_borrow_unavailable_book(clear_books, client):
    book_data = {
        "title": "Unavailable Book",
        "author": "Author",
        "available": True
    }
    response = client.post("/books/", json=book_data)
    book_id = response.json()["id"]
    client.post("/borrow/", json={"book_id": book_id})
    response = client.post("/borrow/", json={"book_id": book_id})
    assert response.status_code == 400
    assert response.json()["detail"] == "Book not available"

# Test returning a book that wasn’t borrowed
def test_return_not_borrowed_book(clear_books, client):
    book_data = {
        "title": "Not Borrowed Book",
        "author": "Author",
        "available": True
    }
    response = client.post("/books/", json=book_data)
    book_id = response.json()["id"]
    response = client.post("/return/", json={"book_id": book_id})
    assert response.status_code == 400
    assert response.json()["detail"] == "Book is not borrowed"

# Test using an invalid book ID
def test_invalid_book_id(clear_books, client):
    invalid_id = "invalid_id"
    update_data = {
        "title": "Test",
        "author": "Test Author",
        "available": True
    }
    response = client.put(f"/books/{invalid_id}", json=update_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid book ID"

# Test adding a book with missing fields
def test_add_book_missing_fields(clear_books, client):
    book_data = {"title": "Only Title"}  # Missing author
    response = client.post("/books/", json=book_data)
    assert response.status_code == 422
    assert "detail" in response.json()
# Library Management Server

A simple library management server built with **FastAPI** and **MongoDB Atlas**, containerized using **Docker**. This project provides a RESTful API to manage books in a library, including adding, retrieving, updating, deleting, borrowing, and returning books.

## Features

- **Endpoints**:
  - `POST /books/`: Add a new book.
  - `GET /books/`: Retrieve all books.
  - `PUT /books/{book_id}`: Update a book’s details.
  - `DELETE /books/{book_id}`: Delete a book.
  - `POST /borrow/`: Borrow an available book.
  - `POST /return/`: Return a borrowed book.
- **Database**: MongoDB Atlas for persistent storage.
- **Containerization**: Dockerized for easy deployment.
- **Testing**: Comprehensive test suite using `pytest` and `httpx`.

## Project Structure

```
library-management-fast-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── models.py            # Pydantic models for validation
│   ├── database.py          # MongoDB Atlas connection setup
│   └── routes/
│       ├── __init__.py
│       └── books.py         # API route definitions
├── Dockerfile               # Docker image configuration
├── requirements.txt         # Python dependencies
├── .dockerignore            # Files to exclude from Docker build
├── test_main.py             # Test suite
└── README.md                # Project documentation
```

## Prerequisites

- **Python 3.9+** (for local development/testing)
- **Docker** (for containerization)
- **MongoDB Atlas Account** (for database hosting)
- **Git** (to clone the repository)

## Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd library-management-fast-api
```

### 2. Configure MongoDB Atlas
- Create a MongoDB Atlas cluster.
- Obtain your connection string (e.g., `mongodb+srv://<username>:<password>@cluster0.mongodb.net/`).
- Whitelist your IP address or set to `0.0.0.0/0` (for testing).

### 3. Set Environment Variables
Create a `.env` file in the project root:
```
MONGODB_URL=mongodb+srv://<username>:<password>@cluster0.mongodb.net/library_db?retryWrites=true&w=majority
```
Replace `<username>` and `<password>` with your MongoDB Atlas credentials.

### 4. Install Dependencies (Optional for Local Development)
If running locally without Docker:
```bash
pip install -r requirements.txt
```

## Running the Application

### Using Docker
1. **Build the Docker Image**:
   ```bash
   docker build -t library-management .
   ```
2. **Run the Container**:
   ```bash
   docker run -d -p 8000:8000 --env-file .env library-management
   ```
   - The API will be available at `http://localhost:8000`.

### Locally (Without Docker)
Run the application directly:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Ensure the `.env` file is in the root directory or set `MONGODB_URL` as an environment variable.

## API Usage

### Example Requests

#### Add a Book
```bash
curl -X POST "http://localhost:8000/books/" \
     -H "Content-Type: application/json" \
     -d '{"title": "The Pragmatic Programmer", "author": "Andy Hunt", "available": true}'
```
**Response**: `{"message": "Book added", "id": "60af924e5c146f001c8d4e20"}`

#### Get All Books
```bash
curl "http://localhost:8000/books/"
```
**Response**: Array of books (e.g., `[{"_id": "...", "title": "...", "author": "...", "available": true}]`)

#### Borrow a Book
```bash
curl -X POST "http://localhost:8000/borrow/" \
     -H "Content-Type: application/json" \
     -d '{"book_id": "60af924e5c146f001c8d4e20"}'
```
**Response**: `{"message": "Book borrowed"}`

Explore other endpoints using tools like **Postman** or **curl**.

### API Documentation
- Interactive docs are available at `http://localhost:8000/docs` (Swagger UI) when the server is running.

## Testing

### Prerequisites
Install test dependencies:
```bash
pip install pytest httpx pymongo python-dotenv
```

### Running Tests
1. **Start the Server**:
   ```bash
   docker run -d -p 8000:8000 --env-file .env library-management
   ```
2. **Run Tests**:
   ```bash
   pytest test_main.py -v
   ```
3. **Stop the Server**:
   ```bash
   docker stop $(docker ps -q --filter ancestor=library-management)
   ```

Alternatively, use a script (`run_tests.sh`):
```bash
#!/bin/bash
docker run -d -p 8000:8000 --env-file .env library-management
sleep 5
pytest test_main.py -v
docker stop $(docker ps -q --filter ancestor=library-management)
```
```bash
chmod +x run_tests.sh
./run_tests.sh
```

### Test Coverage
- Tests all endpoints for normal operation and edge cases (e.g., invalid IDs, unavailable books).
- Uses a clean database state for each test via fixtures.

## Troubleshooting

- **MongoDB Connection Issues**: Verify `MONGODB_URL` in `.env` and ensure your IP is whitelisted in MongoDB Atlas.
- **Port Conflicts**: Ensure port 8000 is free or adjust the `-p` flag in `docker run`.
- **Test Failures**: Check server logs (`docker logs <container-id>`) and ensure the `.env` file is correctly loaded.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.
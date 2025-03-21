from fastapi import FastAPI
from app.routes.books import router as books_router
from app.database import client

app = FastAPI()

@app.on_event("shutdown")
def shutdown_db_client():
    client.close()

app.include_router(books_router)
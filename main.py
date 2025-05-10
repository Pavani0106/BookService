from fastapi import FastAPI
from .routers import books

app = FastAPI()

app.include_router(books.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Service"}

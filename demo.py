from fastapi import FastAPI

app = FastAPI()

@app.get("/read-book")
def read_book():
    return {"message": "Hello World"}

Books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
        "genre": "Fiction",
        "rating": 4.5
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_year": 1960,
        "genre": "Fiction",
        "rating": 4.8
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "published_year": 1949,
        "genre": "Dystopian",
        "rating": 4.7
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "published_year": 1813,
        "genre": "Romance",
        "rating": 4.6
    }
]

@app.get("/")
def get_books():
    return Books


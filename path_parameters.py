from fastapi import FastAPI


app=FastAPI()


@app.get("/fetch-user/{dynamic_parameter}")   #fastapi and function should have same path parameters i.e dynamic_parameter as for example
def fetch_user(dynamic_parameter):
    return {"message":f"Fetching user with {dynamic_parameter}"}


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
        "genre": "Romance",
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

@app.get("/books/{book_title}")
def read_book_title(book_title):
    for book in Books:
        if book.get("title").casefold() == book_title.casefold():
            return book


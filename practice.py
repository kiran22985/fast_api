#1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.

from fastapi import FastAPI

app=FastAPI()

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

#http://127.0.0.1:8000/fetch-books/?author=George%20Orwell
#Using Query Parameters
@app.get("/fetch-books/")
def fetch_all_books_query_params(author):
    books_to_return=[]
    for book in Books:
        if book.get("author").casefold()==author.casefold():
            books_to_return.append(book)
    return books_to_return
        


#http://127.0.0.1:8000/fetch-books/George%20Orwell
#Using Path Parameters
@app.get("/fetch-books/{author_name}")
def fetch_all_books_path_params(author_name:str):
    books_to_return=[]
    for book in Books:
        if book.get("author").casefold()==author_name.casefold():
            books_to_return.append(book)
    return books_to_return
    
    
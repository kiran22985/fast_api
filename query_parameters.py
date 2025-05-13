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

# URL: http://127.0.0.1:8000/books/?genre=Fiction&rating=4.7
#query parameters
@app.get("/books/")
def read_book_by_genre(genre: str, rating: float):
    books_for_genre = []
    for book in Books:
        if (book.get("genre").casefold() == genre.casefold()) and (book.get("rating") >= float(rating)):
            books_for_genre.append(book)
    return books_for_genre



#using of both path parameters and query paramaters
# URL http://127.0.0.1:8000/books/George%20Orwell/?genre=Romance
@app.get("/books/{book_author}/")
def read_book_by_author_and_genre(book_author, genre):
    books_to_return=[]
    for book in Books:
        if(book.get("author").casefold()==book_author.casefold() and book.get("genre").casefold()==genre.casefold() ):
            books_to_return.append(book)
    return books_to_return

    
    
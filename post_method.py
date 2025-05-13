from fastapi import Body, FastAPI 

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


#print(Books[0].get("author"))

@app.post("/books/create-book")
def create_book(new_book=Body()):
    return Books.append(new_book)



#Put method to update data 


@app.put("/books/update-book")
def update_book(updated_book=Body()):
    for i in (len(Books)):
        if Books[i].get("title").caseFold()==update_book.get("title").casefold():
             Books[i]=update_book
             return {"message": "Book updated successfully"}

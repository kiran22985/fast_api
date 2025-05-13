from fastapi import FastAPI,Body


app=FastAPI()

class Book:
    id: int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating


Books=[
    Book(1,"Book1","Author1","Description1",5),
    Book(2,"Book2","Author2","Description2",4),
    Book(3,"Book3","Author3","Description3",3),
    Book(4,"Book4","Author4","Description4",2),
    Book(5,"Book5","Author5","Description5",1),
]

@app.get("/fetch-all-books")
def fetch_all_books():
    return Books

@app.get("/fetch-all-books/{book_id}")
def fetch_all_books_by_id(book_id:int):
    for book in Books:
        if book.id==book_id:
            return book
    return {"Error":"Book not found"}


@app.post("/create-book")
def create_book(new_book=Body()):
    Books.append(new_book)
    



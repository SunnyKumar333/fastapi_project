from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from typing import Optional,List
from pydantic import BaseModel
from books import books
from datetime import datetime


app = FastAPI()

class BookCreateModel(BaseModel):
    title: str
    author: str

@app.get("/books",status_code=200,response_model=List[BookCreateModel])
async def get_all_books()-> dict:
    return books

@app.get("/books/{book_id}",response_model=BookCreateModel)
async def greet(book_id:str)->dict:
    book= list(filter(lambda book:book["id"]==book_id,books))
    if len(book)>0:
        return book[0]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Book not found with id: {book_id}")


@app.post("/books",status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookCreateModel):
    books.append({
        "id":str(int(books[-1]["id"])+1),
        "title":book_data.title,
        "author": book_data.author,
        "created_at":datetime.now()
    })

    return {
        "success":True
    }
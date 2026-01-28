import sqlite3
from typing import List
from fastapi import APIRouter,HTTPException,Depends,status
from book_management.models.author import Author,AuthorCreate
from book_management.database import get_db_connection
from book_management.auth.security import get_api_key
from requests import Session

router = APIRouter()

@router.get("/",response_model=List[Author])
def get_authors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id,name FROM authors")
    authors = cursor.fetchall()
    conn.close()
    return [{"id":author[0],"name":author[1]}for author in authors]

@router.post("/",response_model=Author)
def create_author(
        author: AuthorCreate,
        _: str = Depends(get_api_key),
):
   conn = get_db_connection()
   cursor = conn.cursor()
   try:
       cursor.execute("INSERT INTO authors(name) values (?)",(author.name,))
       conn.commit()
       author_id = cursor.lastrowid
       return Author(id=author_id,name=author.name)
   except sqlite3.IntegrityError:
       conn.close()
       raise HTTPException(
           status_code=status.HTTP_409_COnflict,
           detail=f"The author with name '{author.name}' already exists.")

   finally:
       conn.close()

@router.put("/{author_id}",response_model=Author)
def update_author(
        author_id:int,
        author: AuthorCreate,
        _: str = Depends(get_api_key),
):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE authors SET name=? WHERE id=?",
        (author.name, author_id)
    )
    if cursor.rowcount ==0:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with id '{author.name}' not found."
        )
    conn.commit()
    conn.close()
    return Author(id=author_id,name=author.name)

@router.delete("/{author_id}",response_model=dict)
def delete_author(
        author_id: int,
        _: str = Depends(get_api_key),
):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors WHERE id=?",(author_id,))
    if cursor.rowcount ==0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with id '{author.name}' not found."
        )
    conn.commit()
    conn.close()
    return {'detail': 'Author deleted successfully.'}

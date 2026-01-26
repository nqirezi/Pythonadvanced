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
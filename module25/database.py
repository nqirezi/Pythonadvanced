import sqlite3
from models import Movie,MovieCreate

def create_connetion():
    """Create connection to SQlite database."""
    connection = sqlite3.connect("movies.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    """Create the movie table in the database if it doesn't exist."""
    connection = create_connetion()
    cursor = connection.cursor()
    cursor.execute(
        """
          CREATE TABLE IF NOT EXIST movies(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT NOT NULL,
             director TEXT NOT NULL,
                 )
            """
    )
    connection.commit()
    connection.close()

create_table()

def create_movie(movie:MovieCreate) -> int:
    """
    Adds a new movie to the database.

    Args:
        movie( Movie ): A pydantic model containing the title and director of the movie to be created.

    Returns:
        int: The id of the created newly movie in database.


    """

    connection = create_connetion()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO movies(title,director) VALUES (?,?)", (movie.title,movie.director))
    connection.commit()
    movie_id = cursor.lastrowid
    connection.close()
    return movie_id


def read_movies() :
    """
    Reatrives all movies from the database.\
    """
    connection = create_connetion()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    connection.close()
    movies = [Movie(id=row[0],title=row[1],director=row[2]) for row in rows]
    return movies

def read_movie(movie_id:int):
    """

    Retrives a single movie from database by its ID.
    Return:
    Movie:A movie model representing the movie.
    Return None if the movie does not exist.
    """

    connection = create_connetion()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies WHERE id=?",(movie_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return Movie(id=row["id"],title=row["title"],director=row["director"])

def update_movie(movie_id:int,movie:MovieCreate) -> bool:
    """
    Updated an existing movie from the database.
    """
    connection = create_connetion()
    cursor = connection.cursor()
    cursor.execute("Update movies SET title=?,director=? WHERE id = ?",(movie.title,movie.director,movie_id))
    connection.commit()
    updated = cursor.rowcount
    return updated > 0

def delete_movie(movie_id:int):
    connection = create_connetion()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM movies WHERE id=?",(movie_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0




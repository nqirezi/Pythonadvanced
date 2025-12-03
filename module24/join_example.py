import sqlite3
conn= sqlite3.connect("projects.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY ,
    name Text
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
        course_id INTEGER PRIMARY KEY ,
        course_name Text,
        student_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
        ''')

cursor.execute("INSERT INTO (name) VALUES('Alice)")
cursor.execute("INSERT INTO (name) VALUES('Alice)")

cursor.execute("INSERT INTO courses (course_name,student_id ) VALUES ('Math',1)")
cursor.execute("INSERT INTO courses (course_name,student_id ) VALUES ('Art',1)")
cursor.execute("INSERT INTO courses (course_name,student_id ) VALUES ('Science',2)")

conn.commit()

cursor.execute('''
    SELECT students.name, courses.course_name
    FROM students
    JOIN courses ON students.student_id = courses.course_id
''')

rows = cursor.fetchall()
for row in rows:
    print(f"Student; {row[0], Course:{row[1]}}")

conn.close()

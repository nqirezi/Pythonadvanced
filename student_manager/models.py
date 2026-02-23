from database import connect_db


class Task:

    @staticmethod
    def add_task(user_id, title):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks (user_id, title, status) VALUES (?, ?, ?)",
            (user_id, title, "pending")
        )

        conn.commit()
        conn.close()

    @staticmethod
    def get_tasks(user_id):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, title, status FROM tasks WHERE user_id = ?",
            (user_id,)
        )

        tasks = cursor.fetchall()
        conn.close()
        return tasks


class Grade:

    @staticmethod
    def add_grade(user_id, subject, grade):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO grades (user_id, subject, grade) VALUES (?, ?, ?)",
            (user_id, subject, grade)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def get_grades(user_id):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT subject, grade FROM grades WHERE user_id = ?",
            (user_id,)
        )

        grades = cursor.fetchall()
        conn.close()
        return grades

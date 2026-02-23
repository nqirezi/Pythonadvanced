from flask import render_template,Flask, request, jsonify
from database import create_tables, connect_db
import bcrypt
import jwt
import datetime
from functools import wraps
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey123"

create_tables()



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"]

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = data["username"]
        except:
            return jsonify({"error": "Invalid or expired token"}), 401

        return f(current_user, *args, **kwargs)

    return decorated




@app.route("/")
def home():
    return render_template("index.html")



@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed)
        )
        conn.commit()
    except:
        conn.close()
        return jsonify({"error": "User already exists"}), 400

    conn.close()
    return jsonify({"message": "User registered successfully"}), 201




@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode("utf-8"), user["password"]):

        token = jwt.encode({
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config["SECRET_KEY"], algorithm="HS256")

        return jsonify({
            "message": "Login successful",
            "token": token
        })

    return jsonify({"error": "Invalid credentials"}), 401




@app.route("/add-task", methods=["POST"])
@token_required
def add_task(current_user):

    data = request.get_json()
    title = data["title"]

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (current_user,))
    user = cursor.fetchone()

    cursor.execute(
        "INSERT INTO tasks (user_id, title) VALUES (?, ?)",
        (user["id"], title)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Task added"})




@app.route("/tasks", methods=["GET"])
@token_required
def get_tasks(current_user):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (current_user,))
    user = cursor.fetchone()

    cursor.execute("SELECT title, status FROM tasks WHERE user_id = ?", (user["id"],))
    tasks = cursor.fetchall()
    conn.close()

    return jsonify([dict(task) for task in tasks])




@app.route("/add-grade", methods=["POST"])
@token_required
def add_grade(current_user):

    data = request.get_json()
    subject = data["subject"]
    grade = data["grade"]

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (current_user,))
    user = cursor.fetchone()

    cursor.execute(
        "INSERT INTO grades (user_id, subject, grade) VALUES (?, ?, ?)",
        (user["id"], subject, grade)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Grade added"})



@app.route("/grades", methods=["GET"])
@token_required
def get_grades(current_user):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (current_user,))
    user = cursor.fetchone()

    cursor.execute("SELECT subject, grade FROM grades WHERE user_id = ?", (user["id"],))
    grades = cursor.fetchall()
    conn.close()

    total = sum([g["grade"] for g in grades])
    average = total / len(grades) if grades else 0

    return jsonify({
        "grades": [dict(g) for g in grades],
        "average": average
    })



@app.route("/tech-news", methods=["GET"])
@token_required
def tech_news(current_user):

    keyword = request.args.get("search")

    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.select(".titleline a")

    news = []

    for article in articles:
        title = article.text

        if keyword:
            if keyword.lower() not in title.lower():
                continue

        news.append({
            "title": title,
            "link": article.get("href")
        })

    return jsonify(news[:10])


if __name__ == "__main__":
    app.run(debug=True)
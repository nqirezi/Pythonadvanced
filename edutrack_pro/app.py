from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import jwt
import datetime
import os

app = Flask(__name__)
CORS(app)

SECRET_KEY = "supersecretkey"

users = {}
grades_data = {}


@app.route("/")
def home():
    return jsonify({"message": "EduTrack Pro API po funksionon "})


@app.route("/index.html")
def serve_index():
    return send_from_directory(os.getcwd(), "index.html")



@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data["username"]
    password = data["password"]

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = password
    grades_data[username] = []

    token = jwt.encode(
        {"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=5)},
        SECRET_KEY,
        algorithm="HS256"
    )

    return jsonify({"message": "Account created", "token": token})



@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    if username not in users or users[username] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode(
        {"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=5)},
        SECRET_KEY,
        algorithm="HS256"
    )

    return jsonify({"token": token})



@app.route("/add-grade", methods=["POST"])
def add_grade():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"error": "Missing token"}), 401

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = decoded["user"]
    except:
        return jsonify({"error": "Invalid token"}), 401

    data = request.json
    if "grade" not in data or "subject" not in data:
        return jsonify({"error": "Missing data"}), 400

    if not isinstance(data["grade"], (int, float)) or not 0 <= data["grade"] <= 10:
        return jsonify({"error": "Grade must be number 0-10"}), 400

    grades_data[username].append(data)

    return jsonify({"message": "Grade added"})



@app.route("/grades", methods=["GET"])
def get_grades():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"error": "Missing token"}), 401

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = decoded["user"]
    except:
        return jsonify({"error": "Invalid token"}), 401

    user_grades = grades_data.get(username, [])

    if not user_grades:
        return jsonify({
            "grades": [],
            "average": 0,
            "highest": 0,
            "lowest": 0
        })

    values = [g["grade"] for g in user_grades]

    return jsonify({
        "grades": user_grades,
        "average": round(sum(values)/len(values),2),
        "highest": max(values),
        "lowest": min(values)
    })


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    host="postgres.dev.svc.cluster.local",
    database="mydb",
    user="myuser",
    password="mypassword"
)

@app.route("/api/people", methods=["GET"])
def get_people():
    cur = conn.cursor()
    cur.execute("SELECT name, age FROM people;")
    rows = cur.fetchall()
    cur.close()

    people = [{"name": r[0], "age": r[1]} for r in rows]
    return jsonify(people)


@app.route("/api/people", methods=["POST"])
def add_person():
    data = request.json
    name = data["name"]
    age = data["age"]

    cur = conn.cursor()
    cur.execute("INSERT INTO people (name, age) VALUES (%s, %s);", (name, age))
    conn.commit()
    cur.close()

    return jsonify({"message": "Person added"}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

DB_HOST = "postgres"
DB_NAME = "mydb"
DB_USER = "myuser"
DB_PASSWORD = "mypassword"

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/api/people", methods=["GET"])
def get_people():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, age FROM people;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    people = [{"name": r[0], "age": r[1]} for r in rows]
    return jsonify(people)

@app.route("/api/people", methods=["POST"])
def add_people():
    data = request.json
    name = data["name"]
    age = data["age"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO people (name, age) VALUES (%s, %s);", (name, age))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Person added"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

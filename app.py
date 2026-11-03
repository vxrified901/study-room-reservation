
from flask import Flask
import sqlite3

app = Flask(__name__)

DATABASE = "rooms.db"


def initialize_database():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                capacity INTEGER NOT NULL
            )
        """)

        count = connection.execute(
            "SELECT COUNT(*) FROM rooms"
        ).fetchone()[0]

        if count == 0:
            connection.executemany(
                "INSERT INTO rooms (name, capacity) VALUES (?, ?)",
                [
                    ("Library Room 101", 4),
                    ("Library Room 102", 6),
                    ("Engineering Room 201", 8)
                ]
            )


@app.route("/")
def view_rooms():
    with sqlite3.connect(DATABASE) as connection:
        rooms = connection.execute(
            "SELECT name, capacity FROM rooms"
        ).fetchall()

    html = "<h1>Campus Study Room Reservation System</h1>"
    html += "<h2>Available Study Rooms</h2>"

    for name, capacity in rooms:
        html += f"<p>{name} - Capacity: {capacity}</p>"

    return html


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)

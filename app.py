
from flask import Flask, g, request, has_request_context
import sqlite3
import json
import logging
import uuid
from datetime import datetime, timezone

app = Flask(__name__)
DATABASE = "rooms.db"

logger = logging.getLogger("study_room_app")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)

logger.propagate = False


def log_event(event, level="INFO", **details):
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "event": event,
        "request_id": (
            getattr(g, "request_id", None)
            if has_request_context() else None
        ),
        **details,
    }

    message = json.dumps(record)

    if level == "ERROR":
        logger.error(message)
    else:
        logger.info(message)


@app.before_request
def start_request():
    g.request_id = uuid.uuid4().hex
    log_event("request_started", path=request.path)


@app.after_request
def finish_request(response):
    log_event(
        "request_completed",
        path=request.path,
        status=response.status_code,
    )
    return response


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
                    ("Engineering Room 201", 8),
                ],
            )


def get_rooms():
    try:
        with sqlite3.connect(DATABASE) as connection:
            rooms = connection.execute(
                "SELECT name, capacity FROM rooms"
            ).fetchall()

        log_event("rooms_loaded", room_count=len(rooms))
        return rooms

    except sqlite3.Error as error:
        log_event(
            "database_error",
            level="ERROR",
            error_type=type(error).__name__,
        )
        raise


@app.route("/")
def view_rooms():
    rooms = get_rooms()

    html = "<h1>Campus Study Room Reservation System</h1>"
    html += "<h2>Available Study Rooms</h2>"

    for name, capacity in rooms:
        html += f"<p>{name} - Capacity: {capacity}</p>"

    return html


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)

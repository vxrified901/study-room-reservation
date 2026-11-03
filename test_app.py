
import sqlite3

import app


def test_view_rooms_reads_database(tmp_path, monkeypatch):
    database = tmp_path / "test_rooms.db"
    monkeypatch.setattr(app, "DATABASE", str(database))

    app.initialize_database()

    with sqlite3.connect(database) as connection:
        connection.execute(
            "UPDATE rooms SET capacity = 10 WHERE name = ?",
            ("Library Room 101",)
        )
        connection.commit()

    client = app.app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Library Room 101" in response.data
    assert b"Capacity: 10" in response.data
    assert b"Capacity: 4" not in response.data


def test_database_creates_default_rooms(tmp_path, monkeypatch):
    database = tmp_path / "test_rooms.db"
    monkeypatch.setattr(app, "DATABASE", str(database))

    app.initialize_database()

    with sqlite3.connect(database) as connection:
        rooms = connection.execute(
            "SELECT name, capacity FROM rooms ORDER BY id"
        ).fetchall()

    assert rooms == [
        ("Library Room 101", 4),
        ("Library Room 102", 6),
        ("Engineering Room 201", 8),
    ]


def test_database_initialization_preserves_changes(tmp_path, monkeypatch):
    database = tmp_path / "test_rooms.db"
    monkeypatch.setattr(app, "DATABASE", str(database))

    app.initialize_database()

    with sqlite3.connect(database) as connection:
        connection.execute(
            "UPDATE rooms SET capacity = 10 WHERE name = ?",
            ("Library Room 101",)
        )

    app.initialize_database()

    with sqlite3.connect(database) as connection:
        rooms = connection.execute(
            "SELECT capacity FROM rooms WHERE name = ?",
            ("Library Room 101",)
        ).fetchall()

        count = connection.execute(
            "SELECT COUNT(*) FROM rooms"
        ).fetchone()[0]

    assert rooms == [(10,)]
    assert count == 3


def test_view_rooms_shows_empty_database(tmp_path, monkeypatch):
    database = tmp_path / "empty_rooms.db"
    monkeypatch.setattr(app, "DATABASE", str(database))

    app.initialize_database()

    with sqlite3.connect(database) as connection:
        connection.execute("DELETE FROM rooms")

    response = app.app.test_client().get("/")

    assert response.status_code == 200
    assert b"Available Study Rooms" in response.data
    assert b"Library Room 101" not in response.data
    assert b"Capacity:" not in response.data

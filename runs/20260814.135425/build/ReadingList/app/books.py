"""Application-facing helpers for reading-list book records."""

from __future__ import annotations

from flask import Flask

from app.database import Database


def _database(app: Flask) -> Database:
    return app.extensions["reading_list_database"]


def list_books(app: Flask) -> list[dict[str, int | str | bool]]:
    """Return persisted books in insertion order as application records."""
    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "is_read": book.is_read,
        }
        for book in _database(app).list_books()
    ]

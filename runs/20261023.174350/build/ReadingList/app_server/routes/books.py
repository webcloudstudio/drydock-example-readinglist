"""Book routes: parse HTTP input, call the book service, and shape the HTTP response."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from flask import Blueprint, current_app, jsonify, request

from app_server.services import books as book_service

books = Blueprint("books", __name__)


@books.post("/books")
def post_book() -> tuple[Any, int]:
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        payload = {}
    db = current_app.extensions["db"]
    try:
        book = book_service.add_book(db, payload.get("title"), payload.get("author"))
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    return jsonify(asdict(book)), 201


@books.get("/books")
def get_books() -> tuple[Any, int]:
    db = current_app.extensions["db"]
    return jsonify([asdict(book) for book in book_service.list_books(db)]), 200


@books.delete("/books/<int:book_id>")
def delete_book(book_id: int) -> tuple[Any, int]:
    db = current_app.extensions["db"]
    if not book_service.remove_book(db, book_id):
        return jsonify({"error": f"no book with id {book_id}"}), 404
    return "", 204

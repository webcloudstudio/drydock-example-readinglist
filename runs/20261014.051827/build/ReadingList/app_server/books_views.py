"""HTTP surface for the book list. Thin: parse the request, call the service, shape the response."""

from flask import Blueprint, current_app, jsonify, request

from app_server.books_service import InvalidBook, add_book, list_books, remove_book
from app_server.settings import DATABASE_EXTENSION

__all__ = ["bp"]

bp = Blueprint("books", __name__)


@bp.get("/books")
def read_books():
    database = current_app.extensions[DATABASE_EXTENSION]
    books = list_books(database)
    return jsonify([{"id": book.id, "title": book.title, "author": book.author} for book in books]), 200


@bp.delete("/books/<int:book_id>")
def delete_book(book_id: int):
    database = current_app.extensions[DATABASE_EXTENSION]
    if not remove_book(database, book_id):
        return jsonify(id=book_id), 404
    return "", 204


@bp.post("/books")
def create_book():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        payload = {}
    database = current_app.extensions[DATABASE_EXTENSION]
    try:
        book = add_book(database, payload.get("title"), payload.get("author"))
    except InvalidBook as exc:
        return jsonify(field=exc.field), 400
    return jsonify(id=book.id, title=book.title, author=book.author), 201

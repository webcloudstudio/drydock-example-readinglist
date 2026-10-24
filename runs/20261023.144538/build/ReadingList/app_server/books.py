"""HTTP routes for books: the reading list page, add a book, list stored books in the order added, and remove a book."""

from __future__ import annotations

from flask import Blueprint, abort, current_app, jsonify, redirect, render_template, request
from werkzeug.wrappers import Response

from persistence import Database

from .book_service import BookNotFound, BookRejected, add_book, list_books, remove_book

bp = Blueprint("books", __name__)


def _database() -> Database:
    return current_app.extensions["database"]


def _reading_list(error: str | None = None) -> str:
    """Render the reading list page: the alert region, the add form, and the books in the order added."""
    return render_template("reading_list.html", books=list_books(_database()), error=error)


@bp.get("/")
def index() -> str:
    """Render the reading list page with every stored book in the order added."""
    return _reading_list()


@bp.get("/books")
def get_books() -> Response:
    """Return every stored book as a JSON array of ``id``, ``title`` and ``author``, oldest first."""
    return jsonify(
        [{"id": row.id, "title": row.title, "author": row.author} for row in list_books(_database())]
    )


@bp.post("/books")
def create_book() -> Response:
    """Add a book from the ``title`` and ``author`` form fields, then redirect to the start page.

    A refused submission answers 400: as JSON with ``error`` and ``field`` when the client asks
    for ``application/json``, otherwise as the reading list page with the reason in the alert region.
    """
    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()
    try:
        add_book(_database(), title=title, author=author)
    except BookRejected as rejected:
        if request.accept_mimetypes.best == "application/json":
            refused = jsonify(error=rejected.reason, field=rejected.field)
            refused.status_code = 400
            return refused
        return Response(
            _reading_list(error=rejected.reason),
            status=400,
            mimetype="text/html",
        )
    return redirect("/", code=303)


@bp.post("/books/<int:book_id>/delete")
def delete_book(book_id: int) -> Response:
    """Remove the book with ``book_id``, then redirect to the start page; an unknown id answers 404."""
    try:
        remove_book(_database(), book_id)
    except BookNotFound:
        abort(404)
    return redirect("/", code=303)

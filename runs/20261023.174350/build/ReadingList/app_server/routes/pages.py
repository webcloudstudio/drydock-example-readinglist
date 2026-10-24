"""Application-level routes: the health check and the reading list page.

Each handler parses form or HTTP input, calls the book service, and shapes the response.
"""

from __future__ import annotations

from flask import Blueprint, Response, current_app, jsonify, redirect, render_template, request, url_for

from app_server.services import books as book_service

pages = Blueprint("pages", __name__)


@pages.get("/health")
def health() -> tuple[Response, int]:
    return jsonify({"status": "ok"}), 200


@pages.get("/")
def index() -> tuple[str, int]:
    return _render_reading_list(), 200


@pages.post("/add")
def add() -> tuple[str, int] | Response:
    db = current_app.extensions["db"]
    title = request.form.get("title")
    author = request.form.get("author")
    try:
        book_service.add_book(db, title, author)
    except ValueError as error:
        return _render_reading_list(error=str(error), title=title, author=author), 400
    return redirect(url_for("pages.index"), code=303)


@pages.post("/remove/<int:book_id>")
def remove(book_id: int) -> Response:
    book_service.remove_book(current_app.extensions["db"], book_id)
    return redirect(url_for("pages.index"), code=303)


def _render_reading_list(
    error: str | None = None, title: str | None = None, author: str | None = None
) -> str:
    """Render the page with every book in the order added; echo rejected form values back."""
    books = book_service.list_books(current_app.extensions["db"])
    return render_template(
        "reading_list.html",
        books=books,
        error=error,
        title=title or "",
        author=author or "",
    )

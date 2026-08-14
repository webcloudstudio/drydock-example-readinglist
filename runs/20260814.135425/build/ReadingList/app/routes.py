"""HTTP routes for the ReadingList entry point."""

from __future__ import annotations

from flask import Blueprint, Response, current_app, redirect, render_template, request, url_for

from app.database import Book, Database

main_blueprint = Blueprint("main", __name__)


def _database() -> Database:
    return current_app.extensions["reading_list_database"]


@main_blueprint.get("/")
def reading_list() -> str:
    """Render the current reading list."""
    books: list[Book] = _database().list_books()
    return render_template("reading_list.html", books=books)


@main_blueprint.post("/books")
def add_book() -> Response | tuple[str, int]:
    """Validate and add a book, then return to the ordered reading list."""
    title = request.form.get("title", "")
    author = request.form.get("author", "")

    if not isinstance(title, str) or not title.strip():
        return _invalid_book_response("A book title is required.")
    if not isinstance(author, str) or not author.strip():
        return _invalid_book_response("A book author is required.")

    _database().create_book(title, author)
    return redirect(url_for("main.reading_list"), code=303)


@main_blueprint.post("/books/<int:book_id>/delete")
def delete_book(book_id: int) -> Response:
    """Delete the selected book, then return to the ordered reading list."""
    _database().delete_book(book_id)
    return redirect(url_for("main.reading_list"), code=303)


@main_blueprint.post("/books/<int:book_id>/read")
def mark_book_read(book_id: int) -> Response:
    """Mark the selected book as read, then return to the reading list."""
    _database().mark_book_read(book_id)
    return redirect(url_for("main.reading_list"), code=303)


def _invalid_book_response(error: str) -> tuple[str, int]:
    """Render the list with a validation error without writing a book."""
    books: list[Book] = _database().list_books()
    return render_template(
        "reading_list.html",
        books=books,
        error=error,
        title=request.form.get("title", ""),
        author=request.form.get("author", ""),
    ), 400

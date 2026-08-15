"""HTTP routes for the ReadingList application."""

from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from app.persistence import BookStore, get_book_store

bp = Blueprint("reading_list", __name__)


def _store() -> BookStore:
    return get_book_store()


@bp.get("/")
def index():
    return render_template("index.html", books=_store().list_ordered(), error=None)


@bp.post("/books")
def add_book():
    """Add a book, returning to the list or showing the invalid fields."""
    title = request.form.get("title", "")
    author = request.form.get("author", "")
    missing = [
        field
        for field, value in (("title", title), ("author", author))
        if not value.strip()
    ]
    if missing:
        fields = " and ".join(missing)
        message = f"Please provide a {fields}."
        return (
            render_template(
                "index.html", books=_store().list_ordered(), error=message
            ),
            400,
        )

    _store().add(title, author)
    return redirect(url_for("reading_list.index"))


@bp.post("/books/<int:book_id>/remove")
def remove_book(book_id: int):
    """Remove one book identified by its stable database id."""
    _store().remove(book_id)
    return redirect(url_for("reading_list.index"))


@bp.post("/books/<int:book_id>/mark-read")
@bp.post("/books/<int:book_id>/read")
def mark_read(book_id: int):
    """Mark one book as read and return to the reading list."""
    _store().mark_read(book_id)
    return redirect(url_for("reading_list.index"))


@bp.get("/health")
def health():
    _store().list_ordered()
    return jsonify(status="ok")

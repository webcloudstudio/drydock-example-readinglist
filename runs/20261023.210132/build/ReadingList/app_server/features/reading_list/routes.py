"""Server-rendered HTTP boundary for the reading-list feature."""

from flask import Response, current_app, redirect, render_template, request, url_for

from app_server.features.reading_list import reading_list
from persistence import open_database
from persistence.schema import BookRow


def _database():
    dsn = current_app.config.get("DATABASE_URL") or current_app.config["DATABASE_PATH"]
    return open_database(str(dsn))


def _next_insertion_order(books: list[BookRow]) -> int:
    return max((book.insertion_order for book in books), default=0) + 1


def _read_books() -> list[BookRow]:
    database = _database()
    try:
        return sorted(database.books.list(), key=lambda book: book.insertion_order)
    finally:
        database.close()


@reading_list.get("/")
def index() -> str:
    books = _read_books()
    return render_template("reading_list/index.html", books=books, errors={}, form={})


@reading_list.post("/books")
def add_book() -> Response | str:
    form = {"title": request.form.get("title", ""), "author": request.form.get("author", "")}
    errors = {field: f"{field.title()} is required." for field, value in form.items() if not value.strip()}
    if errors:
        books = _read_books()
        return render_template("reading_list/index.html", books=books, errors=errors, form=form), 400

    database = _database()
    try:
        books = database.books.list()
        database.books.create(title=form["title"].strip(), author=form["author"].strip(), insertion_order=_next_insertion_order(books))
    finally:
        database.close()
    return redirect(url_for("reading_list.index"))


@reading_list.post("/books/<int:book_id>/delete")
def delete_book(book_id: int) -> Response:
    database = _database()
    try:
        database.books.delete(id=book_id)
    finally:
        database.close()
    return redirect(url_for("reading_list.index"))

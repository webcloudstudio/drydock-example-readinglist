from __future__ import annotations

from typing import Any

from flask import Flask, jsonify, redirect, render_template, request, url_for

from validation import validate_book


def register_routes(app: Flask) -> None:
    def add_book_from_form() -> Any:
        title = request.form.get("title", "")
        author = request.form.get("author", "")
        errors = validate_book(title, author)
        store = app.extensions["book_store"]
        if errors:
            return render_template(
                "books.html",
                books=store.list(),
                errors=errors,
                form={"title": title, "author": author},
            ), 400
        store.add(title.strip(), author.strip())
        return redirect(url_for("books"))

    @app.route("/", methods=["GET", "POST"])
    def books() -> Any:
        if request.method == "POST":
            return add_book_from_form()
        store = app.extensions["book_store"]
        return render_template("books.html", books=store.list(), errors={}, form={})

    @app.get("/books")
    def list_books() -> Any:
        return jsonify(app.extensions["book_store"].list())

    @app.post("/books")
    def add_book() -> Any:
        return add_book_from_form()

    @app.post("/books/<int:book_id>/remove")
    def remove_book(book_id: int) -> Any:
        if not app.extensions["book_store"].remove(book_id):
            return jsonify({"error": "Book not found"}), 404
        return redirect(url_for("books"))

    @app.post("/books/<int:book_id>/read")
    def mark_book_read(book_id: int) -> Any:
        if not app.extensions["book_store"].mark_read(book_id):
            return jsonify({"error": "Book not found"}), 404
        return redirect(url_for("books"))

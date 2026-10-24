"""HTML surface for the reading list page. Thin: render the page; the page calls the book routes itself."""

from flask import Blueprint, render_template

__all__ = ["bp"]

bp = Blueprint("pages", __name__)


@bp.get("/")
def reading_list():
    return render_template("reading_list.html")

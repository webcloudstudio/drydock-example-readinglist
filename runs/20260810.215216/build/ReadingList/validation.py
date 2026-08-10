from __future__ import annotations


def validate_book(title: str, author: str) -> dict[str, str]:
    errors: dict[str, str] = {}
    if not title.strip():
        errors["title"] = "Title is required."
    if not author.strip():
        errors["author"] = "Author is required."
    return errors

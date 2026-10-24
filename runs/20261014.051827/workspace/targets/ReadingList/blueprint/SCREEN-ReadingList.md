# SCREEN: Reading List

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | The reading list page where a reader adds, views, and removes books. |
| Depends On  | FEATURE-AddBook.md, FEATURE-ListBooks.md, FEATURE-RemoveBook.md |
| Provides    | GET / |
| Consumes    | POST /books, GET /books, DELETE /books/{id} |
| Route       | / |
| Parent      | — |
| Main Menu   | Reading List (1) |
| Sub Menu    | — |
| Tab Order   | — |

## Purpose

The single page of the application. A reader submits a title and author, sees the ordered list, and removes a book.

## Layout

- A form with a title field and an author field, and a submit control.
- An ordered list of books, in the order returned by `GET /books`.
- A remove control beside each book.
- Validation errors from a rejected submission are shown beside the form, naming the failing field.

## Interactions

- Submitting the form calls `POST /books`. On status 201 the list is reloaded. On status 400 the error for the field named in the response is shown.
- The page loads the list by calling `GET /books`.
- Activating a remove control calls `DELETE /books/{id}` for that book. On status 204 the list is reloaded.

## Database Interface

- None — persistence is owned by FEATURE-AddBook.md, FEATURE-ListBooks.md, and FEATURE-RemoveBook.md.

## Programmatic Acceptance

=== AC screen-get-root ===
Intent: GET / returns status 200 with an HTML page.

from app_server.testing import web_client

client = web_client()
response = client.get("/")
assert response.status_code == 200
assert response.mimetype == "text/html"
=== END AC screen-get-root ===

=== AC screen-add-list-remove ===
Intent: The routes the page calls add, list, and remove a book, and an unknown id returns 404.

import uuid
from app_server.testing import web_client

client = web_client()
title = uuid.uuid4().hex
author = uuid.uuid4().hex
added = client.post("/books", json={"title": title, "author": author})
assert added.status_code == 201
book_id = added.get_json()["id"]
listing = client.get("/books")
assert listing.status_code == 200
assert book_id in [book["id"] for book in listing.get_json()]
removed = client.delete(f"/books/{book_id}")
assert removed.status_code == 204
assert client.delete("/books/999999999").status_code == 404
=== END AC screen-add-list-remove ===

## User Acceptance

- None.

## Guardrails

- The page must not present a book in an order other than the order returned by `GET /books`.
- The page must not offer a submit control that sends an empty title or author.

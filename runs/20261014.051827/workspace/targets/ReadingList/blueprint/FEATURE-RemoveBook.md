# FEATURE: Remove Book

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Remove a book so it is omitted from the next read; report a missing id without altering the list. |
| Depends On  | ARCHITECTURE.md, DATABASE.md, FEATURE-AddBook.md, FEATURE-ListBooks.md |
| Provides    | DELETE /books/{id} |
| Consumes    | books.get, books.delete |

## Purpose

A reader removes a book from the list.

## Route

`DELETE /books/{id}`

- A stored id is removed through `books.delete` and returns status 204.
- An id that is not in the list returns status 404 and leaves the list unchanged.
- A removed book is absent from the next `GET /books`.

## Database Interface

- `FEATURE-BOOKS-003` — read: retrieve a book by id - supplies: `id` - returns: `id`, `title`, `author`
- `FEATURE-BOOKS-004` — write: delete a book by id - supplies: `id` - returns: `id`

## Programmatic Acceptance

=== AC remove-book-deletes ===
Intent: A removed book returns status 204 and is absent from the next list read.

import uuid
from app_server.testing import web_client

author = uuid.uuid4().hex
client = web_client()
added = client.post("/books", json={"title": uuid.uuid4().hex, "author": author})
assert added.status_code == 201
book_id = added.get_json()["id"]
deleted = client.delete(f"/books/{book_id}")
assert deleted.status_code == 204
listing = client.get("/books")
assert listing.status_code == 200
assert book_id not in [book["id"] for book in listing.get_json()]
=== END AC remove-book-deletes ===

=== AC remove-book-missing-id ===
Intent: Removing an id that is not in the list returns 404 and leaves the list unchanged.

import uuid
from app_server.testing import web_client

author = uuid.uuid4().hex
client = web_client()
added = client.post("/books", json={"title": uuid.uuid4().hex, "author": author})
assert added.status_code == 201
book_id = added.get_json()["id"]
assert client.delete(f"/books/{book_id}").status_code == 204
before = [book["id"] for book in client.get("/books").get_json()]
repeated = client.delete(f"/books/{book_id}")
assert repeated.status_code == 404
after = [book["id"] for book in client.get("/books").get_json()]
assert after == before
=== END AC remove-book-missing-id ===

## User Acceptance

- None.

## Guardrails

- Removing a missing id must not alter the list.

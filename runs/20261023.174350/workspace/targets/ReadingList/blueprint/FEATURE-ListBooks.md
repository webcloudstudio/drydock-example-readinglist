# FEATURE: List Books

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | Return all books in the order they were added. |
| Depends On | FEATURE-AddBook.md, DATABASE.md |
| Provides | GET /books |
| Consumes | books.list |

## Purpose

Let the reader view the books. Books are never presented in any order other than the order added.

## Trigger

A client sends `GET /books`.

## Sequence

1. The route calls `app_server.services.books.list_books(db)`.
2. The service calls `books.list`, which returns rows by id ascending.
3. The route returns 200 with a JSON array of `{"id", "title", "author"}` in that order.

## Routes

| Route | Behavior |
|-------|----------|
| `GET /books` | Returns 200 with a JSON array ordered by insertion. An empty list returns `[]`. |

## Reads

`books.list` returns every stored book ordered by id ascending.

## Writes

None.

## Database Interface


- `FEATURE-BOOK-003` — read: books.list - supplies: — - returns: `id`, `title`, `author`

## Tests

The build writes pytest tests that add several books and assert the returned order equals the order submitted, plus the empty-list case.

## Programmatic Acceptance

=== AC listbooks-order ===
Intent: GET /books returns the books added during the check in the order they were added.
Requires: python-package=flask; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

client = web_client()
titles = ["ac-listbooks-order-first", "ac-listbooks-order-second", "ac-listbooks-order-third"]
created = []
try:
    for title in titles:
        response = client.post("/books", json={"title": title, "author": "ac-listbooks-author"})
        assert response.status_code == 201
        created.append(response.get_json()["id"])
    listing = client.get("/books")
    assert listing.status_code == 200
    body = listing.get_json()
    assert isinstance(body, list)
    mine = [book["id"] for book in body if book["id"] in created]
    assert mine == created
finally:
    with committed_session() as db:
        for book_id in created:
            db.books.delete(id=book_id)
=== END AC listbooks-order ===

=== AC listbooks-fields ===
Intent: Each listed book carries the supplied title and author and its id.
Requires: python-package=flask; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

title = "ac-listbooks-fields-title"
author = "ac-listbooks-fields-author"
client = web_client()
created_id = None
try:
    response = client.post("/books", json={"title": title, "author": author})
    assert response.status_code == 201
    created_id = response.get_json()["id"]
    body = client.get("/books").get_json()
    matches = [book for book in body if book["id"] == created_id]
    assert len(matches) == 1
    assert matches[0]["title"] == title
    assert matches[0]["author"] == author
finally:
    if created_id is not None:
        with committed_session() as db:
            db.books.delete(id=created_id)
=== END AC listbooks-fields ===

=== AC listbooks-reachable ===
Intent: GET /books is reachable and returns a JSON array even when no check data exists.
Requires: python-package=flask; scope=test

from app_server.testing import web_client

response = web_client().get("/books")
assert response.status_code == 200
assert isinstance(response.get_json(), list)
=== END AC listbooks-reachable ===

## User Acceptance

- None.

## Guardrails

- Never present books in any order other than the order they were added.
- The route never reads the database directly; it calls the book service.

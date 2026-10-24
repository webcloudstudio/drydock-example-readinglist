# FEATURE: List Books

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Return stored books in the order they were added. |
| Depends On  | ARCHITECTURE.md, DATABASE.md, FEATURE-AddBook.md |
| Provides    | GET /books |
| Consumes    | books.list |

## Purpose

A reader views the books in the order they were added.

## Route

`GET /books` returns status 200 with a JSON array of books, each with `id`, `title`, and `author`. The array is ordered by ascending `id`, which is insertion order.

## Database Interface


- `FEATURE-BOOKS-002` — read: books.list - supplies: `(none)` - returns: `id`, `title`, `author`

## Programmatic Acceptance

=== AC list-books-returns-ok ===
Intent: GET /books returns status 200 with a JSON array.

from app_server.testing import web_client

client = web_client()
response = client.get("/books")
assert response.status_code == 200
assert isinstance(response.get_json(), list)
=== END AC list-books-returns-ok ===

=== AC list-books-insertion-order ===
Intent: Books added in sequence are listed in the order they were added.

import uuid
from app_server.testing import web_client

author = uuid.uuid4().hex
first = uuid.uuid4().hex
second = uuid.uuid4().hex
third = uuid.uuid4().hex
client = web_client()
for title in (first, second, third):
    added = client.post("/books", json={"title": title, "author": author})
    assert added.status_code == 201
listing = client.get("/books")
assert listing.status_code == 200
titles = [book["title"] for book in listing.get_json() if book["title"] in (first, second, third)]
assert titles == [first, second, third]
=== END AC list-books-insertion-order ===

## User Acceptance

- None.

## Guardrails

- Never present books in an order other than the order they were added.

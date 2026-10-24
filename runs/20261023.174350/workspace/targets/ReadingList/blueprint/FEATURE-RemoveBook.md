# FEATURE: Remove Book

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | Remove a book from the reading list so it never reappears in later reads. |
| Depends On | FEATURE-AddBook.md, FEATURE-ListBooks.md, DATABASE.md |
| Provides | DELETE /books/{book_id} |
| Consumes | books.delete, books.get, GET /books |

## Purpose

A reader removes a book they no longer want on their list. Once removed, the book must be absent from every subsequent list read, and the remaining books keep the order in which they were added.

## Trigger

An HTTP `DELETE /books/{book_id}` request, where `book_id` is the integer id returned when the book was added.

## Sequence

1. The route parses `book_id` as an integer. A non-integer id does not match the route and is answered by the framework as an unknown resource (404).
2. The service looks the book up through `books.get`. If it does not exist, the route answers 404 with a JSON error body.
3. The service removes the book through `books.delete`.
4. The route answers 204 with an empty body.

## Routes

| Route | Method | Success | Failure |
|-------|--------|---------|---------|
| `/books/{book_id}` | DELETE | 204, empty body | 404 for an unknown id, including a repeat removal of the same id |

## Reads

- `books.get` — confirms the book exists before deletion.

## Writes

- `books.delete` — permanently removes the book row.

## Database Interface

- `FEATURE-BOOK-004` — write: remove a book - supplies: `id` - returns: `id`
- `FEATURE-BOOK-002` — read: get a book by id - supplies: `id` - returns: `id`

## Operational Behavior

- Removal never alters the ids or relative order of the remaining books.
- A removed book must not reappear in any later read, including after the application restarts.
- Removing an already removed id is a no-op on state and answers 404.

## Programmatic Acceptance

=== AC remove-book-deletes ===
Intent: Removing an added book answers 204 and the book is absent from the next list read.
Suite: scoped

import uuid
from app_server.testing import web_client

client = web_client()
title = "ac-remove-" + uuid.uuid4().hex
author = "ac-remove-author"
created = client.post("/books", json={"title": title, "author": author})
assert created.status_code == 201
book_id = created.get_json()["id"]
try:
    before = [b["id"] for b in client.get("/books").get_json()]
    assert book_id in before
    removed = client.delete(f"/books/{book_id}")
    assert removed.status_code == 204
    after = [b["id"] for b in client.get("/books").get_json()]
    assert book_id not in after
finally:
    client.delete(f"/books/{book_id}")
=== END AC remove-book-deletes ===

=== AC remove-book-unknown-id ===
Intent: Removing an id that does not exist answers 404, and removing the same id twice answers 404 the second time.
Suite: scoped

import uuid
from app_server.testing import web_client

client = web_client()
title = "ac-remove-twice-" + uuid.uuid4().hex
created = client.post("/books", json={"title": title, "author": "ac-remove-author"})
assert created.status_code == 201
book_id = created.get_json()["id"]
try:
    first = client.delete(f"/books/{book_id}")
    assert first.status_code == 204
    second = client.delete(f"/books/{book_id}")
    assert second.status_code == 404
    existing = [b["id"] for b in client.get("/books").get_json()]
    unknown_id = max(existing + [book_id]) + 1000000
    unknown = client.delete(f"/books/{unknown_id}")
    assert unknown.status_code == 404
finally:
    client.delete(f"/books/{book_id}")
=== END AC remove-book-unknown-id ===

=== AC remove-book-preserves-order ===
Intent: Removing the middle book leaves the other books in the order they were added.
Suite: scoped

import uuid
from app_server.testing import web_client

client = web_client()
token = uuid.uuid4().hex
ids = []
try:
    for n in range(3):
        resp = client.post("/books", json={"title": f"ac-order-{token}-{n}", "author": "ac-remove-author"})
        assert resp.status_code == 201
        ids.append(resp.get_json()["id"])
    removed = client.delete(f"/books/{ids[1]}")
    assert removed.status_code == 204
    listed = [b["id"] for b in client.get("/books").get_json()]
    mine = [i for i in listed if i in ids]
    assert mine == [ids[0], ids[2]]
finally:
    for book_id in ids:
        client.delete(f"/books/{book_id}")
=== END AC remove-book-preserves-order ===

## User Acceptance

- None.

## Guardrails

- A removed book must never reappear in a later list read.
- Removal must not change the relative order of the remaining books.
- A request for an unknown id must not alter stored state.

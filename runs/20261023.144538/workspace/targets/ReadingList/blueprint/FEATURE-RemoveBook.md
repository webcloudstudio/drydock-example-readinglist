# FEATURE: Remove Book

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | A reader removes a book so it no longer appears in the list. |
| Depends On | ARCHITECTURE.md, DATABASE.md, FEATURE-AddBook.md |
| Provides | POST /books/{id}/delete |
| Consumes | books.get, books.delete |

## Purpose

Let a reader remove a book from the reading list.

## Trigger

A form post to `POST /books/{id}/delete`.

## Sequence

1. Look up the book with `db.books.get(id=...)`.
2. If it does not exist, answer `404` and change nothing.
3. Otherwise delete it with `db.books.delete(id=...)` and answer `303` redirecting to `/`.
4. Remaining books keep their relative order.

## Reads

- One book via `books.get`.

## Writes

- One deletion via `books.delete`.

## Database Interface

- `FEATURE-BOOKS-003` — read: get a book by id - supplies: `id` - returns: `id`, `title`, `author`
- `FEATURE-BOOKS-004` — write: delete a book - supplies: `id` - returns: `id`

## Programmatic Acceptance

=== AC remove-book-omitted-on-next-read ===
Intent: A removed book is answered with 303 and is absent on the next read.
Suite: scoped

from app_server.testing import web_client

client = web_client()
marker = "ac-remove-gone"
title = marker + " title"

def cleanup():
    for row in client.get("/books").get_json():
        if marker in row["title"]:
            client.post(f"/books/{row['id']}/delete")

cleanup()
try:
    assert client.post("/books", data={"title": title, "author": marker + " author"}).status_code == 303
    ours = [row for row in client.get("/books").get_json() if row["title"] == title]
    assert len(ours) == 1
    book_id = ours[0]["id"]
    response = client.post(f"/books/{book_id}/delete")
    assert response.status_code == 303
    after = [row["id"] for row in client.get("/books").get_json()]
    assert book_id not in after
finally:
    cleanup()
=== END AC remove-book-omitted-on-next-read ===

=== AC remove-book-keeps-order ===
Intent: Removing one book leaves the other books in their original relative order.
Suite: scoped

from app_server.testing import web_client

client = web_client()
marker = "ac-remove-order"
titles = [marker + " one", marker + " two", marker + " three"]

def cleanup():
    for row in client.get("/books").get_json():
        if marker in row["title"]:
            client.post(f"/books/{row['id']}/delete")

cleanup()
try:
    for t in titles:
        assert client.post("/books", data={"title": t, "author": marker + " author"}).status_code == 303
    rows = [row for row in client.get("/books").get_json() if marker in row["title"]]
    middle = rows[1]
    assert client.post(f"/books/{middle['id']}/delete").status_code == 303
    remaining = [row["title"] for row in client.get("/books").get_json() if marker in row["title"]]
    assert remaining == [titles[0], titles[2]]
finally:
    cleanup()
=== END AC remove-book-keeps-order ===

=== AC remove-book-unknown-id ===
Intent: Removing an id that does not exist answers 404 and removes nothing.
Suite: scoped

from app_server.testing import web_client

client = web_client()
marker = "ac-remove-unknown"

def cleanup():
    for row in client.get("/books").get_json():
        if marker in row["title"]:
            client.post(f"/books/{row['id']}/delete")

cleanup()
try:
    assert client.post("/books", data={"title": marker + " title", "author": marker + " author"}).status_code == 303
    before = [row["id"] for row in client.get("/books").get_json()]
    unknown_id = max(before) + 1000000
    response = client.post(f"/books/{unknown_id}/delete")
    assert response.status_code == 404
    after = [row["id"] for row in client.get("/books").get_json()]
    assert after == before
finally:
    cleanup()
=== END AC remove-book-unknown-id ===

## User Acceptance

- None.

## Guardrails

- Removing a book never changes the relative order of the remaining books.
- An unknown id never changes stored data.

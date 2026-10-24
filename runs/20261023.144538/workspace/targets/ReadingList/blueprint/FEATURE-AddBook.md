# FEATURE: Add Book

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | A reader adds a book with a title and an author and it is stored. |
| Depends On | ARCHITECTURE.md, DATABASE.md, UI-GENERAL.md |
| Provides | POST /books |
| Consumes | books.create |

## Purpose

Let a reader add a book to the end of the reading list.

## Trigger

A form post to `POST /books` with fields `title` and `author`.

## Sequence

1. Read `title` and `author` from the form, trimmed of surrounding whitespace.
2. Validation of empty values is owned by FEATURE-RejectEmptyTitle.md and FEATURE-RejectEmptyAuthor.md; this feature handles valid submissions.
3. Store the book through `db.books.create(title=..., author=...)`.
4. Answer `303` redirecting to `/`.

## Reads

- None.

## Writes

- One new book via `books.create`.

## Database Interface

- `FEATURE-BOOKS-001` — write: create a book - supplies: `title`, `author` - returns: `id`, `title`, `author`

## Programmatic Acceptance

=== AC add-book-redirects ===
Intent: A valid submission is accepted with a 303 redirect.
Suite: scoped

from app_server.testing import web_client

client = web_client()
marker = "ac-add-redirect"

def cleanup():
    for row in client.get("/books").get_json():
        if marker in row["title"]:
            client.post(f"/books/{row['id']}/delete")

cleanup()
try:
    response = client.post("/books", data={"title": marker + " title", "author": marker + " author"})
    assert response.status_code == 303
finally:
    cleanup()
=== END AC add-book-redirects ===

=== AC add-book-round-trip ===
Intent: An added book is read back through GET /books with the supplied title and author.
Suite: scoped

from app_server.testing import web_client

client = web_client()
marker = "ac-add-roundtrip"
title = marker + " title"
author = marker + " author"

def cleanup():
    for row in client.get("/books").get_json():
        if marker in row["title"]:
            client.post(f"/books/{row['id']}/delete")

cleanup()
try:
    response = client.post("/books", data={"title": title, "author": author})
    assert response.status_code == 303
    listed = client.get("/books")
    assert listed.status_code == 200
    ours = [row for row in listed.get_json() if row["title"] == title]
    assert len(ours) == 1
    assert ours[0]["author"] == author
    assert ours[0]["id"] is not None
finally:
    cleanup()
=== END AC add-book-round-trip ===

=== AC add-book-persists-in-store ===
Intent: An added book is present in the configured store when read through the persistence package.
Suite: scoped

from app_server.testing import web_client
from persistence.testing import committed_session

client = web_client()
marker = "ac-add-store"
title = marker + " title"
author = marker + " author"

def cleanup():
    for row in client.get("/books").get_json():
        if marker in row["title"]:
            client.post(f"/books/{row['id']}/delete")

cleanup()
try:
    response = client.post("/books", data={"title": title, "author": author})
    assert response.status_code == 303
    with committed_session() as db:
        rows = [row for row in db.books.list() if row.title == title]
    assert len(rows) == 1
    assert rows[0].author == author
finally:
    cleanup()
=== END AC add-book-persists-in-store ===

## User Acceptance

- None.

## Guardrails

- A stored book always has a non-empty title and a non-empty author.
- A newly added book is appended after every existing book.

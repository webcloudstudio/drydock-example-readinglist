# FEATURE: Add Book

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | Add a book with a title and author, persist it, and return the stored book. |
| Depends On | FEATURE-AppShell.md, DATABASE.md |
| Provides | POST /books |
| Consumes | books.create, books.get |

## Purpose

Let the reader add a book. A valid submission is stored and returned; the new book appears in later list reads.

## Trigger

A client sends `POST /books` with a JSON body.

## Sequence

1. The route parses the JSON body for `title` and `author`.
2. The service `app_server.services.books.add_book(db, title, author)` stores the book via `books.create`.
3. The route returns 201 with the stored book.

## Routes

| Route | Behavior |
|-------|----------|
| `POST /books` | JSON `{"title": ..., "author": ...}`. Returns 201 with JSON `{"id", "title", "author"}`. Validation of empty fields is owned by FEATURE-RejectEmptyFields.md. |

## Reads

`books.get` is used to return the stored row.

## Writes

`books.create` inserts one row per valid submission; ids ascend in insertion order.

## Database Interface

- `FEATURE-BOOK-001` — write: create a book - supplies: `title`, `author` - returns: `id`, `title`, `author`
- `FEATURE-BOOK-002` — read: retrieve a book by id - supplies: `id` - returns: `id`, `title`, `author`

## Tests

The build writes pytest tests under `tests/` covering a valid add, the 201 response fields, and a read-back of the stored row.

## Programmatic Acceptance

=== AC addbook-create ===
Intent: POST /books answers 201 and returns the title and author that were supplied, with an id.
Requires: python-package=flask; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

title = "ac-addbook-create-title"
author = "ac-addbook-create-author"
client = web_client()
created_id = None
try:
    response = client.post("/books", json={"title": title, "author": author})
    assert response.status_code == 201
    body = response.get_json()
    created_id = body["id"]
    assert isinstance(created_id, int)
    assert body["title"] == title
    assert body["author"] == author
finally:
    if created_id is not None:
        with committed_session() as db:
            db.books.delete(id=created_id)
=== END AC addbook-create ===

=== AC addbook-persisted ===
Intent: A submitted book is read back from the store with the supplied title and author.
Requires: python-package=flask; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

title = "ac-addbook-persist-title"
author = "ac-addbook-persist-author"
created_id = None
try:
    response = web_client().post("/books", json={"title": title, "author": author})
    assert response.status_code == 201
    created_id = response.get_json()["id"]
    with committed_session() as db:
        row = db.books.get(id=created_id)
        assert row.id == created_id
        assert row.title == title
        assert row.author == author
finally:
    if created_id is not None:
        with committed_session() as db:
            db.books.delete(id=created_id)
=== END AC addbook-persisted ===

=== AC addbook-ascending-ids ===
Intent: Two books added in sequence receive ascending ids, preserving insertion order.
Requires: python-package=flask; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

client = web_client()
created = []
try:
    for title in ["ac-addbook-seq-one", "ac-addbook-seq-two"]:
        response = client.post("/books", json={"title": title, "author": "ac-addbook-seq-author"})
        assert response.status_code == 201
        created.append(response.get_json()["id"])
    assert created[0] < created[1]
finally:
    with committed_session() as db:
        for book_id in created:
            db.books.delete(id=book_id)
=== END AC addbook-ascending-ids ===

## User Acceptance

- None.

## Guardrails

- The route never accesses the database directly; it calls the book service.
- A stored book keeps exactly the title and author supplied.

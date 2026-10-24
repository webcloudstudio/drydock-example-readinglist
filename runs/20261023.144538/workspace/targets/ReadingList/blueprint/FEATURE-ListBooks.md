# FEATURE: List Books

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | The application presents stored books in the order they were added. |
| Depends On | ARCHITECTURE.md, DATABASE.md, FEATURE-AddBook.md |
| Provides | GET /books |
| Consumes | books.list |

## Purpose

Let a reader (and the reading list page) view every book in the order added.

## Trigger

A `GET /books` request.

## Sequence

1. Call `db.books.list()`, which returns rows by ascending `id`.
2. Respond `200` with a JSON array of objects carrying `id`, `title`, and `author`, in that same order.
3. An empty store yields an empty array.

## Reads

- All books via `books.list`.

## Writes

- None.

## Database Interface


- `FEATURE-BOOKS-002` — read: books.list - supplies: — - returns: `id`, `title`, `author`

## Programmatic Acceptance

=== AC list-books-ok ===
Intent: GET /books answers 200 with a JSON array whose items carry id, title, and author.
Suite: scoped

from app_server.testing import web_client

client = web_client()
marker = "ac-list-shape"
title = marker + " title"
author = marker + " author"

def cleanup():
    for row in client.get("/books").get_json():
        if marker in row["title"]:
            client.post(f"/books/{row['id']}/delete")

cleanup()
try:
    assert client.post("/books", data={"title": title, "author": author}).status_code == 303
    response = client.get("/books")
    assert response.status_code == 200
    body = response.get_json()
    assert isinstance(body, list)
    ours = [row for row in body if row["title"] == title]
    assert len(ours) == 1
    assert set(["id", "title", "author"]) <= set(ours[0].keys())
finally:
    cleanup()
=== END AC list-books-ok ===

=== AC list-books-order-added ===
Intent: Books are listed in the order they were added.
Suite: scoped

from app_server.testing import web_client

client = web_client()
marker = "ac-list-order"
titles = [marker + " third-added-last", marker + " a-first", marker + " m-second"]

def cleanup():
    for row in client.get("/books").get_json():
        if marker in row["title"]:
            client.post(f"/books/{row['id']}/delete")

cleanup()
try:
    for t in titles:
        assert client.post("/books", data={"title": t, "author": marker + " author"}).status_code == 303
    body = client.get("/books").get_json()
    ours = [row["title"] for row in body if marker in row["title"]]
    assert ours == titles
    ids = [row["id"] for row in body if marker in row["title"]]
    assert ids == sorted(ids)
finally:
    cleanup()
=== END AC list-books-order-added ===

=== AC list-books-matches-store ===
Intent: The listed sequence of ids matches the persistence package's own listing.
Suite: scoped

from app_server.testing import web_client
from persistence.testing import committed_session

client = web_client()
marker = "ac-list-store"

def cleanup():
    for row in client.get("/books").get_json():
        if marker in row["title"]:
            client.post(f"/books/{row['id']}/delete")

cleanup()
try:
    for n in range(3):
        assert client.post("/books", data={"title": f"{marker} {n}", "author": marker + " author"}).status_code == 303
    http_ids = [row["id"] for row in client.get("/books").get_json()]
    with committed_session() as db:
        store_ids = [row.id for row in db.books.list()]
    assert http_ids == store_ids
finally:
    cleanup()
=== END AC list-books-matches-store ===

## User Acceptance

- None.

## Guardrails

- Books are never presented in any order other than the order added.
- The listing never omits a stored book and never shows a removed one.

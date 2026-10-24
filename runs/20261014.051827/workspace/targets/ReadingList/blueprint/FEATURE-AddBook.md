# FEATURE: Add Book

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Accept a title and author, store the book, and reject an empty title or author. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | POST /books |
| Consumes    | books.create |

## Purpose

A reader adds a book with a title and an author. An empty title or author is rejected with a clear error.

## Route

`POST /books` accepts a JSON body with `title` and `author`.

- A valid submission is stored through `books.create` and returns status 201 with the stored book as JSON: `id`, `title`, `author`.
- An empty or whitespace-only `title` returns status 400 with JSON `{"field": "title"}`.
- An empty or whitespace-only `author` returns status 400 with JSON `{"field": "author"}`.
- A rejected submission is not stored.

## Database Interface

- `FEATURE-BOOKS-001` — write: create a book - supplies: `title`, `author` - returns: `id`, `title`, `author`

## Programmatic Acceptance

=== AC add-book-stores-valid ===
Intent: A valid submission returns 201 with the stored book's title and author.

import uuid
from app_server.testing import web_client

title = uuid.uuid4().hex
author = uuid.uuid4().hex
client = web_client()
response = client.post("/books", json={"title": title, "author": author})
assert response.status_code == 201
body = response.get_json()
assert body["title"] == title
assert body["author"] == author
assert isinstance(body["id"], int)
=== END AC add-book-stores-valid ===

=== AC add-book-rejects-empty-title ===
Intent: An empty title returns 400 and names the title field.

import uuid
from app_server.testing import web_client

author = uuid.uuid4().hex
client = web_client()
response = client.post("/books", json={"title": "", "author": author})
assert response.status_code == 400
assert response.get_json()["field"] == "title"
=== END AC add-book-rejects-empty-title ===

=== AC add-book-rejects-empty-author ===
Intent: An empty author returns 400 and names the author field.

import uuid
from app_server.testing import web_client

title = uuid.uuid4().hex
client = web_client()
response = client.post("/books", json={"title": title, "author": ""})
assert response.status_code == 400
assert response.get_json()["field"] == "author"
=== END AC add-book-rejects-empty-author ===

=== AC add-book-rejects-whitespace-title ===
Intent: A whitespace-only title is treated as empty and returns 400.

import uuid
from app_server.testing import web_client

author = uuid.uuid4().hex
client = web_client()
response = client.post("/books", json={"title": "   ", "author": author})
assert response.status_code == 400
assert response.get_json()["field"] == "title"
=== END AC add-book-rejects-whitespace-title ===

## User Acceptance

- None.

## Guardrails

- Never accept an empty title or an empty author.

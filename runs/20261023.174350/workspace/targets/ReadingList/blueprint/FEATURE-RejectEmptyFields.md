# FEATURE: Reject Empty Fields

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | Reject a submission whose title or author is empty with a clear error and store nothing. |
| Depends On | FEATURE-AddBook.md |
| Provides | validate_book_input |
| Consumes | POST /books |

## Purpose

Guarantee the application never accepts an empty title or empty author. Rejection reports a clear, human-readable error naming the offending field.

## Trigger

A submission to `POST /books` (or the page form route) carries a missing, empty, or whitespace-only title or author.

## Sequence

1. The service calls `validate_book_input(title, author)` in `app_server.services.books` before any store call.
2. A value that is missing, not a string, or empty after stripping surrounding whitespace raises `ValueError` whose message names the field (`title` or `author`).
3. `POST /books` converts the error to status 400 with JSON `{"error": <message>}`.
4. Nothing is stored; the book list is unchanged.

## Routes

This feature adds no route of its own; it governs `POST /books` provided by FEATURE-AddBook.md.

## Reads

None.

## Writes

None. A rejected submission writes nothing.

## Database Interface

- None — persistence is owned by FEATURE-AddBook.md.

## Tests

The build writes pytest tests for empty title, empty author, both empty, missing keys, and whitespace-only values, asserting status 400 and that the list is unchanged.

## Programmatic Acceptance

=== AC reject-empty-title ===
Intent: POST /books with an empty title answers 400 and stores nothing.
Requires: python-package=flask; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

client = web_client()
with committed_session() as db:
    before = len(list(db.books.list()))
response = client.post("/books", json={"title": "", "author": "ac-reject-author"})
assert response.status_code == 400
assert isinstance(response.get_json()["error"], str)
with committed_session() as db:
    after = len(list(db.books.list()))
assert after == before
=== END AC reject-empty-title ===

=== AC reject-empty-author ===
Intent: POST /books with an empty author answers 400 and stores nothing.
Requires: python-package=flask; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

client = web_client()
with committed_session() as db:
    before = len(list(db.books.list()))
response = client.post("/books", json={"title": "ac-reject-title", "author": ""})
assert response.status_code == 400
assert isinstance(response.get_json()["error"], str)
with committed_session() as db:
    after = len(list(db.books.list()))
assert after == before
=== END AC reject-empty-author ===

=== AC reject-both-empty ===
Intent: POST /books with both fields empty answers 400 and stores nothing.
Requires: python-package=flask; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

client = web_client()
with committed_session() as db:
    before = len(list(db.books.list()))
response = client.post("/books", json={"title": "", "author": ""})
assert response.status_code == 400
with committed_session() as db:
    after = len(list(db.books.list()))
assert after == before
=== END AC reject-both-empty ===

=== AC reject-whitespace-and-missing ===
Intent: Whitespace-only and missing fields are rejected with 400 and nothing is stored.
Requires: python-package=flask; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

client = web_client()
payloads = [
    {"title": "   ", "author": "ac-reject-ws-author"},
    {"title": "ac-reject-ws-title", "author": "   "},
    {"author": "ac-reject-missing-author"},
    {"title": "ac-reject-missing-title"},
]
with committed_session() as db:
    before = len(list(db.books.list()))
for payload in payloads:
    response = client.post("/books", json=payload)
    assert response.status_code == 400
with committed_session() as db:
    after = len(list(db.books.list()))
assert after == before
=== END AC reject-whitespace-and-missing ===

=== AC reject-validator ===
Intent: validate_book_input raises ValueError for an empty title or author.

from app_server.services.books import validate_book_input

for title, author in [("", "ac-validator-author"), ("ac-validator-title", ""), ("", "")]:
    try:
        validate_book_input(title, author)
    except ValueError:
        continue
    raise AssertionError("empty input was accepted")
=== END AC reject-validator ===

=== AC reject-valid-still-accepted ===
Intent: A submission with both fields present is still accepted with 201 after validation is in place.
Requires: python-package=flask; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

created_id = None
try:
    response = web_client().post(
        "/books", json={"title": "ac-reject-valid-title", "author": "ac-reject-valid-author"}
    )
    assert response.status_code == 201
    created_id = response.get_json()["id"]
finally:
    if created_id is not None:
        with committed_session() as db:
            db.books.delete(id=created_id)
=== END AC reject-valid-still-accepted ===

## User Acceptance

- None.

## Guardrails

- Never accept an empty title or an empty author.
- A rejected submission stores nothing.
- The error message names the offending field and is human-readable.

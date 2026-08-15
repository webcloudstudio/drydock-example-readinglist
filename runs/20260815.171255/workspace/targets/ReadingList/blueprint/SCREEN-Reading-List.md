# SCREEN: Reading List

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Presents the reader-facing form, ordered book list, empty state, validation feedback, and removal controls. |
| Depends On  | UI-GENERAL.md, FEATURE-Book-Creation.md, FEATURE-Ordered-List.md, FEATURE-Book-Removal.md, FEATURE-Incomplete-Submission.md |
| Provides    | reading_list_screen |
| Consumes    | GET /, POST /books, POST /books/{id}/remove, reading_list_ui_patterns |
| Route       | / |
| Parent      | — |
| Main Menu   | Reading List (1) |
| Sub Menu    | — |
| Tab Order   | 1 |

## Layout and Interactions

The single screen contains:

- A title and author form with a direct submission action.
- The current books rendered in insertion order.
- A clear empty-list state when no books exist.
- A removal control for each listed book.
- Clear validation feedback when title or author is missing.

The screen uses `GET /` for the initial and subsequent list reads, `POST /books` for creation, and `POST /books/<int:book_id>/remove` for removal.

## Programmatic Acceptance

=== AC screen-loads ===
Intent: The reading-list screen is reachable at its declared route.
from app import create_app

app = create_app({"TESTING": True})
client = app.test_client()
response = client.get("/")
assert response.status_code == 200
=== END AC screen-loads ===

=== AC screen-accepts-book-submission ===
Intent: The screen supports submitting a title and author through the declared creation route.
from app import create_app

app = create_app({"TESTING": True})
client = app.test_client()
title = "Screen Book"
author = "Screen Author"
response = client.post("/books", data={"title": title, "author": author})
assert response.status_code in (200, 302, 303)
listed = client.get("/")
assert listed.status_code == 200
assert title.encode() in listed.data
assert author.encode() in listed.data
=== END AC screen-accepts-book-submission ===

=== AC screen-supports-removal ===
Intent: The screen supports removing a listed book through the declared removal route.
from app import create_app

app = create_app({"TESTING": True})
client = app.test_client()
title = "Screen Removal"
author = "Screen Removal Author"
client.post("/books", data={"title": title, "author": author})
response = client.post("/books/1/remove")
assert response.status_code in (200, 302, 303)
listed = client.get("/")
assert listed.status_code == 200
assert title.encode() not in listed.data
=== END AC screen-supports-removal ===

=== AC screen-supports-empty-state ===
Intent: The screen responds successfully when the reading list is empty.
from app import create_app

app = create_app({"TESTING": True})
client = app.test_client()
response = client.get("/")
assert response.status_code == 200
=== END AC screen-supports-empty-state ===

## User Acceptance

- A first-time reader can immediately find the title-and-author submission form.
- The screen presents books in insertion order and exposes removal controls.
- The empty-list and validation states are understandable.

## Guardrails

- The screen must not reorder books.
- The screen must not offer submission without both title and author fields.

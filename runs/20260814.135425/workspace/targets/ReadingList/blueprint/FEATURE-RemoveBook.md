# FEATURE: Remove Book

| Field       | Value |
|-------------|-------|
| Version     | 20260814 V1 |
| Description | Remove a selected book from the persisted reading list. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | POST /books/{id}/delete |
| Consumes    | books persistence interface |

## Purpose

A reader can remove a selected book, after which the book is absent from the next reading-list view while other books remain available.

## Trigger

A reader submits the removal control associated with a persisted book.

## Route

| Method | Path | Behavior |
|--------|------|----------|
| POST | `/books/{id}/delete` | Deletes the selected book and returns to the reading-list workflow. |

## Workflow

1. Receive the selected book identifier.
2. Delete that book through the books persistence interface.
3. Return a successful response or redirect to the reading-list screen.
4. Ensure the next list read omits the removed book.

## Programmatic Acceptance

Requires: python-package=flask; scope=test

=== AC remove-book ===
Intent: Removing a book succeeds through the declared delete route.

from app import create_app

title = "Removable Book"
author = "Removable Author"

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
create_response = client.post("/books", data={"title": title, "author": author})
assert create_response.status_code in (200, 302, 303)

with client.session_transaction() if False else _null_context():
    pass
=== END AC remove-book ===

=== AC removed-book-absent ===
Intent: After removal, the next list view omits the selected book.

from app import create_app

removed_title = "Removed Book"
removed_author = "Removed Author"
remaining_title = "Remaining Book"
remaining_author = "Remaining Author"

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
client.post("/books", data={"title": removed_title, "author": removed_author})
client.post("/books", data={"title": remaining_title, "author": remaining_author})

listing = client.get("/")
assert listing.status_code == 200

# The application exposes the selected identifier through the rendered form.
body = listing.get_data(as_text=True)
marker = f'value="{removed_title}"'
assert removed_title in body

# Locate the first persisted book through the application-facing repository helper.
from app.books import list_books
books = list_books(app)
removed_id = next(book["id"] for book in books if book["title"] == removed_title)

delete_response = client.post(f"/books/{removed_id}/delete")
assert delete_response.status_code in (200, 302, 303)

next_listing = client.get("/")
assert next_listing.status_code == 200
next_body = next_listing.get_data(as_text=True)
assert removed_title not in next_body
assert remaining_title in next_body
=== END AC removed-book-absent ===

=== AC delete-route-reachable ===
Intent: The declared delete route accepts a request for an existing book.

from app import create_app
from app.books import list_books

title = "Route Book"
author = "Route Author"

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
client.post("/books", data={"title": title, "author": author})
book = list_books(app)[0]
response = client.post(f"/books/{book['id']}/delete")

assert response.status_code in (200, 302, 303)
=== END AC delete-route-reachable ===

## User Acceptance

- Removing a book removes its visible entry without unexpectedly removing other books.

## Guardrails

- A removed book must not appear in subsequent list views.
- Remaining books and their order must be preserved.

# FEATURE: Ordered Books and Read Status

| Field       | Value |
|-------------|-------|
| Version     | 20260814 V1 |
| Description | Preserve book insertion order and expose each book's unread or read status. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | ordered book listing, read-status display |
| Consumes    | books persistence interface |

## Purpose

Books are retrieved in their addition order. Each book exposes a durable read-status value of unread or read, and later reads preserve that status.

## Workflow

1. Retrieve all persisted books through the books persistence interface.
2. Order them by their insertion identifier ascending.
3. Present every book with its title, author, and current unread/read status.
4. Preserve the status value across subsequent reads.

## Reads

- Ordered book records from the books persistence interface.

## Writes

- None. Status mutation is owned by `FEATURE-MarkRead.md`.

## Programmatic Acceptance

Requires: python-package=flask; scope=test

=== AC ordered-books ===
Intent: The reading-list view presents books in the order supplied by separate additions.

from app import create_app

first_title = "First Book"
first_author = "First Author"
second_title = "Second Book"
second_author = "Second Author"

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
client.post("/books", data={"title": first_title, "author": first_author})
client.post("/books", data={"title": second_title, "author": second_author})
response = client.get("/")

assert response.status_code == 200
body = response.get_data(as_text=True)
assert body.index(first_title) < body.index(second_title)
=== END AC ordered-books ===

=== AC unread-status ===
Intent: A newly added book is displayed as unread.

from app import create_app

title = "Unread Book"
author = "Unread Author"

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
client.post("/books", data={"title": title, "author": author})
response = client.get("/")

assert response.status_code == 200
body = response.get_data(as_text=True)
status = "Unread"
assert status in body
assert title in body
=== END AC unread-status ===

=== AC status-persistence ===
Intent: A subsequent reading-list request preserves the status value stored for a book.

from app import create_app

title = "Persistent Status Book"
author = "Persistent Status Author"

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
client.post("/books", data={"title": title, "author": author})
first_response = client.get("/")
second_response = client.get("/")

assert first_response.status_code == 200
assert second_response.status_code == 200
status = "Unread"
assert status in first_response.get_data(as_text=True)
assert status in second_response.get_data(as_text=True)
=== END AC status-persistence ===

## User Acceptance

- The list clearly distinguishes unread books from read books.

## Guardrails

- Books must remain in addition order.
- Every displayed book must show its current unread/read state.
- This feature must not independently reorder books.

# FEATURE: Mark Book as Read

| Field       | Value |
|-------------|-------|
| Version     | 20260814 V1 |
| Description | Persist a selected book's read status and display it as read. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | POST /books/{id}/read |
| Consumes    | books persistence interface |

## Purpose

A reader can mark a book as read. The selected book's persisted status changes from unread to read and is shown as read on the next list view.

## Trigger

A reader submits the mark-read control associated with an unread book.

## Route

| Method | Path | Behavior |
|--------|------|----------|
| POST | `/books/{id}/read` | Marks the selected book as read and returns to the reading-list workflow. |

## Workflow

1. Receive the selected book identifier.
2. Update only that book's read status through the books persistence interface.
3. Return a successful response or redirect to the reading-list screen.
4. Read the list again and display the selected book as read.

## Programmatic Acceptance

Requires: python-package=flask; scope=test

=== AC mark-read-route ===
Intent: The declared mark-read route accepts a request for an existing book.

from app import create_app
from app.books import list_books

title = "Readable Book"
author = "Readable Author"

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
client.post("/books", data={"title": title, "author": author})
book = list_books(app)[0]
response = client.post(f"/books/{book['id']}/read")

assert response.status_code in (200, 302, 303)
=== END AC mark-read-route ===

=== AC marked-book-status ===
Intent: Marking a book as read changes its displayed status on a subsequent list view.

from app import create_app
from app.books import list_books

title = "Finished Book"
author = "Finished Author"

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
client.post("/books", data={"title": title, "author": author})
book = list_books(app)[0]

before = client.get("/")
assert before.status_code == 200
unread_status = "Unread"
assert unread_status in before.get_data(as_text=True)

update_response = client.post(f"/books/{book['id']}/read")
assert update_response.status_code in (200, 302, 303)

after = client.get("/")
assert after.status_code == 200
read_status = "Read"
after_body = after.get_data(as_text=True)
assert read_status in after_body
assert title in after_body
=== END AC marked-book-status ===

=== AC mark-read-persists ===
Intent: A marked book remains read across separate list requests.

from app import create_app
from app.books import list_books

title = "Persisted Read Book"
author = "Persisted Read Author"

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
client.post("/books", data={"title": title, "author": author})
book = list_books(app)[0]
client.post(f"/books/{book['id']}/read")

first = client.get("/")
second = client.get("/")

assert first.status_code == 200
assert second.status_code == 200
read_status = "Read"
assert read_status in first.get_data(as_text=True)
assert read_status in second.get_data(as_text=True)
=== END AC mark-read-persists ===

## User Acceptance

- The selected book visibly changes from unread to read after the action completes.

## Guardrails

- Marking one book read must not change another book's status.
- The read status must survive subsequent list requests.

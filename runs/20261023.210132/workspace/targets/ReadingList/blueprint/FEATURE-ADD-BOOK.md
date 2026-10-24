# FEATURE: Add Book

| Field       | Value |
|-------------|-------|
| Version     | 20261023 V1 |
| Description | Adds valid books to the persisted reading list. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | POST `/books` |
| Consumes    | `app_server.create_app`, `persistence.books.create` |

## Purpose

A reader submits a title and author to `POST /books`. The feature persists the book through `books.create` and returns the reader to a usable reading-list workflow where the new book can be seen.

## Database Interface

- `FEATURE-ADD-BOOK-001` — write: create a book - supplies: `title`, `author`, `insertion_order` - returns: `id`, `title`, `author`, `insertion_order`

## Workflow

1. Receive title and author form values.
2. Create the book through the persistence contract.
3. Redirect to the primary list page.
4. The subsequent list read includes the created book.

## Programmatic Acceptance

=== AC add-book-route ===
Intent: The book-creation route accepts a valid title and author submission.

from app_server.testing import web_client

title = "Add Book Acceptance Title"
author = "Add Book Acceptance Author"

client = web_client()
response = client.post(
    "/books",
    data={"title": title, "author": author},
)
assert response.status_code == 302

follow_up = client.get("/")
assert follow_up.status_code == 200
body = follow_up.get_data(as_text=True)
assert title in body
assert author in body
=== END AC add-book-route ===

=== AC add-book-persistence ===
Intent: A valid submission is persisted and readable through the public list workflow.

from app_server.testing import web_client

title = "Persisted Add Book Title"
author = "Persisted Add Book Author"

client = web_client()
created_response = client.post(
    "/books",
    data={"title": title, "author": author},
)
assert created_response.status_code == 302

read_response = client.get("/")
assert read_response.status_code == 200
body = read_response.get_data(as_text=True)
assert title in body
assert author in body
=== END AC add-book-persistence ===

## User Acceptance

- A reader can submit a title and author and see the new book in the list.

## Guardrails

- Valid submissions use the generated persistence contract.
- A created book is not silently omitted from the next list read.
- Empty fields are rejected by the validation boundary.

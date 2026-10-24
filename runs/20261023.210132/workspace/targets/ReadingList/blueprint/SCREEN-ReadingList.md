# SCREEN: Reading List

| Field       | Value |
|-------------|-------|
| Version     | 20261023 V1 |
| Description | Defines the primary server-rendered screen for maintaining the reading list. |
| Depends On  | UI-GENERAL.md, FEATURE-READING-LIST.md, FEATURE-ADD-BOOK.md, FEATURE-REMOVE-BOOK.md, FEATURE-VALIDATE-BOOK.md |
| Provides    | primary reading-list screen |
| Consumes    | GET /, POST /books, POST /books/<book_id>/delete |
| Route       | / |
| Parent      | Main |
| Main Menu   | Reading List (1) |
| Sub Menu    | — |
| Tab Order   | 1 |

## Layout

The primary page contains:

- A page heading and reading-list content region.
- A form with accessible title and author inputs and a submit control.
- An ordered list of stored books, showing each title and author.
- A removal control for each stored book.
- A clear empty-list state when no books exist.
- Validation feedback that leaves the form available for correction.

## Interactions

- `GET /` renders the current list in insertion order.
- `POST /books` submits a new book and returns the updated workflow.
- `POST /books/<book_id>/delete` removes the selected book and returns the updated list.
- Invalid submissions remain recoverable through the rendered form and feedback.

## Programmatic Acceptance

=== AC reading-list-screen-load ===
Intent: The primary reading-list screen is reachable and returns a successful response.

from app_server.testing import web_client

client = web_client()
response = client.get("/")

assert response.status_code == 200
=== END AC reading-list-screen-load ===

=== AC reading-list-screen-add ===
Intent: The primary screen accepts a book submission and renders the supplied book after the workflow completes.

from app_server.testing import web_client

title = "Screen Test Title"
author = "Screen Test Author"

client = web_client()
response = client.post("/books", data={"title": title, "author": author})
assert response.status_code == 302

list_response = client.get("/")
assert list_response.status_code == 200
body = list_response.get_data(as_text=True)
assert title in body
assert author in body
=== END AC reading-list-screen-add ===

=== AC reading-list-screen-remove ===
Intent: The primary screen removes a selected book and omits it from the subsequent list response.

from app_server.testing import web_client

title = "Screen Removal Title"
author = "Screen Removal Author"

client = web_client()
create_response = client.post("/books", data={"title": title, "author": author})
assert create_response.status_code == 302

before_response = client.get("/")
assert before_response.status_code == 200
before_body = before_response.get_data(as_text=True)
assert title in before_body
assert author in before_body

from persistence.testing import db_session

with db_session() as db:
    rows = db.books.list()
    selected = next(row for row in rows if row.title == title and row.author == author)
    book_id = selected.id

delete_response = client.post(f"/books/{book_id}/delete")
assert delete_response.status_code == 302

after_response = client.get("/")
assert after_response.status_code == 200
after_body = after_response.get_data(as_text=True)
assert title not in after_body
assert author not in after_body
=== END AC reading-list-screen-remove ===

## User Acceptance

- The reader can understand whether the list is empty, populated, loading, or showing a validation error.
- The add form and removal controls are usable from the primary page.

## Guardrails

- The screen never displays books outside the stored insertion order.
- A removed book is absent on the next list read.
- The form remains available after validation failure.

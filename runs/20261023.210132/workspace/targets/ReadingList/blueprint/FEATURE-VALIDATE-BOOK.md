# FEATURE: Validate Book

| Field       | Value |
|-------------|-------|
| Version     | 20261023 V1 |
| Description | Validates book submissions and returns correction feedback for incomplete entries. |
| Depends On  | ARCHITECTURE.md, DATABASE.md, FEATURE-ADD-BOOK.md |
| Provides    | validation for POST /books |
| Consumes    | POST /books, app_server.create_app, persistence.books.list |

## Purpose

The validation boundary protects the reading list from incomplete books. Submissions with an empty title, empty author, or both are rejected before persistence with a client-error response. The form remains usable so the reader can correct and resubmit.

## Workflow

1. Receive title and author form values at `POST /books`.
2. Reject the submission with HTTP 400 when either required value is empty.
3. Preserve the submitted values and identify the missing field or fields in the rendered feedback.
4. Do not create a persistence record for rejected input.
5. Accept corrected values through the existing add-book workflow.

## Database Interface


- None — persistence is owned by FEATURE-ADD-BOOK.md, FEATURE-READING-LIST.md, FEATURE-REMOVE-BOOK.md.

## Programmatic Acceptance

=== AC validate-book-route ===
Intent: The book submission route rejects an empty title with a client-error response and does not persist the invalid submission.

from app_server.testing import web_client
from persistence.testing import db_session

title = ""
author = "Validation Author"

client = web_client()
response = client.post("/books", data={"title": title, "author": author})

assert response.status_code == 400

with db_session() as db:
    rows = db.books.list()
    assert all(row.title != title or row.author != author for row in rows)
=== END AC validate-book-route ===

=== AC validate-book-author ===
Intent: The book submission route rejects an empty author with a client-error response and does not persist the invalid submission.

from app_server.testing import web_client
from persistence.testing import db_session

title = "Validation Title"
author = ""

client = web_client()
response = client.post("/books", data={"title": title, "author": author})

assert response.status_code == 400

with db_session() as db:
    rows = db.books.list()
    assert all(row.title != title or row.author != author for row in rows)
=== END AC validate-book-author ===

=== AC validate-book-correction ===
Intent: A reader can correct an invalid submission and successfully add the corrected book.

from app_server.testing import web_client

invalid_title = ""
invalid_author = "Correctable Author"
valid_title = "Corrected Title"
valid_author = "Corrected Author"

client = web_client()
invalid_response = client.post(
    "/books",
    data={"title": invalid_title, "author": invalid_author},
)
assert invalid_response.status_code == 400

valid_response = client.post(
    "/books",
    data={"title": valid_title, "author": valid_author},
)
assert valid_response.status_code == 302

list_response = client.get("/")
assert list_response.status_code == 200
body = list_response.get_data(as_text=True)
assert valid_title in body
assert valid_author in body
=== END AC validate-book-correction ===

## User Acceptance

- None.

## Guardrails

- Empty titles and authors are rejected before persistence.
- Validation returns HTTP 400 and keeps the form workflow recoverable.
- Validation feedback identifies the missing required field or fields.

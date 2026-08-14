# FEATURE: Validate Book

| Field       | Value |
|-------------|-------|
| Version     | 20260814 V1 |
| Description | Defines validation and error handling for incomplete book submissions. |
| Depends On  | ARCHITECTURE.md, DATABASE.md, FEATURE-AddBook.md |
| Provides    | book submission validation |
| Consumes     | POST /books |

## Purpose

The application rejects a submission when its title or author is empty, including when the value contains only surrounding whitespace. Rejected submissions return HTTP `400`, preserve the form context, and do not create a database row. The response includes a clear reason for the rejection for the reader.

## Validation Rules

- Reject an empty title.
- Reject an empty author.
- Reject a title or author that becomes empty after surrounding whitespace is removed.
- Never persist or display a rejected book.

## Programmatic Acceptance

Requires: python-package=flask; scope=runtime

=== AC validation-route-reachable ===
Intent: The creation route exposes a contractually defined failure response for an incomplete submission.
from app import create_app

app = create_app({"TESTING": True, "READING_LIST_DATABASE": ":memory:"})
client = app.test_client()
response = client.post("/books", data={"title": "", "author": "Author"})
assert response.status_code == 400
=== END AC validation-route-reachable ===

=== AC validation-empty-title ===
Intent: An empty title is rejected without persistence.
from app import create_app
from app.database import Database

database_path = "acceptance-empty-title.sqlite"
app = create_app({"TESTING": True, "READING_LIST_DATABASE": database_path})
client = app.test_client()
author = "Known Author"

response = client.post("/books", data={"title": "", "author": author})
assert response.status_code == 400
assert Database(database_path).list_books() == []
=== END AC validation-empty-title ===

=== AC validation-empty-author ===
Intent: An empty author is rejected without persistence.
from app import create_app
from app.database import Database

database_path = "acceptance-empty-author.sqlite"
app = create_app({"TESTING": True, "READING_LIST_DATABASE": database_path})
client = app.test_client()
title = "Known Title"

response = client.post("/books", data={"title": title, "author": ""})
assert response.status_code == 400
assert Database(database_path).list_books() == []
=== END AC validation-empty-author ===

=== AC validation-whitespace ===
Intent: Whitespace-only title and author values are rejected without persistence.
from app import create_app
from app.database import Database

database_path = "acceptance-whitespace.sqlite"
app = create_app({"TESTING": True, "READING_LIST_DATABASE": database_path})
client = app.test_client()
whitespace = "   "
response = client.post("/books", data={"title": whitespace, "author": whitespace})

assert response.status_code == 400
assert Database(database_path).list_books() == []
=== END AC validation-whitespace ===

## User Acceptance

- A reader receives a clear reason when a title or author is missing.

## Guardrails

- Empty titles and authors are never stored.
- Empty titles and authors are never displayed as books.
- Validation occurs before persistence.

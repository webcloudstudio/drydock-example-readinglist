# FEATURE: Incomplete Submission

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Rejects book submissions that omit a title or author and reports the missing requirement. |
| Depends On  | FEATURE-Book-Creation.md |
| Provides    | validate_book_submission |
| Consumes    | POST /books, book_creation |

## Purpose

Validate book submissions at the submission boundary before persistence.

## Workflow

A submission is invalid when its title is empty, its author is empty, or both are empty. Invalid submissions are rejected, are not persisted, and return a clear user-facing indication that the required field is missing. Valid submissions continue through the existing creation workflow.

## Programmatic Acceptance

=== AC validation-rejects-empty-title ===
Intent: A submission with an empty title is rejected with a client validation response.
from app import create_app

app = create_app({"TESTING": True})
client = app.test_client()
author = "Known Author"
response = client.post("/books", data={"title": "", "author": author})
assert response.status_code == 400
=== END AC validation-rejects-empty-title ===

=== AC validation-rejects-empty-author ===
Intent: A submission with an empty author is rejected with a client validation response.
from app import create_app

app = create_app({"TESTING": True})
client = app.test_client()
title = "Known Title"
response = client.post("/books", data={"title": title, "author": ""})
assert response.status_code == 400
=== END AC validation-rejects-empty-author ===

=== AC validation-does-not-persist-invalid-submission ===
Intent: Invalid submissions do not appear in the public list.
from app import create_app

app = create_app({"TESTING": True})
client = app.test_client()
title = "Rejected Title"
author = "Rejected Author"
response = client.post("/books", data={"title": title, "author": ""})
assert response.status_code == 400
listed = client.get("/")
assert listed.status_code == 200
assert title.encode() not in listed.data
assert author.encode() not in listed.data
=== END AC validation-does-not-persist-invalid-submission ===

=== AC validation-preserves-valid-submission ===
Intent: A valid submission remains supported by the creation workflow.
from app import create_app

app = create_app({"TESTING": True})
client = app.test_client()
title = "Valid Title"
author = "Valid Author"
response = client.post("/books", data={"title": title, "author": author})
assert response.status_code in (200, 302, 303)
listed = client.get("/")
assert listed.status_code == 200
assert title.encode() in listed.data
assert author.encode() in listed.data
=== END AC validation-preserves-valid-submission ===

## User Acceptance

- A reader receives a clear indication when title or author is required.

## Guardrails

- Never accept or store a submission with an empty title or author.
- Validation must occur before persistence.

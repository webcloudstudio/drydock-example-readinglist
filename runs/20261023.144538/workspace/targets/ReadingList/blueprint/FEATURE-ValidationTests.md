# FEATURE: Validation Tests

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | Automated pytest tests that prove an empty or whitespace-only title or author is rejected with status 400, a reported reason, and nothing stored. |
| Depends On | FEATURE-RejectEmptyTitle.md, FEATURE-RejectEmptyAuthor.md, FEATURE-AddBook.md, ARCHITECTURE.md |
| Provides | tests/test_validation.py |
| Consumes | POST /books, GET /books |

## Purpose

The guardrails "Never accept an empty title or an empty author" and "Never omit a rejection reason when a submission is rejected" require automated coverage. This specification governs the project's own pytest module `tests/test_validation.py`, written by the build agent beside the finished code. It exercises validation only through `POST /books` and `GET /books`.

## Database Interface

- None — persistence is owned by FEATURE-AddBook.md.

## Test Module

`tests/test_validation.py` uses the `web_client` fixture and covers one behavior per test:

| Behavior | Expectation |
|----------|-------------|
| Empty title rejected | Status 400, a non-empty `error`, and `field` naming the title. |
| Whitespace-only title rejected | Same as an empty title. |
| Missing title rejected | Same as an empty title. |
| Empty author rejected | Status 400, a non-empty `error`, and `field` naming the author. |
| Whitespace-only author rejected | Same as an empty author. |
| Missing author rejected | Same as an empty author. |
| Nothing stored on rejection | The list from `GET /books` is unchanged after a rejected submission. |
| Browser rejection shows reason | Without `Accept: application/json` the answer is 400 and the page body is non-empty. |

## Programmatic Acceptance

=== AC validation-tests-module-passes ===
Intent: The validation pytest module exists and every test in it passes against the built application.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys
from pathlib import Path

import app_server

module = Path("tests/test_validation.py")
assert module.is_file()
result = subprocess.run(
    [sys.executable, "-m", "pytest", "-q", str(module)],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC validation-tests-module-passes ===

=== AC validation-empty-title-rejected ===
Intent: An empty title is rejected with 400, a non-empty reason, the title field named, and nothing stored.

from app_server.testing import web_client

client = web_client()
field = "title"
other = "author"
before = client.get("/books").get_json()
response = client.post(
    "/books",
    data={field: "", other: "Valid Author"},
    headers={"Accept": "application/json"},
)
assert response.status_code == 400
body = response.get_json()
assert isinstance(body["error"], str) and body["error"].strip()
assert body["field"] == field
assert client.get("/books").get_json() == before
=== END AC validation-empty-title-rejected ===

=== AC validation-blank-title-rejected ===
Intent: A whitespace-only title is rejected with 400 and a non-empty reason, and nothing is stored.

from app_server.testing import web_client

client = web_client()
field = "title"
blank = "   "
before = client.get("/books").get_json()
response = client.post(
    "/books",
    data={field: blank, "author": "Valid Author"},
    headers={"Accept": "application/json"},
)
assert response.status_code == 400
body = response.get_json()
assert isinstance(body["error"], str) and body["error"].strip()
assert body["field"] == field
assert client.get("/books").get_json() == before
=== END AC validation-blank-title-rejected ===

=== AC validation-missing-title-rejected ===
Intent: A submission with no title field is rejected with 400 and a non-empty reason.

from app_server.testing import web_client

client = web_client()
field = "title"
before = client.get("/books").get_json()
response = client.post(
    "/books",
    data={"author": "Valid Author"},
    headers={"Accept": "application/json"},
)
assert response.status_code == 400
body = response.get_json()
assert isinstance(body["error"], str) and body["error"].strip()
assert body["field"] == field
assert client.get("/books").get_json() == before
=== END AC validation-missing-title-rejected ===

=== AC validation-empty-author-rejected ===
Intent: An empty author is rejected with 400, a non-empty reason, the author field named, and nothing stored.

from app_server.testing import web_client

client = web_client()
field = "author"
other = "title"
before = client.get("/books").get_json()
response = client.post(
    "/books",
    data={field: "", other: "Valid Title"},
    headers={"Accept": "application/json"},
)
assert response.status_code == 400
body = response.get_json()
assert isinstance(body["error"], str) and body["error"].strip()
assert body["field"] == field
assert client.get("/books").get_json() == before
=== END AC validation-empty-author-rejected ===

=== AC validation-blank-author-rejected ===
Intent: A whitespace-only author is rejected with 400 and a non-empty reason, and nothing is stored.

from app_server.testing import web_client

client = web_client()
field = "author"
blank = "   "
before = client.get("/books").get_json()
response = client.post(
    "/books",
    data={"title": "Valid Title", field: blank},
    headers={"Accept": "application/json"},
)
assert response.status_code == 400
body = response.get_json()
assert isinstance(body["error"], str) and body["error"].strip()
assert body["field"] == field
assert client.get("/books").get_json() == before
=== END AC validation-blank-author-rejected ===

=== AC validation-missing-author-rejected ===
Intent: A submission with no author field is rejected with 400 and a non-empty reason.

from app_server.testing import web_client

client = web_client()
field = "author"
before = client.get("/books").get_json()
response = client.post(
    "/books",
    data={"title": "Valid Title"},
    headers={"Accept": "application/json"},
)
assert response.status_code == 400
body = response.get_json()
assert isinstance(body["error"], str) and body["error"].strip()
assert body["field"] == field
assert client.get("/books").get_json() == before
=== END AC validation-missing-author-rejected ===

=== AC validation-browser-rejection-has-body ===
Intent: A rejected browser submission answers 400 with a non-empty page that reports the rejection.

from app_server.testing import web_client

client = web_client()
before = client.get("/books").get_json()
response = client.post("/books", data={"title": "", "author": ""})
assert response.status_code == 400
assert len(response.get_data()) > 0
assert client.get("/books").get_json() == before
=== END AC validation-browser-rejection-has-body ===

## User Acceptance

- None.

## Guardrails

- Tests assert the status code, the presence of a non-empty reason, and the named field, never the wording of the reason.
- A rejected submission never changes the stored list.

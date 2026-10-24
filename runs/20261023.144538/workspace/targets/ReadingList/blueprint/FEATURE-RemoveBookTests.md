# FEATURE: Remove Book Tests

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | Automated pytest tests that prove removing a book omits it on the next read, preserves the order of the rest, and answers 404 for an unknown id. |
| Depends On | FEATURE-RemoveBook.md, FEATURE-AddBook.md, FEATURE-ListBooks.md, ARCHITECTURE.md |
| Provides | tests/test_remove_book.py |
| Consumes | POST /books/{id}/delete, POST /books, GET /books |

## Purpose

The Reading List guardrail "Never ship a behavior without an automated test covering it" applies to removal. This specification governs the project's own pytest module `tests/test_remove_book.py`, written by the build agent beside the finished code against observed output. It exercises removal only through the public HTTP interface.

## Database Interface

- None — persistence is owned by FEATURE-RemoveBook.md.

## Test Module

`tests/test_remove_book.py` uses the `web_client` fixture from `tests/conftest.py` and covers one behavior per test, each named for the behavior:

| Behavior | Expectation |
|----------|-------------|
| Removed book is omitted | After `POST /books/{id}/delete` answers 303, `GET /books` no longer lists that id. |
| Other books remain | Removing one of several books leaves the others listed. |
| Remaining order preserved | The remaining books keep their relative order of addition. |
| Unknown id | `POST /books/{id}/delete` for an id that does not exist answers 404. |
| Repeat removal | Removing the same id twice answers 303 then 404. |

Each test creates the books it needs through `POST /books`, reads ids back from `GET /books`, and removes the books it created before finishing, so tests do not depend on each other's residue.

## Programmatic Acceptance

=== AC remove-tests-module-passes ===
Intent: The remove-book pytest module exists and every test in it passes against the built application.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys
from pathlib import Path

import app_server

module = Path("tests/test_remove_book.py")
assert module.is_file()
result = subprocess.run(
    [sys.executable, "-m", "pytest", "-q", str(module)],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC remove-tests-module-passes ===

=== AC remove-omits-on-next-read ===
Intent: A removed book is absent from GET /books on the next read.

from app_server.testing import web_client

client = web_client()
marker = "AC-rmtests-omit"


def owned():
    return [b for b in client.get("/books").get_json() if b["title"].startswith(marker)]


def cleanup():
    for b in owned():
        client.post(f"/books/{b['id']}/delete")


cleanup()
try:
    title = marker + "-one"
    author = "Remove Author"
    created = client.post("/books", data={"title": title, "author": author})
    assert created.status_code == 303
    found = owned()
    assert len(found) == 1
    book_id = found[0]["id"]
    removed = client.post(f"/books/{book_id}/delete")
    assert removed.status_code == 303
    assert book_id not in [b["id"] for b in client.get("/books").get_json()]
finally:
    cleanup()
=== END AC remove-omits-on-next-read ===

=== AC remove-preserves-order ===
Intent: Removing the middle book leaves the other two listed in the order they were added.

from app_server.testing import web_client

client = web_client()
marker = "AC-rmtests-order"


def owned():
    return [b for b in client.get("/books").get_json() if b["title"].startswith(marker)]


def cleanup():
    for b in owned():
        client.post(f"/books/{b['id']}/delete")


cleanup()
try:
    titles = [marker + "-a", marker + "-b", marker + "-c"]
    for t in titles:
        assert client.post("/books", data={"title": t, "author": "Order Author"}).status_code == 303
    before = owned()
    assert [b["title"] for b in before] == titles
    middle = before[1]
    assert client.post(f"/books/{middle['id']}/delete").status_code == 303
    after = owned()
    assert [b["id"] for b in after] == [before[0]["id"], before[2]["id"]]
finally:
    cleanup()
=== END AC remove-preserves-order ===

=== AC remove-unknown-id-404 ===
Intent: Removing an id that does not exist answers 404.

from app_server.testing import web_client

client = web_client()
existing = [b["id"] for b in client.get("/books").get_json()]
unknown_id = max(existing, default=0) + 100000
assert unknown_id not in existing
response = client.post(f"/books/{unknown_id}/delete")
assert response.status_code == 404
=== END AC remove-unknown-id-404 ===

=== AC remove-twice-second-404 ===
Intent: Removing the same book twice succeeds once and then answers 404.

from app_server.testing import web_client

client = web_client()
marker = "AC-rmtests-twice"


def owned():
    return [b for b in client.get("/books").get_json() if b["title"].startswith(marker)]


def cleanup():
    for b in owned():
        client.post(f"/books/{b['id']}/delete")


cleanup()
try:
    assert client.post("/books", data={"title": marker, "author": "Twice Author"}).status_code == 303
    found = owned()
    assert len(found) == 1
    book_id = found[0]["id"]
    assert client.post(f"/books/{book_id}/delete").status_code == 303
    assert client.post(f"/books/{book_id}/delete").status_code == 404
finally:
    cleanup()
=== END AC remove-twice-second-404 ===

## User Acceptance

- None.

## Guardrails

- Tests reach removal only through the public HTTP routes, never through the store.
- Tests create and remove only the books they own and never reset the store.

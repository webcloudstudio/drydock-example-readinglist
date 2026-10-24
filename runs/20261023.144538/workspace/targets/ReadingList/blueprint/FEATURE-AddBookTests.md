# FEATURE: Add Book Tests

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | Automated pytest tests that prove a reader can add a book and read it back with its title and author. |
| Depends On | FEATURE-AddBook.md |
| Provides | None |
| Consumes | POST /books |

## Purpose

Guarantee that adding a book is covered by an automated test that runs under `pytest -q`.

## Deliverable

`tests/test_add_book.py`, using the `web_client` fixture from `tests/conftest.py`. The file contains pytest tests covering at least:

- a valid `POST /books` is answered 303;
- the added book appears in `GET /books` with the title and author that were submitted;
- adding two books keeps both, in the order added.

Each test uses criterion-owned unique titles and removes the books it created so tests do not depend on each other's residue.

## Reads

`GET /books`.

## Writes

`POST /books`.

## Database Interface

- None — persistence is owned by FEATURE-AddBook.md.

## Programmatic Acceptance

=== AC add-tests-file-defines-tests ===
Intent: tests/test_add_book.py exists, parses, defines at least three test functions, and exercises the books route.
Suite: scoped
Requires: python-package=pytest; scope=test

import ast
from pathlib import Path

path = Path("tests/test_add_book.py")
assert path.is_file()
source = path.read_text(encoding="utf-8")
tree = ast.parse(source)
names = [
    node.name
    for node in ast.walk(tree)
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test_")
]
assert len(names) >= 3
assert "/books" in source
=== END AC add-tests-file-defines-tests ===

=== AC add-tests-pass ===
Intent: The add-book test file passes when run with pytest from the application root.
Suite: scoped
Requires: python-package=pytest; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-m", "pytest", "-q", "tests/test_add_book.py"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC add-tests-pass ===

=== AC add-roundtrip-behavior ===
Intent: Adding a book through POST /books is readable back through GET /books with the supplied title and author.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

title = "AddTestsRoundTripTitle"
author = "AddTestsRoundTripAuthor"


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.title == title and row.author == author:
                db.books.delete(id=row.id)


client = web_client()
purge()
try:
    response = client.post("/books", data={"title": title, "author": author})
    assert response.status_code == 303
    rows = [r for r in client.get("/books").get_json() if r["title"] == title]
    assert len(rows) == 1
    assert rows[0]["author"] == author
finally:
    purge()
=== END AC add-roundtrip-behavior ===

## User Acceptance

- None.

## Guardrails

- Tests assert observable state (status codes and parsed responses), not printed text.
- Tests remove only the books they created.

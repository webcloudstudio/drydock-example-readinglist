# FEATURE: List Books Tests

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | Automated pytest tests that prove books are listed in the order they were added. |
| Depends On | FEATURE-ListBooks.md |
| Provides | None |
| Consumes | GET /books |

## Purpose

Guarantee that listing books in the order added is covered by an automated test that runs under `pytest -q`.

## Deliverable

`tests/test_list_books.py`, using the `web_client` fixture from `tests/conftest.py`. The file contains pytest tests covering at least:

- an empty store returns an empty JSON array from `GET /books` (the test isolates its own data from any residue);
- a single added book is returned with `id`, `title`, and `author`;
- several books added in sequence are returned in the order added, with ascending ids.

Each test uses unique titles and removes the books it created.

## Reads

`GET /books`.

## Writes

`POST /books`, as test setup only.

## Database Interface

- None — persistence is owned by FEATURE-ListBooks.md.

## Programmatic Acceptance

=== AC list-tests-file-defines-tests ===
Intent: tests/test_list_books.py exists, parses, defines at least three test functions, and exercises the books route.
Suite: scoped
Requires: python-package=pytest; scope=test

import ast
from pathlib import Path

path = Path("tests/test_list_books.py")
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
=== END AC list-tests-file-defines-tests ===

=== AC list-tests-pass ===
Intent: The list-books test file passes when run with pytest from the application root.
Suite: scoped
Requires: python-package=pytest; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-m", "pytest", "-q", "tests/test_list_books.py"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC list-tests-pass ===

=== AC list-order-behavior ===
Intent: Books added in sequence are returned by GET /books in the order added.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

author = "ListTestsOrderAuthor"
titles = ["ListTestsFirst", "ListTestsSecond", "ListTestsThird"]


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.author == author:
                db.books.delete(id=row.id)


client = web_client()
purge()
try:
    for t in titles:
        assert client.post("/books", data={"title": t, "author": author}).status_code == 303
    rows = [r for r in client.get("/books").get_json() if r["author"] == author]
    assert [r["title"] for r in rows] == titles
    ids = [r["id"] for r in rows]
    assert ids == sorted(ids)
finally:
    purge()
=== END AC list-order-behavior ===

## User Acceptance

- None.

## Guardrails

- Tests never assume the store is empty; they filter to the books they created.
- Tests assert observable state (parsed responses), not printed text.

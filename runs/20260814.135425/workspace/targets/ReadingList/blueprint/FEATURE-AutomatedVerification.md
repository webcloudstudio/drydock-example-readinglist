# FEATURE: Automated Verification

| Field       | Value |
|-------------|-------|
| Version     | 20260814 V1 |
| Description | Provide isolated automated tests for all required reading-list behaviors. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | focused automated test suite |
| Consumes    | GET /, POST /books, POST /books/{id}/read, POST /books/{id}/delete |

## Purpose

The project test suite verifies the public reading-list workflows, including creation, validation, ordering, removal, marking books read, and displaying status.

## Test Requirements

- Use pytest.
- Create isolated application state for each test.
- Exercise public HTTP behavior through Flask's test client.
- Verify both successful and invalid submission paths.
- Verify read-back state rather than runner output.

## Programmatic Acceptance

Requires: python-package=pytest; scope=test
Requires: python-package=flask; scope=test

=== AC focused-suite-exists ===
Intent: The focused pytest suite executes successfully after the implementation stories are complete.

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-m", "pytest", "tests"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC focused-suite-exists ===

=== AC public-add-route-covered ===
Intent: The automated verification surface can exercise the public book-creation route.

from app import create_app

title = "Coverage Book"
author = "Coverage Author"

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
response = client.post("/books", data={"title": title, "author": author})

assert response.status_code in (200, 302, 303)
=== END AC public-add-route-covered ===

=== AC public-list-route-covered ===
Intent: The automated verification surface can exercise the public list route.

from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
response = client.get("/")

assert response.status_code == 200
=== END AC public-list-route-covered ===

=== AC public-mutation-routes-covered ===
Intent: The automated verification surface can exercise read and delete routes against persisted books.

from app import create_app
from app.books import list_books

title = "Mutation Coverage Book"
author = "Mutation Coverage Author"

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()
client.post("/books", data={"title": title, "author": author})
book = list_books(app)[0]

read_response = client.post(f"/books/{book['id']}/read")
assert read_response.status_code in (200, 302, 303)

delete_response = client.post(f"/books/{book['id']}/delete")
assert delete_response.status_code in (200, 302, 303)
=== END AC public-mutation-routes-covered ===

## User Acceptance

- None. Automated verification is evaluated through the executable suite.

## Guardrails

- Tests must use isolated state and must not depend on test execution order.
- The suite must cover every required behavior named by the project acceptance contract.

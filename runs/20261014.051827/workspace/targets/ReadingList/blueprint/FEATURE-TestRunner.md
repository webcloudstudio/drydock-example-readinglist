# FEATURE: Test Runner

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | POSIX bin/test.sh that runs the complete automated suite and exits with its status; the terminal verification gate. |
| Depends On  | ARCHITECTURE.md, DATABASE.md, FEATURE-AddBook.md, FEATURE-ListBooks.md, FEATURE-RemoveBook.md, SCREEN-ReadingList.md |
| Provides    | sh bin/test.sh |

## Purpose

The reader's project must provide one command that runs every automated test and reports success only when all of them pass.

## Runner

- `bin/test.sh` is a POSIX `sh` script at the application root.
- It runs the complete pytest suite with `.venv/bin/python -m pytest -q` from the application root.
- It exits with the status of that run. It exits nonzero if `.venv` is missing.
- It runs no subset of the suite.

## Tests

- Pytest tests cover adding a book, listing books in insertion order, removing a book, and rejecting an empty title or author, as declared by the feature stories.
- Each behavior has at least one test that calls the public route through `web_client`.

## Database Interface

- None — persistence is owned by FEATURE-AddBook.md.

## Programmatic Acceptance

=== AC test-runner-posix-syntax ===
Intent: bin/test.sh parses as POSIX sh.

import subprocess

result = subprocess.run(["sh", "-n", "bin/test.sh"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC test-runner-posix-syntax ===

=== AC test-runner-full-suite ===
Intent: The complete automated suite runs unfiltered through sh bin/test.sh and exits zero only when every test passes.
Suite: full

import subprocess
import sys

result = subprocess.run(["sh", "bin/test.sh"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC test-runner-full-suite ===

## User Acceptance

- None.

## Guardrails

- Never report a passing suite while any automated test fails.
- Never ship without automated tests covering each behavior.
- `bin/test.sh` must not skip, filter, or reinterpret the suite.

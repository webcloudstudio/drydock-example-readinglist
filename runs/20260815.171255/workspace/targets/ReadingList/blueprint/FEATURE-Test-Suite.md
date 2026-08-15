# FEATURE: Test Suite

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Provides automated coverage and a complete POSIX test launcher for the reading-list application. |
| Depends On  | SCREEN-Reading-List.md |
| Provides    | sh bin/test.sh |
| Consumes    | reading_list_screen, book_creation, ordered_book_listing, book_removal, validate_book_submission |

## Purpose

Provide automated tests for adding books, preserving insertion order, removing books, and rejecting empty titles or authors. The root-level `bin/test.sh` launcher is POSIX-compatible and runs the complete suite from the application root.

## Test Coverage

The project test suite covers:

- Successful creation with title and author.
- Ordered listing and the empty-list state.
- Removal and preservation of remaining order.
- Rejection of empty title, empty author, and both fields empty.
- Non-persistence of rejected submissions.

## Programmatic Acceptance

=== AC complete-suite ===
Intent: The required POSIX test launcher runs the complete automated suite successfully.
Suite: full
Requires: executable=sh; scope=test

import subprocess

result = subprocess.run(
    ["sh", "bin/test.sh"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC complete-suite ===

=== AC launcher-runs-from-root ===
Intent: The test launcher is runnable from the application root using the required command.
Requires: executable=sh; scope=test

import subprocess

result = subprocess.run(
    ["sh", "bin/test.sh"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC launcher-runs-from-root ===

=== AC behavior-suite-command-exists ===
Intent: The complete launcher invocation is the executable project verification boundary.
Requires: executable=sh; scope=test

import subprocess

result = subprocess.run(
    ["sh", "bin/test.sh"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode in (0, 1)
=== END AC behavior-suite-command-exists ===

## User Acceptance

- The complete suite can be run from the application root with `sh bin/test.sh`.

## Guardrails

- `bin/test.sh` must be POSIX-compatible.
- The launcher must run the complete automated suite.
- A nonzero test result must produce a nonzero launcher exit status.

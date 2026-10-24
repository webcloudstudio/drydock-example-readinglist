# FEATURE: Verification

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | The POSIX-compatible bin/test.sh runner and the terminal full-suite gate that proves every automated test passes. |
| Depends On | ARCHITECTURE.md, FEATURE-AddBookTests.md, FEATURE-ListBooksTests.md, FEATURE-RemoveBookTests.md, FEATURE-ValidationTests.md, SCREEN-ReadingList.md |
| Provides | bin/test.sh |

## Purpose

The application root provides `bin/test.sh`, a POSIX `sh` script that runs the complete automated test suite from the application root. `sh bin/test.sh` exits zero only when every test passes. This is the terminal story: it runs after every implementation and test story, runs the whole suite through the Commander-owned dispatcher `sources/full_test.sh`, and preserves the command, exit code, standard output, and standard error as evidence.

## Database Interface

- None — persistence is owned by FEATURE-AddBook.md.

## Runner Behavior

- `bin/test.sh` is written in POSIX `sh`, with no bash-only syntax.
- It changes to the application root (the parent of `bin/`) so it runs correctly from any working directory.
- It activates `.venv` when present, then runs `pytest -q` over the entire suite with no filter, skip, or selection.
- Its exit status is that of `pytest -q`; it never masks a failure.

## Programmatic Acceptance

=== AC runner-is-posix-script ===
Intent: bin/test.sh exists at the application root and parses as POSIX sh.
Requires: executable=sh; scope=test

import subprocess
from pathlib import Path

runner = Path("bin/test.sh")
assert runner.is_file()
result = subprocess.run(["sh", "-n", str(runner)], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC runner-is-posix-script ===

=== AC suite-files-present ===
Intent: Every behavior has its pytest module in the application's test suite.

from pathlib import Path

import app_server

modules = [
    "tests/test_add_book.py",
    "tests/test_list_books.py",
    "tests/test_remove_book.py",
    "tests/test_validation.py",
]
missing = [m for m in modules if not Path(m).is_file()]
print(f"missing modules: {missing}")
assert missing == []
=== END AC suite-files-present ===

=== AC full-suite-gate ===
Intent: The complete suite, run through the staged dispatcher from the application root, exits zero.
Suite: full
Requires: executable=sh; scope=test

import os
import subprocess
import sys

import app_server

result = subprocess.run(
    ["sh", "sources/full_test.sh"],
    capture_output=True,
    text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC full-suite-gate ===

## User Acceptance

- None.

## Guardrails

- `bin/test.sh` never filters, skips, or reinterprets tests and never exits zero while any test fails.
- The full suite runs only in this terminal story; earlier stories run their own scoped slices.

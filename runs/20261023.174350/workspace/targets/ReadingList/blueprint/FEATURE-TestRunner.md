# FEATURE: Test Runner

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | Provide a POSIX-compatible bin/test.sh that runs the complete automated suite and exits zero only when every test passes. |
| Depends On | ARCHITECTURE.md, DATABASE.md, FEATURE-AppShell.md, FEATURE-AddBook.md, FEATURE-RejectEmptyFields.md, FEATURE-ListBooks.md, FEATURE-RemoveBook.md, SCREEN-ReadingList.md |
| Provides | bin/test.sh |
| Consumes | pytest -q |

## Purpose

Give the reader and the build a single dependable command, `sh bin/test.sh`, run from the application root, that executes every automated test and reports success only when all of them pass. This is the terminal verification story: it runs after every implementation story, and its command, exit code, standard output, and standard error are preserved as evidence.

## Trigger

`sh bin/test.sh` from the application root, or `sh sources/full_test.sh`, which dispatches to it.

## Sequence

1. The script changes to the application root (the parent of `bin/`), independent of the caller's working directory.
2. It activates `.venv` when `.venv/bin/activate` exists; otherwise it uses the interpreter on `PATH`.
3. It runs `pytest -q`.
4. It exits with pytest's exit status, so zero means every test passed and any failure, error, or collection problem is non-zero.

## Interfaces

| Interface | Contract |
|-----------|----------|
| `bin/test.sh` | POSIX `sh` only: no bashisms, no arrays, no `[[ ]]`. Uses `.` rather than `source`. Does not mask pytest's exit status. |

## Coverage Expectations

The suite under `tests/` contains tests for adding a book, listing books in the order added, removing a book, and rejecting an empty title or author. Each behavior has at least one test.

## Reads

- `tests/` and `.venv` in the application root.

## Writes

- None beyond what pytest itself writes (caches).

## Database Interface

- None — persistence is owned by FEATURE-AddBook.md.

## Programmatic Acceptance

=== AC test-runner-posix-syntax ===
Intent: bin/test.sh exists and parses as POSIX sh without errors.
Suite: scoped

import subprocess
from pathlib import Path

script = Path("bin/test.sh")
assert script.is_file()
result = subprocess.run(["sh", "-n", "bin/test.sh"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC test-runner-posix-syntax ===

=== AC test-runner-covers-behaviors ===
Intent: The test suite contains test modules for the add, list, remove, and rejection behaviors and pytest collects them without error.
Suite: scoped

import subprocess
import sys
from pathlib import Path

tests = sorted(Path("tests").glob("test_*.py"))
assert len(tests) >= 4
result = subprocess.run(
    [sys.executable, "-m", "pytest", "--collect-only", "-q"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC test-runner-covers-behaviors ===

=== AC test-runner-full-suite ===
Intent: The Commander-owned entry point sources/full_test.sh dispatches to bin/test.sh and the complete automated suite exits zero.
Suite: full

import os
import subprocess

result = subprocess.run(
    ["sh", "sources/full_test.sh"],
    capture_output=True, text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC test-runner-full-suite ===

=== AC test-runner-direct ===
Intent: Running sh bin/test.sh from the application root exits zero.
Suite: full

import os
import subprocess

result = subprocess.run(
    ["sh", "bin/test.sh"],
    capture_output=True, text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC test-runner-direct ===

## User Acceptance

- None.

## Guardrails

- A test run is never reported as passing unless every automated test passes; the script's exit status is pytest's exit status.
- The script uses only POSIX sh constructs.
- The script does not skip, filter, or deselect tests.

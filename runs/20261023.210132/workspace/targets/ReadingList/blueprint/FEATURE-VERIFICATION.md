# FEATURE: Verification

| Field       | Value |
|-------------|-------|
| Version     | 20261023 V1 |
| Description | Provides the complete POSIX automated test runner for the ReadingList application. |
| Depends On  | ARCHITECTURE.md, DATABASE.md, UI-GENERAL.md, FEATURE-READING-LIST.md, FEATURE-ADD-BOOK.md, FEATURE-REMOVE-BOOK.md, FEATURE-VALIDATE-BOOK.md, SCREEN-ReadingList.md |
| Provides    | bin/test.sh, complete automated test suite |
| Consumes    | primary reading-list screen, GET /, POST /books, POST /books/<book_id>/delete |

## Verification Contract

`bin/test.sh` is executable from the application root and is POSIX-compatible. It runs the complete automated test suite without filtering. It exits zero only when every automated test passes and preserves the suite's standard output and standard error.

The suite covers:

- Adding a valid book.
- Listing books in insertion order.
- Removing a selected book.
- Rejecting an empty title.
- Rejecting an empty author.

## Programmatic Acceptance

=== AC verification-runner-present ===
Intent: The delivered application provides an executable test runner at the required path.

from pathlib import Path
import os

runner = Path("bin/test.sh")
assert runner.is_file()
assert os.access(runner, os.X_OK)
=== END AC verification-runner-present ===

=== AC verification-full-suite ===
Intent: The complete staged release harness runs the delivered test runner successfully.
Suite: full

import subprocess

result = subprocess.run(
    ["sh", "sources/full_test.sh"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC verification-full-suite ===

## User Acceptance

- None.

## Guardrails

- `bin/test.sh` remains POSIX-compatible.
- The runner executes the complete automated suite from the application root.
- A failing automated test produces a nonzero exit status.

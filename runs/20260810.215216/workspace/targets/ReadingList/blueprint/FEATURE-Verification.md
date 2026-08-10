# FEATURE: Verification

| Field       | Value |
|-------------|-------|
| Version     | 20260810 V1 |
| Description | Provide the complete POSIX test runner and automated behavior coverage. |
| Depends On  | ARCHITECTURE.md, DATABASE.md, UI-GENERAL.md, FEATURE-Add-Book.md, FEATURE-List-Books.md, FEATURE-Validate-Book.md, FEATURE-Remove-Book.md, SCREEN-Reading-List.md |
| Provides    | sh bin/test.sh |
| Consumes    | application test suite |

## Verification Workflow

`bin/test.sh` is executable by POSIX `sh` from the application root. It invokes the complete automated test suite without narrowing the test selection. Its exit status is the suite's exit status: zero only when every test passes. The automated suite covers adding, listing, insertion ordering, validation, and removal.

## Programmatic Acceptance

Requires: executable=sh; scope=test

Requires: python-package=pytest; scope=test

### complete-suite-run
The complete automated test suite passes through the required POSIX runner.

Suite: full

Sea Trials: st-001, st-006

```python
import os
import subprocess

result = subprocess.run(
    ["sh", "bin/test.sh"],
    capture_output=True,
    text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
```

### runner-is-posix-invocable
The runner can be invoked from the application root using POSIX `sh`.

```python
import os
import subprocess

result = subprocess.run(
    ["sh", "bin/test.sh"],
    capture_output=True,
    text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr)
assert result.returncode in (0, 1)
```

### suite-covers-book-behaviors
The test suite contains executable coverage for each required book behavior.

```python
from pathlib import Path

test_files = list(Path("tests").glob("**/*.py"))
source = "\n".join(path.read_text(encoding="utf-8") for path in test_files)

assert "add" in source.lower()
assert "list" in source.lower()
assert "remov" in source.lower()
assert "author" in source.lower()
```

## User Acceptance

- A developer can run `sh bin/test.sh` from the application root without additional instructions.

## Guardrails

- The runner preserves the command, exit code, standard output, and standard error as verification evidence.
- The suite runs locally and does not transmit reader data to a third-party service.

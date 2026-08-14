# FEATURE: Complete Test Command

| Field       | Value |
|-------------|-------|
| Version     | 20260814 V1 |
| Description | Provide a POSIX-compatible command that runs the complete automated test suite. |
| Depends On  | ARCHITECTURE.md |
| Provides    | sh bin/test.sh |
| Consumes    | focused automated test suite |

## Purpose

The application root provides an executable `bin/test.sh` command. Running `sh bin/test.sh` invokes the complete automated suite and returns success only when the suite succeeds.

## Command Contract

- Path: `bin/test.sh`
- Invocation: `sh bin/test.sh`
- Shell compatibility: POSIX.
- Working directory: application root.
- Output and error streams: preserve the test runner's normal output and error behavior.
- Exit status: zero only when every automated test passes.

## Programmatic Acceptance

Requires: executable=sh; scope=test
Requires: executable=python3; scope=test

=== AC test-command-executable ===
Intent: The application root contains the declared test command and it can be invoked with sh.

from pathlib import Path
import os
import stat

script = Path("bin/test.sh")
assert script.is_file()
mode = script.stat().st_mode
assert mode & stat.S_IXUSR or mode & stat.S_IXGRP or mode & stat.S_IXOTH
=== END AC test-command-executable ===

=== AC test-command-success ===
Intent: The declared test command exits zero when the complete automated suite passes.

import os
import subprocess

result = subprocess.run(
    ["sh", "bin/test.sh"],
    capture_output=True,
    text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr, file=__import__("sys").stderr)
assert result.returncode == 0
=== END AC test-command-success ===

=== AC suite-full ===
Intent: The terminal test command runs the complete automated suite successfully.
Suite: full

import os
import subprocess
import sys

result = subprocess.run(
    ["sh", "bin/test.sh"],
    capture_output=True,
    text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC suite-full ===

## User Acceptance

- A developer can run `sh bin/test.sh` from the application root to verify the project.

## Guardrails

- The command must be POSIX-compatible.
- The command must not report success when any automated test fails.
- The command must preserve the test runner's standard output and standard error.

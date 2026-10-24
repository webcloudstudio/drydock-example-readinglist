# Evidence: Block 14 · Feature (block-14)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 2951
- execution id: 20261023.151937.051Z-e7e7d08e

## Stories built
- Provide the POSIX bin/test.sh runner and gate on the complete suite. (verification) [story]

## Acceptance tooling authorization
- VERIFICATION.md#runner-is-posix-script: executable=sh; scope=test; authorization=existing Target environment
- VERIFICATION.md#full-suite-gate: executable=sh; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 781)
- implements: VERIFICATION.md (SP 1137)

## Build directory changes
- bin/test.sh
- data/app.db
- tests/test_test_runner.py

## Pre-build acceptance observation
- RED: runner-is-posix-script (VERIFICATION.md)
  intent: bin/test.sh exists at the application root and parses as POSIX sh.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      runner = PosixPath('bin/test.sh')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "runner-is-posix-script.py", line 5, in <module>
        assert runner.is_file()
               ^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): suite-files-present (VERIFICATION.md)
  intent: Every behavior has its pytest module in the application's test suite.
  return code: 0
  stdout:
    missing modules: []
- RED: full-suite-gate (VERIFICATION.md)
  intent: The complete suite, run through the staged dispatcher from the application root, exits zero.
  return code: 1
  stderr:
    error: no bin/test.sh at the application root.
    st-001 requires the application to provide a POSIX-compatible bin/test.sh that exits
    zero when every automated test passes.
    
    --- drydock: values at failure ---
      result = CompletedProcess(args=['sh', 'sources/full_test.sh'], returncode=1, stdout='', stderr='error: no bin/test.sh at the application root.\nst-001 requires the application to provide a POSIX-compatible bin/test.sh that exits\nzero when every automated test passes.\n')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "full-suite-gate.py", line 15, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: runner-is-posix-script (VERIFICATION.md)
  intent: bin/test.sh exists at the application root and parses as POSIX sh.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: suite-files-present (VERIFICATION.md)
  intent: Every behavior has its pytest module in the application's test suite.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    missing modules: []
- PASS: full-suite-gate (VERIFICATION.md)
  intent: The complete suite, run through the staged dispatcher from the application root, exits zero.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    ........................................................................ [ 37%]
    ........................................................................ [ 75%]
    ...............................................                          [100%]
    191 passed in 11.18s

## Build summary
Build directory has no `bin/test.sh` yet, and all four suite modules the AC checks for already exist. Writing the runner now.The suite ran from `/` and passed (185 tests), but `set -u` makes the `.venv` activate script fail on `OSTYPE`, so activation is silently incomplete. Scoping `set -u` off around the activation fixes that.Clean now. Next, deterministic tests for the runner's behavior. I'll check the existing test style first.The helper resolved `sys.executable` through its symlink, which points at the base interpreter and not `.venv/bin`. Dropping `resolve()` fixes it.The new runner tests pass. Now the declared full-suite gate, invoked exactly as the AC declares it.Gate passes. Checking that only my two files changed in the working tree.RESULT: SUCCESS

FILES CHANGED:
- bin/test.sh
- tests/test_test_runner.py

SUMMARY:
- `bin/test.sh` is a POSIX `sh` runner. It changes to the application root (the parent of `bin/`), activates `.venv` when present, and then `exec`s `pytest -q` over the whole suite with no filter, so its exit status is pytest's. The venv activate script reads unset variables, so `set -u` is relaxed only around the `.` line.
- `tests/test_test_runner.py` adds six tests. Each runs the real runner against a temporary application root and reads back the exit status:
  - the script parses under `sh -n`
  - a passing suite exits 0
  - a failing suite exits nonzero, including when one of several tests fails
  - the runner works from an unrelated working directory
  - a failing suite exits 1, so the runner doesn't mask pytest's status
- Declared acceptance checks:
  - `runner-is-posix-script`: `sh -n bin/test.sh` exits 0.
  - `suite-files-present`: all four required modules exist (`test_add_book.py`, `test_list_books.py`, `test_remove_book.py`, `test_validation.py`).
  - `full-suite-gate`: `sh sources/full_test.sh` exits 0 with 191 passed. The dispatcher runs `bin/test.sh`, which runs the full suite.
- Test counts: the project suite was 185 passed before the new file, and 191 passed after. The six new runner tests were run separately and all passed.
- `sources/` is untouched. Nothing was staged or committed, and nothing was written under `evidence/`, `MANIFEST.md`, or `QuarterDeck/`.

Choices I made:
- The runner runs `pytest -q` directly, as the stack declares, rather than `python -m pytest`.
- The runner's own tests use temporary application roots, so they never re-enter this suite.

BLOCKERS:
- None.

<blueprint-decisions>
[{"spec":"VERIFICATION.md","severity":"Low","subject":"Venv activation under set -u","decision":"The runner sources .venv/bin/activate with set -u relaxed around it, because the activate script references OSTYPE, which is unset under dash. Alternative was prepending .venv/bin to PATH without sourcing. Sourcing keeps the activation the spec describes. Is that acceptable?"}]
</blueprint-decisions>

FILES CHANGED are as above. The `blueprint-decisions` payload is for the reviewer.

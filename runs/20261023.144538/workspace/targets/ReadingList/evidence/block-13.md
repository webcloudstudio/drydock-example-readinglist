# Evidence: Block 13 · Service (block-13)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 5086
- execution id: 20261023.151653.150Z-aa70569b

## Stories built
- Provide automated pytest tests for rejecting an empty title or author. (test-validation) [story]

## Acceptance tooling authorization
- FEATURE-ValidationTests.md#validation-tests-module-passes: executable=python3; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 781)
- implements: FEATURE-ValidationTests.md (SP 2684)
- context: ARCHITECTURE_compact.md (SP 281)
- context: DATABASE_compact.md (SP 360)

## Build directory changes
- data/app.db
- tests/test_validation.py

## Pre-build acceptance observation
- RED: validation-tests-module-passes (FEATURE-ValidationTests.md)
  intent: The validation pytest module exists and every test in it passes against the built application.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      module = PosixPath('tests/test_validation.py')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "validation-tests-module-passes.py", line 8, in <module>
        assert module.is_file()
               ^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): validation-empty-title-rejected (FEATURE-ValidationTests.md)
  intent: An empty title is rejected with 400, a non-empty reason, the title field named, and nothing stored.
  return code: 0
- GREEN (prepassed): validation-blank-title-rejected (FEATURE-ValidationTests.md)
  intent: A whitespace-only title is rejected with 400 and a non-empty reason, and nothing is stored.
  return code: 0
- GREEN (prepassed): validation-missing-title-rejected (FEATURE-ValidationTests.md)
  intent: A submission with no title field is rejected with 400 and a non-empty reason.
  return code: 0
- GREEN (prepassed): validation-empty-author-rejected (FEATURE-ValidationTests.md)
  intent: An empty author is rejected with 400, a non-empty reason, the author field named, and nothing stored.
  return code: 0
- GREEN (prepassed): validation-blank-author-rejected (FEATURE-ValidationTests.md)
  intent: A whitespace-only author is rejected with 400 and a non-empty reason, and nothing is stored.
  return code: 0
- GREEN (prepassed): validation-missing-author-rejected (FEATURE-ValidationTests.md)
  intent: A submission with no author field is rejected with 400 and a non-empty reason.
  return code: 0
- GREEN (prepassed): validation-browser-rejection-has-body (FEATURE-ValidationTests.md)
  intent: A rejected browser submission answers 400 with a non-empty page that reports the rejection.
  return code: 0

## Post-build programmatic acceptance
- PASS: validation-tests-module-passes (FEATURE-ValidationTests.md)
  intent: The validation pytest module exists and every test in it passes against the built application.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    ................................................                         [100%]
    48 passed in 1.11s
- PASS: validation-empty-title-rejected (FEATURE-ValidationTests.md)
  intent: An empty title is rejected with 400, a non-empty reason, the title field named, and nothing stored.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validation-blank-title-rejected (FEATURE-ValidationTests.md)
  intent: A whitespace-only title is rejected with 400 and a non-empty reason, and nothing is stored.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validation-missing-title-rejected (FEATURE-ValidationTests.md)
  intent: A submission with no title field is rejected with 400 and a non-empty reason.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validation-empty-author-rejected (FEATURE-ValidationTests.md)
  intent: An empty author is rejected with 400, a non-empty reason, the author field named, and nothing stored.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validation-blank-author-rejected (FEATURE-ValidationTests.md)
  intent: A whitespace-only author is rejected with 400 and a non-empty reason, and nothing is stored.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validation-missing-author-rejected (FEATURE-ValidationTests.md)
  intent: A submission with no author field is rejected with 400 and a non-empty reason.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validation-browser-rejection-has-body (FEATURE-ValidationTests.md)
  intent: A rejected browser submission answers 400 with a non-empty page that reports the rejection.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
I'll start by inspecting the build directory and the staged sources.The build directory already has the application. Next I'll read the existing tests, the app code, and the test runner so the new module follows their conventions.The sibling `test_reject_empty_author.py` isolates each test in its own SQLite store and applies `schema.sql`. Before I decide between that and the spec's `web_client` fixture, I'll check how settings resolve the store and whether the schema is auto-applied.The spec's `web_client` fixture reads `DATABASE_URL` when it creates the app, so I can keep the sibling isolation pattern and still use that fixture. Each test gets its own provisioned SQLite file, so rejections never touch `data/app.db`. I'll write the module now.Now I'll run the new module through the project's venv, then the full project suite to confirm nothing else broke.All 48 new tests pass, and the full suite passes at 185. Next I'll run each declared acceptance criterion from the spec as a standalone script, the way the harness does, with the module-level script copies kept in a scratch directory outside the build tree.All eight criteria exit 0. Last, I'll confirm which files changed in the build tree.RESULT: SUCCESS

FILES CHANGED:
- tests/test_validation.py

SUMMARY:
Added `tests/test_validation.py`, which covers the FEATURE-ValidationTests spec. It runs eight rejected submissions (empty, whitespace-only, and missing title; empty, whitespace-only, and missing author) through `POST /books`. Each test reads its outcome back through the public interface (the HTTP status, the parsed JSON body, and `GET /books`). The tests check the status code, a non-empty `error`, the named `field`, that the stored list is unchanged after a rejection, and that a browser-style rejection returns 400 with a non-empty page.

Choices I made:
- Each test gets its own SQLite store, provisioned from `schema.sql`, following the sibling reject-empty modules. The `web_client` fixture reads `DATABASE_URL` at creation, so it uses that store and never touches `data/app.db`.
- The "stored list unchanged" check seeds one book first, so a rejection that wrongly stored a row would be caught.
- Assertions check status, presence of a reason, and field name, never the reason's wording, per the spec's guardrail.

Verification:
- `.venv/bin/python -m pytest -q tests/test_validation.py`: 48 passed, exit 0.
- `.venv/bin/python -m pytest -q` (full project suite): 185 passed, exit 0.
- All eight declared acceptance criteria from the spec, run as standalone scripts with the project venv: each exits 0.
- `git status` shows only `tests/test_validation.py` as new. I did not run `git add` or commit.

BLOCKERS:
- None.

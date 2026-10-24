# Evidence: Block 11 · Service (block-11)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 3644
- execution id: 20261023.151221.415Z-e9ae3d38

## Stories built
- Provide automated pytest tests for listing books in the order added. (test-list-books) [story]

## Acceptance tooling authorization
- FEATURE-ListBooksTests.md#list-tests-file-defines-tests: python-package=pytest; scope=test; authorization=existing Target environment
- FEATURE-ListBooksTests.md#list-tests-pass: python-package=pytest; scope=test; authorization=existing Target environment
- FEATURE-ListBooksTests.md#list-order-behavior: python-package=pytest; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 781)
- implements: FEATURE-ListBooksTests.md (SP 1259)
- context: ARCHITECTURE_compact.md (SP 281)
- context: DATABASE_compact.md (SP 360)

## Build directory changes
- data/app.db

## Pre-build acceptance observation
- GREEN (prepassed): list-tests-file-defines-tests (FEATURE-ListBooksTests.md)
  intent: tests/test_list_books.py exists, parses, defines at least three test functions, and exercises the books route.
  return code: 0
- GREEN (prepassed): list-tests-pass (FEATURE-ListBooksTests.md)
  intent: The list-books test file passes when run with pytest from the application root.
  return code: 0
  stdout:
    ............                                                             [100%]
    12 passed in 0.33s
- GREEN (prepassed): list-order-behavior (FEATURE-ListBooksTests.md)
  intent: Books added in sequence are returned by GET /books in the order added.
  return code: 0

## Post-build programmatic acceptance
- PASS: list-tests-file-defines-tests (FEATURE-ListBooksTests.md)
  intent: tests/test_list_books.py exists, parses, defines at least three test functions, and exercises the books route.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: list-tests-pass (FEATURE-ListBooksTests.md)
  intent: The list-books test file passes when run with pytest from the application root.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    ............                                                             [100%]
    12 passed in 0.44s
- PASS: list-order-behavior (FEATURE-ListBooksTests.md)
  intent: Books added in sequence are returned by GET /books in the order added.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Agent self-report (advisory)
The build agent declared a failure. This is advisory only; the programmatic acceptance above is the authority for this block's outcome.
- summary: No files needed writing; the list-books deliverable already existed from block-5 and passes all declared checks.
- detail:
    The step's tests (tests/test_list_books.py) were already committed and green, with all three declared acceptance checks and the full suite (141) passing. Nothing was modified, so the contract requires RESULT: FAILED. Before rerunning, decide whether block-11 should be closed as already satisfied; a rerun would reproduce this same result and change nothing.

## Build summary
The project already has a `tests/test_list_books.py`, and `bin/` has no `test.sh`. I'll read the existing files before writing anything.The `tests/test_list_books.py` file already exists and the tree is clean. I'll check whether it is tracked and whether it passes, then run the declared acceptance checks.The file is tracked (built in block-5) and its 12 tests pass. Next I'll run the three declared acceptance checks from the spec, plus the project suite.The order check failed only because `-I` ignores `PYTHONPATH`. I'll rerun it with the project root on the path; the script directory holds only my two files, so dropping `-I` is safe here.RESULT: FAILED

FILES CHANGED:
- (none; `tests/test_list_books.py` already existed and was built in block-5, so this step wrote nothing)

SUMMARY:
The test-list-books deliverable is already in place and passes. I did not change any file, so I'm reporting FAILED per the contract's no-files-written rule, not because the behavior is missing. Please decide whether to mark block-11 complete without a rerun, or rerun it after you've reviewed this result.

Verified in the build directory:
- Declared acceptance checks:
  - `list-tests-file-defines-tests`: PASS (12 `test_` functions, `/books` present).
  - `list-tests-pass`: PASS (`pytest -q tests/test_list_books.py`, 12 passed, exit 0).
  - `list-order-behavior`: PASS (run as a standalone script against the configured store; it purges its own rows afterwards).
- Project suite: `pytest -q` gives 141 passed, exit 0.
- Coverage in `tests/test_list_books.py` matches the spec: empty array, one book with `id`/`title`/`author`, several books in insertion order, ascending ids, and listing consistent with the store order.
- Git: the working tree is clean and the file is tracked.

One deviation from the spec text: the spec asks tests to use unique titles and remove the books they create. The existing tests instead give each test its own temporary SQLite store, which isolates them more strongly and makes cleanup unnecessary. I kept that rather than rewrite working tests.

Out of scope for this block, but it will matter at the release gate: `bin/test.sh` does not exist yet, so `sources/full_test.sh` will fail with the st-001 error until a later block adds it.

BLOCKERS:
- Nothing blocks the test deliverable. The contract's rule for a step that writes no files forces FAILED.

FAILURE_SUMMARY: No files needed writing; the list-books deliverable already existed from block-5 and passes all declared checks.
FAILURE_DETAIL: The step's tests (tests/test_list_books.py) were already committed and green, with all three declared acceptance checks and the full suite (141) passing. Nothing was modified, so the contract requires RESULT: FAILED. Before rerunning, decide whether block-11 should be closed as already satisfied; a rerun would reproduce this same result and change nothing.

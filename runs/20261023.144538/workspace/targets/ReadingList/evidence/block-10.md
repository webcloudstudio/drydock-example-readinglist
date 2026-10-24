# Evidence: Block 10 · Service (block-10)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 3618
- execution id: 20261023.151000.516Z-4c2636a3

## Stories built
- Provide automated pytest tests for adding a book. (test-add-book) [story]

## Acceptance tooling authorization
- FEATURE-AddBookTests.md#add-tests-file-defines-tests: python-package=pytest; scope=test; authorization=existing Target environment
- FEATURE-AddBookTests.md#add-tests-pass: python-package=pytest; scope=test; authorization=existing Target environment
- FEATURE-AddBookTests.md#add-roundtrip-behavior: python-package=pytest; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 781)
- implements: FEATURE-AddBookTests.md (SP 1223)
- context: ARCHITECTURE_compact.md (SP 281)
- context: DATABASE_compact.md (SP 360)

## Build directory changes
- data/app.db
- tests/test_add_book.py

## Pre-build acceptance observation
- GREEN (prepassed): add-tests-file-defines-tests (FEATURE-AddBookTests.md)
  intent: tests/test_add_book.py exists, parses, defines at least three test functions, and exercises the books route.
  return code: 0
- GREEN (prepassed): add-tests-pass (FEATURE-AddBookTests.md)
  intent: The add-book test file passes when run with pytest from the application root.
  return code: 0
  stdout:
    ....................                                                     [100%]
    20 passed in 0.46s
- GREEN (prepassed): add-roundtrip-behavior (FEATURE-AddBookTests.md)
  intent: Adding a book through POST /books is readable back through GET /books with the supplied title and author.
  return code: 0

## Post-build programmatic acceptance
- PASS: add-tests-file-defines-tests (FEATURE-AddBookTests.md)
  intent: tests/test_add_book.py exists, parses, defines at least three test functions, and exercises the books route.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: add-tests-pass (FEATURE-AddBookTests.md)
  intent: The add-book test file passes when run with pytest from the application root.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    ...........................                                              [100%]
    27 passed in 0.97s
- PASS: add-roundtrip-behavior (FEATURE-AddBookTests.md)
  intent: Adding a book through POST /books is readable back through GET /books with the supplied title and author.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
The existing suite is green (134 passed). `tests/test_add_book.py` doesn't exist yet, so I'll write it now. Per the spec, it uses the `web_client` fixture against the configured store, unique titles per test, and removes only the books it created.The write reported "updated", not "created", and `tests/test_add_book.py` was in the earlier file listing. I overwrote a file I hadn't read. Checking git to see what it contained.I made a mistake. The file already existed and was committed in `149030d` (Build block-4, FEATURE-AddBook). Its tests cover the `app` fixture and the empty-field rules, and they still pass. I'm restoring it from git and adding the new round-trip tests to it, so nothing is lost.The file is back to its committed content, which is what the notice shows. Now I'll add the new imports and round-trip tests alongside the existing ones.Now I'll run the declared acceptance check (`pytest -q tests/test_add_book.py`), the full suite, and the spec's round-trip criterion script.The round-trip check failed only because I ran it with `-I`, which ignores the project path. The pytest results are good: 27 passed in the add-book file and 141 across the suite. Rerunning the round-trip criterion with the project on the path.I added the add-book round-trip tests to `tests/test_add_book.py`, and the suite is green. One mistake along the way: I overwrote that file before reading it, then restored it from git. The file already held the committed FEATURE-AddBook tests (Build block-4), so I added the new tests to it rather than replacing it. Nothing from the committed version was lost.

**What the new tests cover** (7 tests, all using the `web_client` fixture against the configured store):
- A valid `POST /books` answers 303 with `Location: /`.
- The added book appears in `GET /books` with the submitted title and author.
- The book is stored with the submitted title and author, read back through `committed_session`.
- Surrounding whitespace is trimmed on the round trip.
- Two added books are both listed, in the order added, and each keeps its own author.

Each test uses a unique `AddTest-…` title, and an `added_titles` fixture deletes exactly those books afterwards. I checked that no `AddTest` rows remain in the store.

**Verification**
- `pytest -q tests/test_add_book.py`: 27 passed (the committed tests plus the new ones).
- `pytest -q` for the full suite: 141 passed.
- The declared `add-roundtrip-behavior` criterion, run as a standalone script: round-trip ok, exit 0.

**Choices I made**
- The new tests run against the configured store (`DATABASE_URL`, default `data/app.db`), as the spec describes, rather than an isolated temp store like the committed tests use.
- The round trip trims whitespace. I took that from the route's behavior, since the spec doesn't mention it.

**Not in this step:** `bin/test.sh` does not exist yet. `sources/full_test.sh` will report failure until it is built, which belongs to a different step.

RESULT: SUCCESS

FILES CHANGED:
- tests/test_add_book.py

SUMMARY:
Added round-trip pytest tests for POST /books and GET /books to the existing tests/test_add_book.py. The new tests use the web_client fixture, unique titles, and checked cleanup of only the books they created. Declared add-book criteria and the full suite pass (141 tests).

BLOCKERS:
- None for this step. `bin/test.sh` is absent, so `sources/full_test.sh` will fail until it is built in a later step.

<blueprint-decisions>
[{"spec":"FEATURE-AddBookTests.md","severity":"Low","subject":"Store used by the round-trip tests","decision":"The new tests run against the configured store (DATABASE_URL or data/app.db), as the spec's web_client and committed_session guidance describes. Each test removes only the books it created. The existing FEATURE-AddBook tests keep their isolated temp store. Is a shared configured store acceptable, or should these tests move to an isolated store?"}]
</blueprint-decisions>

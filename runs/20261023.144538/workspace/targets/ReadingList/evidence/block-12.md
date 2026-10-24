# Evidence: Block 12 · Service (block-12)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 4546
- execution id: 20261023.151420.658Z-34c16494

## Stories built
- Provide automated pytest tests for removing a book. (test-remove-book) [story]

## Acceptance tooling authorization
- FEATURE-RemoveBookTests.md#remove-tests-module-passes: executable=python3; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 781)
- implements: FEATURE-RemoveBookTests.md (SP 2148)
- context: ARCHITECTURE_compact.md (SP 281)
- context: DATABASE_compact.md (SP 360)

## Build directory changes
- data/app.db
- tests/test_remove_book.py

## Pre-build acceptance observation
- GREEN (prepassed): remove-tests-module-passes (FEATURE-RemoveBookTests.md)
  intent: The remove-book pytest module exists and every test in it passes against the built application.
  return code: 0
  stdout:
    .................                                                        [100%]
    17 passed in 1.00s
- GREEN (prepassed): remove-omits-on-next-read (FEATURE-RemoveBookTests.md)
  intent: A removed book is absent from GET /books on the next read.
  return code: 0
- GREEN (prepassed): remove-preserves-order (FEATURE-RemoveBookTests.md)
  intent: Removing the middle book leaves the other two listed in the order they were added.
  return code: 0
- GREEN (prepassed): remove-unknown-id-404 (FEATURE-RemoveBookTests.md)
  intent: Removing an id that does not exist answers 404.
  return code: 0
- GREEN (prepassed): remove-twice-second-404 (FEATURE-RemoveBookTests.md)
  intent: Removing the same book twice succeeds once and then answers 404.
  return code: 0

## Post-build programmatic acceptance
- PASS: remove-tests-module-passes (FEATURE-RemoveBookTests.md)
  intent: The remove-book pytest module exists and every test in it passes against the built application.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    .............                                                            [100%]
    13 passed in 0.60s
- PASS: remove-omits-on-next-read (FEATURE-RemoveBookTests.md)
  intent: A removed book is absent from GET /books on the next read.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: remove-preserves-order (FEATURE-RemoveBookTests.md)
  intent: Removing the middle book leaves the other two listed in the order they were added.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: remove-unknown-id-404 (FEATURE-RemoveBookTests.md)
  intent: Removing an id that does not exist answers 404.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: remove-twice-second-404 (FEATURE-RemoveBookTests.md)
  intent: Removing the same book twice succeeds once and then answers 404.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
I'll start by inspecting the build directory to see what already exists.A `tests/test_remove_book.py` already exists, so I need to read it before deciding what to change. I'll also read the fixtures and the app code it depends on.The existing module is already substantial and appears to be committed. Next I'll check whether git tracks it, look at the route it exercises, and run it.The module is committed from block 6 and all 17 tests pass. It does not match the block's specification, though. The spec says each test should create books through `POST /books`, read ids back from `GET /books`, use the `web_client` fixture, and that tests reach removal only through the HTTP routes, never the store. The current file uses the service and store directly, including `remove_book` and `database.books.list()`, and runs against a tmp store. I'll rewrite it to match the spec and keep the behaviors it already covers.Now I'll run the rewritten module, then the project's own test command to check nothing else is affected. I'm not touching `sources/full_test.sh`, since no criterion in this block invokes it.The rewritten module passes 13 of 13, and the full project suite passes 137 of 137 with no test residue left in the store. The block also declares four programmatic acceptance criteria. I'll run them against the built app from a scratch directory outside the build tree.The remove-book test module now follows the feature spec, and all declared checks pass. The change is uncommitted, as the build rules require.

I rewrote `tests/test_remove_book.py`. It already existed from block 6 and passed, but it did not match the spec. It called the service and read the store directly, and it used a temporary store rather than the configured one. The new version:

- Uses the `web_client` fixture and reaches removal only through `POST /books/{id}/delete`.
- Creates books through `POST /books`, reads ids back from `GET /books`, and removes its own books at teardown.
- Covers the spec's five behaviors, plus remaining order, remaining id/title/author, a non-integer id, and GET on the delete path returning 405.

Verification:
- `tests/test_remove_book.py`: 13 passed. The earlier version had 17, and the four dropped tests reached the store or service directly.
- Full project suite (`pytest -q`): 137 passed.
- The four declared acceptance checks (omits on next read, preserves order, unknown id 404, second removal 404) all pass when run against the built app.
- No test books are left in the store afterwards.

I did not run `sources/full_test.sh`, since no criterion in this block invokes it.

One thing outside this block: COMPASS requires a POSIX `bin/test.sh`, and the repo only has `bin/run.sh`. I did not add it, because it is not part of this step.

RESULT: SUCCESS

FILES CHANGED:
- tests/test_remove_book.py

SUMMARY:
Rewrote the remove-book pytest module to match FEATURE-RemoveBookTests.md. It exercises removal only through the HTTP routes, using the `web_client` fixture, creates and cleans up its own books, and covers removal, omission on next read, order preservation, unknown id 404, and repeat removal 404. Module: 13 passed. Full project suite: 137 passed. Declared acceptance checks: 4 of 4 pass (run manually from /tmp against the built app; the module check is covered by the 13-pass module run).

<blueprint-decisions>
[{"spec":"FEATURE-RemoveBookTests.md","severity":"Low","subject":"Dropped service-level and store-read tests from tests/test_remove_book.py","decision":"The earlier module called remove_book and read database.books directly, which the spec's guardrail forbids (\"Tests reach removal only through the public HTTP routes, never through the store\"). I removed those four tests and rewrote the rest to use HTTP only. Is that acceptable, or should service-level coverage live in a separate module?"}]
</blueprint-decisions>

BLOCKERS:
- None for this block.

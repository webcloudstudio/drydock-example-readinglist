# Evidence: Block 8 · Service (block-8)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 5320
- execution id: 20261023.150538.609Z-f89307a8

## Stories built
- Reject a submission whose author is empty and report the reason. (reject-empty-author) [story]

## Acceptance tooling authorization
- FEATURE-RejectEmptyAuthor.md#reject-author-empty-json: python-package=pytest; scope=test; authorization=existing Target environment
- FEATURE-RejectEmptyAuthor.md#reject-author-whitespace: python-package=pytest; scope=test; authorization=existing Target environment
- FEATURE-RejectEmptyAuthor.md#reject-author-missing: python-package=pytest; scope=test; authorization=existing Target environment
- FEATURE-RejectEmptyAuthor.md#reject-author-html: python-package=pytest; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 781)
- implements: FEATURE-RejectEmptyAuthor.md (SP 2161)
- context: ARCHITECTURE_compact.md (SP 281)
- context: DATABASE_compact.md (SP 360)
- stack: flask.md (SP 691)

## Build directory changes
- tests/test_reject_empty_author.py

## Pre-build acceptance observation
- GREEN (prepassed): reject-author-empty-json (FEATURE-RejectEmptyAuthor.md)
  intent: An empty author on POST /books answers 400 with a non-empty reason naming the author field and stores nothing.
  return code: 0
- GREEN (prepassed): reject-author-whitespace (FEATURE-RejectEmptyAuthor.md)
  intent: A whitespace-only author is treated as empty, rejected with 400, and nothing is stored.
  return code: 0
- GREEN (prepassed): reject-author-missing (FEATURE-RejectEmptyAuthor.md)
  intent: A POST /books with no author field at all is rejected with 400 and nothing is stored.
  return code: 0
- GREEN (prepassed): reject-author-html (FEATURE-RejectEmptyAuthor.md)
  intent: A browser submission with an empty author is answered 400 with a re-rendered page and nothing is stored.
  return code: 0

## Post-build programmatic acceptance
- PASS: reject-author-empty-json (FEATURE-RejectEmptyAuthor.md)
  intent: An empty author on POST /books answers 400 with a non-empty reason naming the author field and stores nothing.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reject-author-whitespace (FEATURE-RejectEmptyAuthor.md)
  intent: A whitespace-only author is treated as empty, rejected with 400, and nothing is stored.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reject-author-missing (FEATURE-RejectEmptyAuthor.md)
  intent: A POST /books with no author field at all is rejected with 400 and nothing is stored.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reject-author-html (FEATURE-RejectEmptyAuthor.md)
  intent: A browser submission with an empty author is answered 400 with a re-rendered page and nothing is stored.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
The author rejection already appears in `add_book` and the route. Next I'll check the existing tests, whether `bin/test.sh` exists, and what the previous commits changed.The rejection behavior is already in place from earlier blocks. What's missing for this block is a test file that proves the `reject-empty-author` assertions. Before writing it, I'll get a baseline of the existing suite.Baseline is 94 passing. I'll add a test file for this block that follows the same fixture and style as `test_reject_empty_title.py`.All 117 tests pass. Next I'll run the four declared acceptance criteria as written. They run against the configured store (`data/app.db`) through the criteria's own purge and cleanup, so I'll execute them from the project root with the venv interpreter and keep the runner script outside the build tree.Block 8 (reject-empty-author) is done. The author rejection was already in the code from earlier blocks, so this step only added the tests that prove it.

- **Existing behaviour:** `add_book` and the `POST /books` route already reject a missing, empty, or whitespace-only author with status 400, a reason, and `field: author`, and store nothing.
- **New tests:** `tests/test_reject_empty_author.py` adds 23 tests covering the JSON and HTML paths, the absent and whitespace cases, title-first ordering, and nothing stored.
- **Declared criteria:** I ran all four `reject-author-*` criteria from the project root against the configured store. All passed.
- **Suite:** `pytest -q` is green at 117 passed (94 existing plus 23 new).

Not done: `bin/test.sh` does not exist. COMPASS requires it, and `sources/full_test.sh` dispatches to it, so the full scoring gate currently fails. That file isn't part of this block's spec, so I didn't create it. It needs its own step or a foundation fix.

<blueprint-decisions>
[]
</blueprint-decisions>

RESULT: SUCCESS

FILES CHANGED:
- tests/test_reject_empty_author.py

SUMMARY:
Block 8 (reject-empty-author) builds on behaviour already present from earlier blocks: `add_book` in `app_server/book_service.py` and the `POST /books` route in `app_server/books.py` refuse an empty or whitespace-only author with status 400, a non-empty reason, and `field: author`, and store nothing. This step adds `tests/test_reject_empty_author.py` (23 tests) covering JSON and HTML paths, missing and whitespace authors, title-first ordering, earlier books left intact, and the service-level refusal.

Verification:
- Declared criteria `reject-author-empty-json`, `reject-author-whitespace`, `reject-author-missing`, `reject-author-html`: each run from the project root against the configured store with its own purge and cleanup. All PASS.
- `.venv/bin/python -m pytest -q`: 117 passed (94 pre-existing plus 23 new).
- `sources/full_test.sh` was not invoked; no criterion in this block declares it.

BLOCKERS:
- `bin/test.sh` is missing from the application root. COMPASS requires it (POSIX `sh`, exits zero only when all tests pass), and `sources/full_test.sh` dispatches to it, so the release gate fails regardless of this block. It is outside this block's spec, so it was not created here.

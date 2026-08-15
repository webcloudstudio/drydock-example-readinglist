# Evidence: Block 4 · Service (block-4)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 5364
- execution id: 20260815.172624.780Z-f89bc148

## Stories built
- Add and persist a book submitted with a title and author. (book-creation) [story]

## Stacked context
- compass: COMPASS.md (SP 724)
- implements: FEATURE-Book-Creation.md (SP 780)
- context: ARCHITECTURE_compact.md (SP 133)
- context: DATABASE_compact.md (SP 164)
- stack: python_compact.md (SP 1534)
- stack: flask_compact.md (SP 1083)
- stack: sqlite_compact.md (SP 876)

## Build directory changes
- tests/test_routes.py

## Pre-build acceptance observation
- GREEN (prepassed): book-creation-route (FEATURE-Book-Creation.md)
  intent: The book-creation route accepts a submitted title and author and returns a redirect response.
  return code: 0
- GREEN (prepassed): book-creation-readback (FEATURE-Book-Creation.md)
  intent: A successfully submitted book is visible when the list is read again.
  return code: 0
- GREEN (prepassed): book-creation-preserves-existing-order (FEATURE-Book-Creation.md)
  intent: Adding a new book preserves the relative order of books already present.
  return code: 0

## Post-build programmatic acceptance
- PASS: book-creation-route (FEATURE-Book-Creation.md)
  intent: The book-creation route accepts a submitted title and author and returns a redirect response.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: book-creation-readback (FEATURE-Book-Creation.md)
  intent: A successfully submitted book is visible when the list is read again.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: book-creation-preserves-existing-order (FEATURE-Book-Creation.md)
  intent: Adding a new book preserves the relative order of books already present.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- tests/test_routes.py

SUMMARY:
Implemented explicit book-creation acceptance coverage for redirect behavior and insertion-order preservation. Existing `/books` persistence workflow passes all tests.

`sh bin/test.sh`: 20 passed.

BLOCKERS:
- None

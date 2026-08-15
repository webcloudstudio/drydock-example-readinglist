# Evidence: Block 6 · Service (block-6)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 5440
- execution id: 20260815.172854.587Z-8535c0e7

## Stories built
- Remove a selected book from the reading list. (book-removal) [story]

## Stacked context
- compass: COMPASS.md (SP 724)
- implements: FEATURE-Book-Removal.md (SP 864)
- context: ARCHITECTURE_compact.md (SP 133)
- context: DATABASE_compact.md (SP 164)
- stack: python_compact.md (SP 1534)
- stack: flask_compact.md (SP 1083)
- stack: sqlite_compact.md (SP 876)

## Build directory changes
- app/__init__.py
- data/reading_list.db
- tests/test_architecture.py
- tests/test_routes.py

## Pre-build acceptance observation
- GREEN (prepassed): removal-route-reachable (FEATURE-Book-Removal.md)
  intent: The removal route accepts a valid removal request.
  return code: 0
- RED: removal-persists (FEATURE-Book-Removal.md)
  intent: Removing a book makes it absent on the next public list read.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "removal-persists.py", line 14, in <module>
        assert title.encode() not in after.data
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: removal-preserves-remaining-order (FEATURE-Book-Removal.md)
  intent: Removing one book leaves the other books in their original relative order.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "removal-preserves-remaining-order.py", line 20, in <module>
        assert removed_title.encode() not in response.data
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: removal-route-reachable (FEATURE-Book-Removal.md)
  intent: The removal route accepts a valid removal request.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: removal-persists (FEATURE-Book-Removal.md)
  intent: Removing a book makes it absent on the next public list read.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: removal-preserves-remaining-order (FEATURE-Book-Removal.md)
  intent: Removing one book leaves the other books in their original relative order.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- app/__init__.py
- tests/test_architecture.py
- tests/test_routes.py

SUMMARY:
Implemented isolated test databases and added removal regression coverage. All three acceptance scenarios pass. `sh bin/test.sh`: 26 passed.

BLOCKERS:
- None

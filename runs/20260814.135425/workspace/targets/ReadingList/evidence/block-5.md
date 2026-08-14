# Evidence: Block 5 · Service (block-5)

- block type: block
- date: 2026-08-14
- resulting state: closed/verified
- story points (combined assembled cost): 5367
- execution id: 20260814.140810.746Z-680ad2ae

## Stories built
- Preserve addition order and display unread/read status. (reading-list-order-status) [story]

## Stacked context
- compass: COMPASS.md (SP 729)
- implements: FEATURE-OrderAndStatus.md (SP 786)
- context: ARCHITECTURE_compact.md (SP 156)
- context: DATABASE_compact.md (SP 154)
- stack: flask_compact.md (SP 1083)
- stack: python_compact.md (SP 1534)
- stack: sqlite_compact.md (SP 876)

## Build directory changes
- app/templates/reading_list.html
- tests/test_routes.py

## Pre-build acceptance observation
- UNVERIFIED: ordered-books (FEATURE-OrderAndStatus.md)
  intent: The reading-list view presents books in the order supplied by separate additions.
  error: unverified acceptance: acceptance environment unavailable: Target Python project has no .venv
- UNVERIFIED: unread-status (FEATURE-OrderAndStatus.md)
  intent: A newly added book is displayed as unread.
  error: unverified acceptance: acceptance environment unavailable: Target Python project has no .venv
- UNVERIFIED: status-persistence (FEATURE-OrderAndStatus.md)
  intent: A subsequent reading-list request preserves the status value stored for a book.
  error: unverified acceptance: acceptance environment unavailable: Target Python project has no .venv

## Post-build programmatic acceptance
- UNVERIFIED: ordered-books (FEATURE-OrderAndStatus.md)
  intent: The reading-list view presents books in the order supplied by separate additions.
  provisioning: not required
  error: unverified acceptance: acceptance environment unavailable: Target Python project has no .venv
- UNVERIFIED: unread-status (FEATURE-OrderAndStatus.md)
  intent: A newly added book is displayed as unread.
  provisioning: not required
  error: unverified acceptance: acceptance environment unavailable: Target Python project has no .venv
- UNVERIFIED: status-persistence (FEATURE-OrderAndStatus.md)
  intent: A subsequent reading-list request preserves the status value stored for a book.
  provisioning: not required
  error: unverified acceptance: acceptance environment unavailable: Target Python project has no .venv

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- app/templates/reading_list.html
- tests/test_routes.py

SUMMARY:
Implemented explicit unread/read status display while preserving insertion order. Added route tests for unread defaults and persisted read status.

`sh bin/test.sh`: 24 passed.

BLOCKERS:
- None.

# Evidence: Block 5 · Feature (block-5)

- block type: block
- date: 2026-08-10
- resulting state: closed/verified
- story points (combined assembled cost): 3620
- execution id: 20260810.220510.310Z-6c3c46aa

## Stories built
- Add the route and application behavior for marking a selected book as read. (mark-read-route) [story]
- Add persisted read state per book, the corresponding BookStore operations, and migration handling for existing rows. (mark-read-schema) [story]
- Add automated coverage for persisted read state, marking books read, and rendering read and unread states. (mark-read-verification) [story]
- Display each book's unread or read state and provide the mark-read control. (mark-read-view) [story]

## Stacked context
- compass: COMPASS.md (SP 685)
- implements: changes/TICKET-001-Mark-Book-Read.md (SP 292)
- context: ARCHITECTURE_compact.md (SP 109)
- implements: changes/TICKET-002-Mark-Book-Read.md (SP 321)
- context: DATABASE_compact.md (SP 113)
- implements: changes/TICKET-003-Mark-Book-Read.md (SP 365)
- context: FEATURE-Verification.md (SP 589)
- implements: changes/TICKET-004-Mark-Book-Read.md (SP 325)
- context: SCREEN-Reading-List.md (SP 821)

## Build directory changes
- persistence.py
- routes.py
- templates/books.html
- tests/test_acceptance.py

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- persistence.py
- routes.py
- templates/books.html
- tests/test_acceptance.py

SUMMARY:
Implemented persisted read state, legacy migration, mark-read route, UI controls, and automated coverage. `sh bin/test.sh` passes all 29 tests; Ruff passes.

BLOCKERS:
- None

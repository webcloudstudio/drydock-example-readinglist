# Evidence: Block 8 · Service (block-8)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 4413
- execution id: 20260815.173249.820Z-d90fee89

## Stories built
- Assemble the reader-facing form, ordered list, empty state, and removal controls. (reading-list-screen) [story]

## Stacked context
- compass: COMPASS.md (SP 724)
- implements: SCREEN-Reading-List.md (SP 800)
- context: UI-GENERAL_compact.md (SP 204)
- stack: python_compact.md (SP 1534)
- stack: flask_compact.md (SP 1083)

## Build directory changes
- app/templates/index.html
- tests/test_screen.py

## Pre-build acceptance observation
- GREEN (prepassed): screen-loads (SCREEN-Reading-List.md)
  intent: The reading-list screen is reachable at its declared route.
  return code: 0
- GREEN (prepassed): screen-accepts-book-submission (SCREEN-Reading-List.md)
  intent: The screen supports submitting a title and author through the declared creation route.
  return code: 0
- GREEN (prepassed): screen-supports-removal (SCREEN-Reading-List.md)
  intent: The screen supports removing a listed book through the declared removal route.
  return code: 0
- GREEN (prepassed): screen-supports-empty-state (SCREEN-Reading-List.md)
  intent: The screen responds successfully when the reading list is empty.
  return code: 0

## Post-build programmatic acceptance
- PASS: screen-loads (SCREEN-Reading-List.md)
  intent: The reading-list screen is reachable at its declared route.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: screen-accepts-book-submission (SCREEN-Reading-List.md)
  intent: The screen supports submitting a title and author through the declared creation route.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: screen-supports-removal (SCREEN-Reading-List.md)
  intent: The screen supports removing a listed book through the declared removal route.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: screen-supports-empty-state (SCREEN-Reading-List.md)
  intent: The screen responds successfully when the reading list is empty.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- app/templates/index.html
- tests/test_screen.py

SUMMARY:
Implemented the reader-facing screen accessibility refinement and explicit acceptance tests for loading, submission, removal, and empty state. Full suite: 36 passed. Ruff checks passed.

BLOCKERS:
- None

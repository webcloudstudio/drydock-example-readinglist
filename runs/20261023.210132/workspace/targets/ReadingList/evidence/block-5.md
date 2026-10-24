# Evidence: Block 5 · Service (block-5)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 2577
- execution id: 20261023.211144.220Z-18305c12

## Stories built
- Assemble the primary reading-list page and interactions. (reading-list-screen) [story]

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 551)
- implements: SCREEN-ReadingList.md (SP 918)
- stack: flask.md (SP 451)

## Build directory changes
- app_server/templates/reading_list/index.html
- data/app.db
- tests/test_reading_list_screen.py

## Pre-build acceptance observation
- GREEN (prepassed): reading-list-screen-load (SCREEN-ReadingList.md)
  intent: The primary reading-list screen is reachable and returns a successful response.
  return code: 0
- GREEN (prepassed): reading-list-screen-add (SCREEN-ReadingList.md)
  intent: The primary screen accepts a book submission and renders the supplied book after the workflow completes.
  return code: 0
- GREEN (prepassed): reading-list-screen-remove (SCREEN-ReadingList.md)
  intent: The primary screen removes a selected book and omits it from the subsequent list response.
  return code: 0

## Post-build programmatic acceptance
- PASS: reading-list-screen-load (SCREEN-ReadingList.md)
  intent: The primary reading-list screen is reachable and returns a successful response.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reading-list-screen-add (SCREEN-ReadingList.md)
  intent: The primary screen accepts a book submission and renders the supplied book after the workflow completes.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reading-list-screen-remove (SCREEN-ReadingList.md)
  intent: The primary screen removes a selected book and omits it from the subsequent list response.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- app_server/templates/reading_list/index.html
- tests/test_reading_list_screen.py

SUMMARY:
Added accessible invalid-field feedback and focused screen tests. All tests and 3 screen acceptance checks pass.

BLOCKERS:
- None

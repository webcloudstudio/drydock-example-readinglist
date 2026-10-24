# Evidence: Block 3 · Foundational (block-3)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 2157
- execution id: 20261023.210648.884Z-a36997d1

## Stories built
- Define the shared server-rendered interface patterns. (ui-general) [story]

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 551)
- implements: UI-GENERAL.md (SP 507)
- stack: flask.md (SP 451)

## Build directory changes
- app_server/__init__.py
- app_server/features/reading_list/routes.py
- app_server/static/reading-list.css
- app_server/templates/reading_list/index.html
- instance/readinglist.sqlite3
- tests/test_architecture.py

## Pre-build acceptance observation
- GREEN (prepassed): ui-general-client (UI-GENERAL.md)
  intent: The shared interface is available through the application's published testing client.
  return code: 0
- RED: ui-general-form (UI-GENERAL.md)
  intent: The primary interface accepts the declared book form fields.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "ui-general-form.py", line 11, in <module>
        assert response.status_code in (200, 302, 303)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: ui-general-client (UI-GENERAL.md)
  intent: The shared interface is available through the application's published testing client.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: ui-general-form (UI-GENERAL.md)
  intent: The primary interface accepts the declared book form fields.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- app_server/__init__.py
- app_server/features/reading_list/routes.py
- app_server/templates/reading_list/index.html
- app_server/static/reading-list.css
- tests/test_architecture.py

SUMMARY:
Implemented the server-rendered reading-list interface with accessible forms, validation feedback, empty state, insertion-order display, add/remove actions, styling, and tests. All tests passed.

BLOCKERS:
- None

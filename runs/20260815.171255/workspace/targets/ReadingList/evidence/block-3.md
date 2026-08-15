# Evidence: Block 3 · Foundational (block-3)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 4166
- execution id: 20260815.172349.042Z-3e42d88f

## Stories built
- Define shared presentation patterns for the reading-list interface. (ui-general) [story]

## Reusable compacts
- UI-GENERAL_compact.md

## Stacked context
- compass: COMPASS.md (SP 724)
- implements: UI-GENERAL.md (SP 759)
- stack: python_compact.md (SP 1534)
- stack: flask_compact.md (SP 1083)

## Build directory changes
- app/routes.py
- app/static/css/style.css
- app/templates/index.html
- tests/test_routes.py

## Pre-build acceptance observation
- RED: ui-patterns-form (UI-GENERAL.md)
  intent: The shared presentation includes labeled title and author controls and a submission control.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "ui-patterns-form.py", line 8, in <module>
        assert 'name="title"' in body
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): ui-patterns-empty-state (UI-GENERAL.md)
  intent: The shared presentation provides a reader-visible empty-list state.
  return code: 0
- RED: ui-patterns-removal-control (UI-GENERAL.md)
  intent: The shared presentation provides a removal control for a listed book.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "ui-patterns-removal-control.py", line 8, in <module>
        assert response.status_code in (302, 303)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: ui-patterns-form (UI-GENERAL.md)
  intent: The shared presentation includes labeled title and author controls and a submission control.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: ui-patterns-empty-state (UI-GENERAL.md)
  intent: The shared presentation provides a reader-visible empty-list state.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: ui-patterns-removal-control (UI-GENERAL.md)
  intent: The shared presentation provides a removal control for a listed book.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
<reusable-compact filename="UI-GENERAL.md">
- Single responsive reading-list screen with heading, required title/author form, submit control, ordered book list, per-book removal controls, empty state, and visible validation errors.
- Controls require labels and stable names; removal targets must use book identity, not position.
- Preserve insertion order and display understandable missing-field errors.
- CSS must provide readable typography, focus states, contrast, spacing, and responsive narrow-screen layout.
- Acceptance: GET `/` includes `name="title"`, `name="author"`, and a form; empty state mentions reading plus empty/no books; POST `/books` then GET `/` shows title, author, and removal control.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- app/routes.py
- app/templates/index.html
- app/static/css/style.css
- tests/test_routes.py

SUMMARY:
Implemented the accessible reading-list presentation, add/remove routes, validation alert, empty state, responsive styling, and acceptance-focused tests. Full suite passes: 18 tests. Ruff checks pass.

BLOCKERS:
- None.

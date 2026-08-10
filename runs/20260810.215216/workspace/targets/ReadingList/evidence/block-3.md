# Evidence: Block 3 · Service (block-3)

- block type: block
- date: 2026-08-10
- resulting state: closed/verified
- story points (combined assembled cost): 4607
- execution id: 20260810.220149.657Z-5901d6a0

## Stories built
- Present the reading-list entry point and available book actions. (reading-list-screen) [story]

## Acceptance tooling authorization
- SCREEN-Reading-List.md#renders-empty-list: python-package=flask; scope=test; authorization=existing Target dependency manifest

## Stacked context
- compass: COMPASS.md (SP 685)
- implements: SCREEN-Reading-List.md (SP 821)
- context: UI-GENERAL_compact.md (SP 94)
- context: FEATURE-Add-Book_compact.md (SP 97)
- context: FEATURE-List-Books_compact.md (SP 68)
- context: FEATURE-Validate-Book_compact.md (SP 75)
- context: FEATURE-Remove-Book_compact.md (SP 89)
- stack: python_compact.md (SP 1534)
- stack: flask_compact.md (SP 1083)

## Build directory changes
- routes.py
- tests/test_acceptance.py

## Pre-build acceptance observation
- RED: renders-empty-list (SCREEN-Reading-List.md)
  intent: The primary entry point is reachable and renders the empty-list state.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: renders-added-book (SCREEN-Reading-List.md)
  intent: A book added through the user workflow appears on the primary screen.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: submits-book-form (SCREEN-Reading-List.md)
  intent: The screen's add interaction calls the declared creation route.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: submits-remove-control (SCREEN-Reading-List.md)
  intent: The screen's remove interaction calls the declared removal route.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: renders-validation-error (SCREEN-Reading-List.md)
  intent: An invalid screen submission returns to a state containing a user-facing error.
  error: baseline unavailable: authorized Target tooling is not provisioned

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- routes.py
- tests/test_acceptance.py

SUMMARY:
- Wired `POST /` to add books through the existing workflow.
- Added screen acceptance tests for rendering, adding, removing, and validation.
- Full suite: 21 passed.
- Ruff checks passed.

BLOCKERS:
- None

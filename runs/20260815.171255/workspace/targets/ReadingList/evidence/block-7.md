# Evidence: Block 7 · Service (block-7)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 4439
- execution id: 20260815.173115.893Z-f187318d

## Stories built
- Reject submissions missing a title or author with a clear error. (incomplete-submission) [story]

## Stacked context
- compass: COMPASS.md (SP 724)
- implements: FEATURE-Incomplete-Submission.md (SP 731)
- context: ARCHITECTURE_compact.md (SP 133)
- context: DATABASE_compact.md (SP 164)
- stack: python_compact.md (SP 1534)
- stack: flask_compact.md (SP 1083)

## Build directory changes
- tests/test_routes.py

## Pre-build acceptance observation
- GREEN (prepassed): validation-rejects-empty-title (FEATURE-Incomplete-Submission.md)
  intent: A submission with an empty title is rejected with a client validation response.
  return code: 0
- GREEN (prepassed): validation-rejects-empty-author (FEATURE-Incomplete-Submission.md)
  intent: A submission with an empty author is rejected with a client validation response.
  return code: 0
- GREEN (prepassed): validation-does-not-persist-invalid-submission (FEATURE-Incomplete-Submission.md)
  intent: Invalid submissions do not appear in the public list.
  return code: 0
- GREEN (prepassed): validation-preserves-valid-submission (FEATURE-Incomplete-Submission.md)
  intent: A valid submission remains supported by the creation workflow.
  return code: 0

## Post-build programmatic acceptance
- PASS: validation-rejects-empty-title (FEATURE-Incomplete-Submission.md)
  intent: A submission with an empty title is rejected with a client validation response.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validation-rejects-empty-author (FEATURE-Incomplete-Submission.md)
  intent: A submission with an empty author is rejected with a client validation response.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validation-does-not-persist-invalid-submission (FEATURE-Incomplete-Submission.md)
  intent: Invalid submissions do not appear in the public list.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validation-preserves-valid-submission (FEATURE-Incomplete-Submission.md)
  intent: A valid submission remains supported by the creation workflow.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- tests/test_routes.py

SUMMARY:
Added coverage for missing title, missing author, both missing, non-persistence, and valid submissions. Full suite: 32 passed. All declared acceptance checks passed.

BLOCKERS:
- None

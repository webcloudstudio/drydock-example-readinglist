# Evidence: Block 4 · Service (block-4)

- block type: block
- date: 2026-08-10
- resulting state: closed/verified
- story points (combined assembled cost): 3669
- execution id: 20260810.220314.394Z-0f058337

## Stories built
- Provide the complete POSIX automated test runner. (verification) [story]

## Acceptance tooling authorization
- FEATURE-Verification.md#complete-suite-run: executable=sh; scope=test; authorization=existing Target environment
- FEATURE-Verification.md#complete-suite-run: python-package=pytest; scope=test; authorization=existing Target dependency manifest

## Stacked context
- compass: COMPASS.md (SP 685)
- implements: FEATURE-Verification.md (SP 589)
- context: SEA_TRIALS.md (SP 558)
- context: ARCHITECTURE_compact.md (SP 109)
- context: DATABASE_compact.md (SP 113)
- stack: python_compact.md (SP 1534)

## Build directory changes
- bin/test.sh
- tests/test_verification.py

## Pre-build acceptance observation
- RED: complete-suite-run (FEATURE-Verification.md)
  intent: The complete automated test suite passes through the required POSIX runner.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: runner-is-posix-invocable (FEATURE-Verification.md)
  intent: The runner can be invoked from the application root using POSIX `sh`.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: suite-covers-book-behaviors (FEATURE-Verification.md)
  intent: The test suite contains executable coverage for each required book behavior.
  error: baseline unavailable: authorized Target tooling is not provisioned

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- bin/test.sh
- tests/test_verification.py

SUMMARY:
Updated the POSIX runner to preserve pytest’s exit status and output. Added runner contract tests. Full suite passes: 23 tests.

BLOCKERS:
- None

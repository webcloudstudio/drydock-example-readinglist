# Evidence: Block 5 · Feature (block-5)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 2657
- execution id: 20261014.053057.570Z-4b066be4

## Stories built
- Provide POSIX bin/test.sh that runs the complete automated suite and is the terminal verification gate. (feature-test-runner) [story]

## Stacked context
- compass: COMPASS.md (SP 833)
- implements: FEATURE-TestRunner.md (SP 818)
- context: ARCHITECTURE_compact.md (SP 261)
- context: DATABASE_compact.md (SP 272)
- stack: python_compact.md (SP 390)

## Build directory changes
- bin/test.sh
- tests/test_test_runner.py

## Pre-build acceptance observation
- RED: test-runner-posix-syntax (FEATURE-TestRunner.md)
  intent: bin/test.sh parses as POSIX sh.
  return code: 1
  stdout:
    sh: 0: cannot open bin/test.sh: No such file
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['sh', '-n', 'bin/test.sh'], returncode=2, stdout='', stderr='sh: 0: cannot open bin/test.sh: No such file\n')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "test-runner-posix-syntax.py", line 6, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: test-runner-full-suite (FEATURE-TestRunner.md)
  intent: The complete automated suite runs unfiltered through sh bin/test.sh and exits zero only when every test passes.
  return code: 1
  stderr:
    sh: 0: cannot open bin/test.sh: No such file
    
    --- drydock: values at failure ---
      result = CompletedProcess(args=['sh', 'bin/test.sh'], returncode=2, stdout='', stderr='sh: 0: cannot open bin/test.sh: No such file\n')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "test-runner-full-suite.py", line 7, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: test-runner-posix-syntax (FEATURE-TestRunner.md)
  intent: bin/test.sh parses as POSIX sh.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: test-runner-full-suite (FEATURE-TestRunner.md)
  intent: The complete automated suite runs unfiltered through sh bin/test.sh and exits zero only when every test passes.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    ........................................................................ [ 91%]
    .......                                                                  [100%]

## Build summary
Now I'll write the runner, which is a thin POSIX wrapper around the full pytest suite.Next, tests for the runner itself. They read back the exit status of the script run in isolated temp copies, so the script never recurses into this file.The last test I wrote is redundant and its parameter is unused, so I'll remove it.Now I'll make the script executable and run the two declared acceptance checks exactly as specified, plus the full gate.RESULT: SUCCESS

FILES CHANGED:
- bin/test.sh
- tests/test_test_runner.py

SUMMARY:
- `bin/test.sh` is a POSIX `sh` script. It resolves the application root from its own location, `cd`s there, and exits nonzero with a message if `.venv/bin/python` is missing. Otherwise it `exec`s `.venv/bin/python -m pytest -q`, so the suite's exit status is the script's exit status. It runs the full suite with no filtering.
- `tests/test_test_runner.py` has 5 tests. Each one copies the script into its own temp application root, so the nested suite never re-enters this file and nothing is left in the build directory:
  - the script parses under `sh -n`
  - it exits nonzero when `.venv` is missing
  - it exits zero when every test passes
  - it exits nonzero when any test fails
  - it works when invoked from a different working directory
- Acceptance checks, run as declared:
  - `test-runner-posix-syntax` (`sh -n bin/test.sh`): exit 0.
  - `test-runner-full-suite` (`sh bin/test.sh`): exit 0.
- Suite counts: the full gate ran 79 tests (74 existing plus 5 new), all passed. The new runner tests were also run on their own and passed.
- `sources/full_test.sh` was not modified and not run. Its contents just dispatch to `sh bin/test.sh`, which is what the acceptance check exercised.
- I made `bin/test.sh` executable so it can run directly. Nothing was staged or committed.

Choices I made:
- The error message for a missing `.venv` points to `uv venv` and `uv sync`. The spec didn't name a setup command.
- The runner tests use a symlink to the project's `.venv` inside each temp root, so they don't create a second environment.

BLOCKERS:
- None.

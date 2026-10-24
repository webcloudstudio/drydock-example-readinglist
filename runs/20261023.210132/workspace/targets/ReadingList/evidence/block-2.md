# Evidence: Block 2 · Foundational (block-2)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 7501
- execution id: -

## Stories built
- Provide relational persistence for ordered books. (database) [story]

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 551)
- implements: DATABASE.md (SP 1361)
- stack: persistence.md (SP 2816)
- stack: sqlite.md (SP 2109)

## Pre-build acceptance observation
- RED: database-books-create (DATABASE.md)
  intent: The books create operation returns the declared book row with the supplied values.
  error: foundation not built: `persistence` is the package the database foundation (postgres.md, sqlite.md) builds, and the build directory has no `persistence/`. The criterion exercises the built application, so it was not run.
- RED: database-books-list (DATABASE.md)
  intent: The books list operation returns books in insertion order.
  error: foundation not built: `persistence` is the package the database foundation (postgres.md, sqlite.md) builds, and the build directory has no `persistence/`. The criterion exercises the built application, so it was not run.
- RED: database-books-delete (DATABASE.md)
  intent: The books delete operation returns the selected identifier and removes that book from subsequent reads.
  error: foundation not built: `persistence` is the package the database foundation (postgres.md, sqlite.md) builds, and the build directory has no `persistence/`. The criterion exercises the built application, so it was not run.

## Post-build programmatic acceptance
- PASS: database-books-create (DATABASE.md)
  intent: The books create operation returns the declared book row with the supplied values.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not requested
  return code: 0
- PASS: database-books-list (DATABASE.md)
  intent: The books list operation returns books in insertion order.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not requested
  return code: 0
- PASS: database-books-delete (DATABASE.md)
  intent: The books delete operation returns the selected identifier and removes that book from subsequent reads.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not requested
  return code: 0

## Build summary
(no summary returned)

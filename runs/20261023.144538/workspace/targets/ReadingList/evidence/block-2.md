# Evidence: Block 2 · Foundational (block-2)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 11423
- execution id: -

## Stories built
- Declare and provision the books table and its repository operations. (database) [story]

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 781)
- implements: DATABASE.md (SP 2302)
- stack: persistence.md (SP 4315)
- stack: sqlite.md (SP 3027)

## Pre-build acceptance observation
- RED: books-create (DATABASE.md)
  intent: Creating a book returns a row carrying the supplied title and author and an assigned id.
  error: foundation not built: `persistence` is the package the database foundation (postgres.md, sqlite.md) builds, and the build directory has no `persistence/`. The criterion exercises the built application, so it was not run.
- RED: books-get (DATABASE.md)
  intent: A created book can be read back by id with the supplied title and author.
  error: foundation not built: `persistence` is the package the database foundation (postgres.md, sqlite.md) builds, and the build directory has no `persistence/`. The criterion exercises the built application, so it was not run.
- RED: books-list-order (DATABASE.md)
  intent: Listing returns books in the order they were created.
  error: foundation not built: `persistence` is the package the database foundation (postgres.md, sqlite.md) builds, and the build directory has no `persistence/`. The criterion exercises the built application, so it was not run.
- RED: books-delete (DATABASE.md)
  intent: A deleted book is absent from the list on the next read and other books remain.
  error: foundation not built: `persistence` is the package the database foundation (postgres.md, sqlite.md) builds, and the build directory has no `persistence/`. The criterion exercises the built application, so it was not run.

## Post-build programmatic acceptance
- PASS: books-create (DATABASE.md)
  intent: Creating a book returns a row carrying the supplied title and author and an assigned id.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not requested
  return code: 0
- PASS: books-get (DATABASE.md)
  intent: A created book can be read back by id with the supplied title and author.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not requested
  return code: 0
- PASS: books-list-order (DATABASE.md)
  intent: Listing returns books in the order they were created.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not requested
  return code: 0
- PASS: books-delete (DATABASE.md)
  intent: A deleted book is absent from the list on the next read and other books remain.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not requested
  return code: 0

## Build summary
(no summary returned)

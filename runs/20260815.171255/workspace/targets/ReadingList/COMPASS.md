# COMPASS: ReadingList

## Compass
ReadingList is a small web application for readers who want to maintain a personal, ordered list of books to read. A reader can add a book with its title and author, review books in insertion order, and remove books when they are no longer needed.

## Constraints
- The application must run as a web application.
- Book submissions require both a title and an author.
- Books must be shown in the order they were added.
- `bin/test.sh` must be POSIX-compatible and run from the application root.
- The complete automated test suite must pass for `bin/test.sh` to exit zero.

## Guardrails
- Never accept or store a submission with an empty title or author.
- Never reorder books relative to their addition order.
- Never report the test command as successful when any automated test fails.
- Always provide a clear reason when rejecting incomplete input.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/workspace/targets/ReadingList`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/workspace/targets/ReadingList/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/workspace/targets/ReadingList/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/workspace/targets/ReadingList/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/workspace/targets/ReadingList/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/workspace/targets/ReadingList/evidence/`
<!-- drydock:build-write-guardrail:end -->

<!-- Drydock author intent sha256=c86a1a56f7d25ca5548192dbe12c57989f5b1ddd34835753e64e7deb83845e3a source=reading-list.md -->

# Reading List

Build a web application that keeps a list of books to read.

The reader can add a book with a title and author, view the books in the order added,
and remove a book. An empty title or author is rejected with a clear error message.

The application includes automated tests for each behavior.

The completed application provides a POSIX-compatible `bin/test.sh` that runs the complete
automated test suite from the application root. `sh bin/test.sh` exits zero only when every test
passes. The final build story runs this command after every implementation story and preserves its
command, exit code, standard output, and standard error as evidence.

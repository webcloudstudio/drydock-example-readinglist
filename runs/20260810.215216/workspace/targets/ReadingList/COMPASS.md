# COMPASS: ReadingList

## Compass
ReadingList is a web application for readers who want to maintain a personal list of books to read. It lets a reader add books with titles and authors, view them in insertion order, and remove them.

## Constraints
- Provide a POSIX-compatible `bin/test.sh`.
- The complete automated suite must run from the application root.
- `sh bin/test.sh` exits zero only when every test passes.
- Preserve test-run command, exit code, stdout, and stderr as evidence.

## Guardrails
- Reject empty titles and authors with a clear reason.
- Preserve insertion order when displaying books.
- Never transmit a reader’s list to a third-party service.
- Keep add, view, and remove flows usable without instructions.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260810.215216/build/ReadingList`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260810.215216/workspace/targets/ReadingList`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260810.215216/workspace/targets/ReadingList/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260810.215216/workspace/targets/ReadingList/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260810.215216/workspace/targets/ReadingList/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260810.215216/workspace/targets/ReadingList/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260810.215216/workspace/targets/ReadingList/evidence/`
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

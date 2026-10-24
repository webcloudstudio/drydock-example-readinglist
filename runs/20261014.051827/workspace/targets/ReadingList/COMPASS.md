# COMPASS: ReadingList

## Compass
A small web application that keeps a reader's list of books to read. A reader adds a book with a title and author, views the books in the order added, and removes books. It exists so the reader can track what to read next without losing order or accepting incomplete entries.

## Constraints
- The completed application must provide a POSIX-compatible `bin/test.sh` at the application root.
- `sh bin/test.sh` must run the complete automated test suite and exit zero only when every test passes.
- The final build story runs `sh bin/test.sh` after every implementation story and preserves its command, exit code, standard output, and standard error as evidence.

## Guardrails
- Never accept an empty title or an empty author.
- Never present books in an order other than the order they were added.
- Never report a passing test suite while any automated test fails.
- Never ship without automated tests covering each behavior.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/workspace/targets/ReadingList`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/workspace/targets/ReadingList/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/workspace/targets/ReadingList/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/workspace/targets/ReadingList/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/workspace/targets/ReadingList/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/workspace/targets/ReadingList/evidence/`
<!-- drydock:build-write-guardrail:end -->

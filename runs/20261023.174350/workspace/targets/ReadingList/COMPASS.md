# COMPASS: ReadingList

## Compass
A web application that lets a reader keep a personal list of books to read. The reader adds a book with a title and author, views books in the order they were added, and removes books. It serves a single reader who needs a simple, dependable reading list with clear feedback on invalid input.

## Constraints
- The application is a web application with a user-facing interface.
- The completed application must provide a POSIX-compatible `bin/test.sh` runnable from the application root with `sh bin/test.sh`.
- `bin/test.sh` must exit zero only when every automated test passes.
- The final build story runs `bin/test.sh` after every implementation story and preserves its command, exit code, stdout, and stderr as evidence.

## Guardrails
- Never accept an empty title or an empty author; reject the submission with a clear error message.
- Never present books in any order other than the order they were added.
- Never report a test run as passing unless every automated test passes.
- Never omit a removed book from the next list read only partially; a removed book must not reappear.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/workspace/targets/ReadingList`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/workspace/targets/ReadingList/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/workspace/targets/ReadingList/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/workspace/targets/ReadingList/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/workspace/targets/ReadingList/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/workspace/targets/ReadingList/evidence/`
<!-- drydock:build-write-guardrail:end -->

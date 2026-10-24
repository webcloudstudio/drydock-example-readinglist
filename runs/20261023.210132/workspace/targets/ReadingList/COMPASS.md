# COMPASS: ReadingList

## Compass

ReadingList is a small web application for readers who want to maintain a personal list of books to read. A reader can add books with titles and authors, view them in insertion order, and remove them. The application must be easy to exercise through its primary web page and fully verifiable through its supplied test runner.

## Constraints

- The delivered `bin/test.sh` must be POSIX-compatible.
- `sh bin/test.sh` is the complete automated test command.
- The test runner must exit zero only when every automated test passes.
- Use local relational persistence suitable for repeatable automated tests.
- Preserve the order in which books are added.

## Guardrails

- Never store or display a book with an empty title or author.
- Always report a clear reason when validation rejects a submission.
- Never silently reorder books.
- After removal, do not show the removed book on the next read.
- Keep every described behavior covered by automated tests.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.210132/build/ReadingList`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.210132/workspace/targets/ReadingList`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.210132/workspace/targets/ReadingList/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.210132/workspace/targets/ReadingList/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.210132/workspace/targets/ReadingList/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.210132/workspace/targets/ReadingList/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.210132/workspace/targets/ReadingList/evidence/`
<!-- drydock:build-write-guardrail:end -->

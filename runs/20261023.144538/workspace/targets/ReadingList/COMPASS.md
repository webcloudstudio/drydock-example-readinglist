# COMPASS: ReadingList

## Compass
A reader-facing web application for keeping an ordered list of books to read. Each book has a title and an author. Readers add, view in insertion order, and remove books. The product exists so a reader can track what they intend to read without losing track of the order they added titles.

## Constraints
- The application root must contain a POSIX-compatible `bin/test.sh` runnable with `sh`.
- `bin/test.sh` must exit zero only when every automated test passes.
- The complete automated test suite must run from the application root.

## Guardrails
- Never accept an empty title or an empty author.
- Never present books in any order other than the order added.
- Never omit a rejection reason when a submission is rejected.
- Never ship a behavior without an automated test covering it.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/workspace/targets/ReadingList`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/workspace/targets/ReadingList/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/workspace/targets/ReadingList/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/workspace/targets/ReadingList/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/workspace/targets/ReadingList/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/workspace/targets/ReadingList/evidence/`
<!-- drydock:build-write-guardrail:end -->

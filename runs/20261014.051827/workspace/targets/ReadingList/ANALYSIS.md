# Blueprint Analysis: ReadingList

## Commander Expectations

- assert the product lets a reader add a book with a title and an author
- assert the product shows books in the order they were added
- assert the product lets a reader remove a book
- assert an empty title or author is rejected with a clear error message
- assert the product includes automated tests for each behavior
- assert the completed application provides a POSIX-compatible `bin/test.sh` that runs the complete automated test suite from the application root and exits zero only when every test passes

## Crew

| Crew | Charge |
|---|---|
| Commander | Defines intent and decides what done means. |
| Team Lead | Confirms epic completeness and stakeholder expectations. |
| Planning Crew | Authors atomic specifications and the ordered Manifest. |
| Shipyard Crew | Builds the tickets without synchronous Commander access. |

## Story List

### Feature: Book List Management

| ID | Story | High-level AC |
|---|---|---|
| BOOKS-001 | Add a book with title and author | Submitting a title and an author stores the book and shows it in the list |
| BOOKS-002 | Reject a submission with an empty title or author | An empty title or empty author is rejected and the reason is reported |
| BOOKS-003 | List books in the order added | Books are presented in insertion order |
| BOOKS-004 | Remove a book from the list | A removed book is omitted from the list on the next read |

### Feature: Test Coverage and Verification

| ID | Story | High-level AC |
|---|---|---|
| TEST-001 | Automated tests cover adding a book | An automated test exercises the add behavior |
| TEST-002 | Automated tests cover listing books in order added | An automated test exercises the ordering behavior |
| TEST-003 | Automated tests cover removing a book | An automated test exercises the remove behavior |
| TEST-004 | Automated tests cover rejecting an empty title or author | An automated test exercises the rejection behavior |
| TEST-005 | Provide POSIX-compatible `bin/test.sh` runner | `sh bin/test.sh` runs the complete automated test suite from the application root and exits zero only when every test passes |

## Story Guidance

Named stories planning must produce. Authoritative record: `STORY_GUIDANCE.json`.

None.

## Surfaced Acceptance Criteria

| ID | Story ID | Criterion |
|---|---|---|
| AC-001 | BOOKS-002 | The rejection message names the failing field (title or author) |
| AC-002 | BOOKS-004 | Removing a book that is not in the list is reported without altering the list |

## Source Inventory

| Path | Content kind | Disposition | Reason |
|---|---|---|---|
| `sources/full_test.sh` | code | analyzed | readable UTF-8 |
| `sources/reading-list.md` | markdown | analyzed | readable UTF-8 |

## Relationship Model

| Source or group | Relationship type | Related source or group | Evidence | Delivery implication |
|---|---|---|---|---|
| sources/full_test.sh | test-kit-to-implementation | bin/test.sh | `sources/full_test.sh` checks for `bin/test.sh` at the application root and execs it | The application must supply `bin/test.sh`; the harness reports its absence as failure |
| sources/reading-list.md | instruction-to-test | TEST-005 | `reading-list.md` requires `sh bin/test.sh` to exit zero only when every test passes | TEST-005 gates on the complete suite |
| sources/reading-list.md | dependency | BOOKS-001..004 | `reading-list.md` lists add, order, remove, and reject behaviors | Each behavior has a paired test story (TEST-001..004) |

## Source Roles

| Path | Role | Plan disposition | Build disposition |
|---|---|---|---|
| sources/reading-list.md | author intent | compass | prompt-only |
| sources/full_test.sh | conformance harness | context | stage |

## Planning Instructions

### Delivery Shape

The system is a web application that keeps a reading list. Inputs are a reader's submitted title and author, and removal requests. Outputs are the rendered ordered list and validation errors. The required execution flow is: the application is built, then `sh bin/test.sh` runs from the application root, and `sources/full_test.sh` acts as the scoring entry point that delegates to it.

### Story Realization Map

- BOOKS-001: add behavior. Evidence: `sources/reading-list.md` ("add a book with a title and author"). Requires a persistence capability and a submission route/screen.
- BOOKS-002: rejection of empty fields. Evidence: `sources/reading-list.md` ("An empty title or author is rejected with a clear error message"). Requires validation and an error display.
- BOOKS-003: ordering. Evidence: `sources/reading-list.md` ("view the books in the order added"). Requires stable insertion ordering in the store and list view.
- BOOKS-004: removal. Evidence: `sources/reading-list.md` ("remove a book"). Requires a removal route/screen and persistence.
- TEST-001..004: focused automated tests, one per behavior. Evidence: `sources/reading-list.md` ("automated tests for each behavior").
- TEST-005: POSIX runner `bin/test.sh` and terminal full-suite verification. Evidence: `sources/reading-list.md`, `sources/full_test.sh`. Requires the test harness capability.

### Test and Acceptance Strategy

Focused story tests run the slice each story owns and declare `Suite: scoped`. TEST-005 is the single terminal verification story. It depends on every implementation and test story, and its acceptance assertion declares `Suite: full`, running `sh bin/test.sh` unfiltered and requiring exit zero. Sea Trial st-001 proves the same complete-suite requirement.

### Sequencing and Dependencies

- BOOKS-001 precedes BOOKS-002 and BOOKS-003 (the list must hold stored books before validation and ordering are observable).
- BOOKS-003 precedes BOOKS-004 (removal is observed through the ordered list).
- Each TEST-00n follows its BOOKS story.
- TEST-005 follows every implementation and test story.

### Source Conflicts and Gaps

- None. The sources do not contain conflicting definitions. Stack and persistence choices are proposed in `TECHNOLOGY_STACK.md` and do not block planning.

## Analysis Notes
generated: 2026-10-14
blueprint: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/workspace/targets/ReadingList/blueprint

Quality: Ready
  blockers: 0
  questions: 0
  features: 2
  stories: 9
  stack: not declared
  display_name: ReadingList
  short_description: not proposed
  
None.

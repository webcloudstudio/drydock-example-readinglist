# Blueprint Analysis: ReadingList

## Commander Expectations

- assert the product lets a reader add a book with a title and an author
- assert the product lists books in the order they were added
- assert the product lets a reader remove a book
- assert an empty title or author is rejected with a clear error message
- assert the product ships automated tests covering each behavior
- assert the product provides a POSIX-compatible `bin/test.sh` that runs the complete automated test suite from the application root

## Crew

| Crew | Charge |
|---|---|
| Commander | Defines intent and decides what done means. |
| Team Lead | Confirms epic completeness and stakeholder expectations. |
| Planning Crew | Authors atomic specifications and the ordered Manifest. |
| Shipyard Crew | Builds the tickets without synchronous Commander access. |

## Story List

### Feature: Book List

| ID | Story | High-level AC |
|---|---|---|
| BOOK-LIST-001 | Add a book with title and author | Submitting a title and author stores the book and shows it in the list |
| BOOK-LIST-002 | Reject a submission with an empty title or author | Empty title or author is rejected and the reason is reported |
| BOOK-LIST-003 | View books in the order added | Books are presented in insertion order |
| BOOK-LIST-004 | Remove a book from the list | A removed book is omitted from the list on the next read |

### Feature: Test Coverage

| ID | Story | High-level AC |
|---|---|---|
| TEST-COVERAGE-001 | Automated tests for adding a book | Tests exist for the add-book behavior |
| TEST-COVERAGE-002 | Automated tests for listing books in order added | Tests exist for the ordering behavior |
| TEST-COVERAGE-003 | Automated tests for removing a book | Tests exist for the removal behavior |
| TEST-COVERAGE-004 | Automated tests for rejecting empty title or author | Tests exist for the empty-field rejection behavior |
| TEST-COVERAGE-005 | Application-root POSIX test runner `bin/test.sh` | `sh bin/test.sh` runs the complete automated suite and exits zero only when every test passes |

## Story Guidance

Named stories planning must produce. Authoritative record: `STORY_GUIDANCE.json`.

None.

## Surfaced Acceptance Criteria

| ID | Story ID | Criterion |
|---|---|---|
| AC-001 | BOOK-LIST-001 | The application shall store the submitted title and author and display the new book in the list |
| AC-002 | BOOK-LIST-002 | If the title is empty, then the application shall reject the submission and report a clear error message |
| AC-003 | BOOK-LIST-002 | If the author is empty, then the application shall reject the submission and report a clear error message |
| AC-004 | BOOK-LIST-003 | The application shall present books in the order they were added |
| AC-005 | BOOK-LIST-004 | When a reader removes a book, the application shall omit it from the next list read |
| AC-006 | TEST-COVERAGE-005 | The application shall provide `bin/test.sh` at the application root, POSIX-compatible, that exits zero only when every automated test passes |

## Source Inventory

| Path | Content kind | Disposition | Reason |
|---|---|---|---|
| `sources/full_test.sh` | code | analyzed | readable UTF-8 |
| `sources/reading-list.md` | markdown | analyzed | readable UTF-8 |

## Relationship Model

| Source or group | Relationship type | Related source or group | Evidence | Delivery implication |
|---|---|---|---|---|
| sources/reading-list.md | dependency | sources/full_test.sh | Source states the completed app provides `bin/test.sh`; `full_test.sh` dispatches to it and reports absence as failure | Terminal verification story depends on all behavior stories and the `bin/test.sh` deliverable |
| sources/full_test.sh | dependency | bin/test.sh (application-built) | `full_test.sh` line `exec sh bin/test.sh` | The application must produce `bin/test.sh`; the harness is staged, not the runner |

## Source Roles

| Path | Role | Plan disposition | Build disposition |
|---|---|---|---|
| sources/reading-list.md | author intent | compass | prompt-only |
| sources/full_test.sh | conformance harness | context | stage |

## Planning Instructions

### Delivery Shape

The system is a web application for managing a personal reading list. Inputs are reader-submitted title and author pairs and removal requests. Outputs are a rendered ordered list of books and validation error messages. Required execution flow: the application is built from story increments; each behavior story is implemented with its own focused tests; the final terminal story provides `bin/test.sh` and proves the complete suite passes via `sh sources/full_test.sh`.

### Story Realization Map

- BOOK-LIST-001: `sources/reading-list.md` (add book, title and author). Requires a persistence capability and a web add form/route. Acceptance: focused story tests.
- BOOK-LIST-002: `sources/reading-list.md` (empty title or author rejected with clear error). Requires validation at the submission boundary. Acceptance: focused story tests.
- BOOK-LIST-003: `sources/reading-list.md` (view in order added). Requires stable ordering of stored records. Acceptance: focused story tests.
- BOOK-LIST-004: `sources/reading-list.md` (remove a book). Requires a removal capability and list refresh. Acceptance: focused story tests.
- TEST-COVERAGE-001 to 004: `sources/reading-list.md` ("automated tests for each behavior"). Test harness capability; each story carries its own test slice. Acceptance: focused story tests scoped to the owned behavior.
- TEST-COVERAGE-005: `sources/reading-list.md` (POSIX `bin/test.sh`), `sources/full_test.sh` (conformance harness). Terminal verification story; declares `Suite: full`; depends on all other stories. Acceptance: `sh sources/full_test.sh` exits zero.

### Test and Acceptance Strategy

Focused story tests are bounded to each story's owned slice and declare `Suite: scoped`. The terminal story TEST-COVERAGE-005 gates on the complete unfiltered suite via `sh sources/full_test.sh` and declares `Suite: full`. Final Sea Trial verification runs the same full-suite command as a proof gate.

### Sequencing and Dependencies

- BOOK-LIST-001 precedes BOOK-LIST-002, BOOK-LIST-003, and BOOK-LIST-004 (each depends on a stored book).
- TEST-COVERAGE-001 through 004 accompany their behavior stories.
- TEST-COVERAGE-005 depends on every implementation and test story and runs last.

### Source Conflicts and Gaps

- None. The source defines one coherent behavior set; no cross-source conflicts were found. Stack is unstated and is proposed in TECHNOLOGY_STACK.md under the conventional-choice rule; no stack questionnaire is raised per the Commander-owned stack rule.

## Analysis Notes
generated: 2026-10-23
blueprint: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/workspace/targets/ReadingList/blueprint

Quality: Ready
  blockers: 0
  questions: 0
  features: 2
  stories: 9
  stack: not declared
  display_name: ReadingList
  short_description: A web application for keeping a personal list of books to read, with add, ordered view, and remove.

None.

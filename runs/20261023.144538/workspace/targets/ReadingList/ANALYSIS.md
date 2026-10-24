# Blueprint Analysis: ReadingList

## Commander Expectations

- assert the product lets a reader add a book with a title and an author
- assert the product shows books in the order they were added
- assert the product lets a reader remove a book
- assert an empty title or author is rejected with a clear error message
- assert the application includes automated tests for each behavior
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
| BOOKS-001 | Add a book with title and author | A reader submits a title and an author and the book is stored and shown in the list |
| BOOKS-002 | List books in the order added | Books are presented in the order they were added |
| BOOKS-003 | Remove a book from the list | After a reader removes a book, it is omitted from the list on the next read |

### Feature: Input Validation

| ID | Story | High-level AC |
|---|---|---|
| VALID-001 | Reject a submission with an empty title | A submission with an empty title is rejected and the reason is reported |
| VALID-002 | Reject a submission with an empty author | A submission with an empty author is rejected and the reason is reported |

### Feature: Test Coverage and Verification

| ID | Story | High-level AC |
|---|---|---|
| TEST-001 | Provide automated tests for adding a book | Automated tests exist for adding a book |
| TEST-002 | Provide automated tests for listing books in order added | Automated tests exist for listing books in the order added |
| TEST-003 | Provide automated tests for removing a book | Automated tests exist for removing a book |
| TEST-004 | Provide automated tests for rejecting an empty title or author | Automated tests exist for rejecting an empty title or author |
| TEST-005 | Provide POSIX-compatible `bin/test.sh` runner | `sh bin/test.sh` runs the complete automated test suite from the application root and exits zero only when every test passes |

## Story Guidance

Named stories planning must produce. Authoritative record: `STORY_GUIDANCE.json`.

None.

## Surfaced Acceptance Criteria

| ID | Story ID | Criterion |
|---|---|---|
| AC-001 | BOOKS-001 | The stored book is shown in the list with its title and author |
| AC-002 | BOOKS-002 | Books appear in the order they were added |
| AC-003 | BOOKS-003 | A removed book does not appear in the list on the next read |
| AC-004 | VALID-001 | An empty title is rejected and the rejection reason is reported to the reader |
| AC-005 | VALID-002 | An empty author is rejected and the rejection reason is reported to the reader |
| AC-006 | TEST-005 | `bin/test.sh` is located at the application root and is executed with `sh` |

## Source Inventory

| Path | Content kind | Disposition | Reason |
|---|---|---|---|
| `sources/full_test.sh` | code | analyzed | readable UTF-8 |
| `sources/reading-list.md` | markdown | analyzed | readable UTF-8 |

## Relationship Model

| Source or group | Relationship type | Related source or group | Evidence | Delivery implication |
|---|---|---|---|---|
| sources/reading-list.md | dependency | sources/full_test.sh | `full_test.sh` requires `bin/test.sh`, which `reading-list.md` names as a product requirement | `bin/test.sh` must exist as a deliverable before the terminal verification story can pass |
| sources/reading-list.md | instruction-to-test | BOOKS-001, BOOKS-002, BOOKS-003, VALID-001, VALID-002 | "includes automated tests for each behavior" | Each behavior story has a paired test story |
| sources/full_test.sh | test-kit-to-implementation | bin/test.sh (application root) | Dispatcher runs `sh bin/test.sh` from application root | Terminal verification gates on the full suite |

## Source Roles

| Path | Role | Plan disposition | Build disposition |
|---|---|---|---|
| sources/reading-list.md | author intent | compass | none |
| sources/full_test.sh | conformance harness | context | stage |

## Planning Instructions

### Delivery Shape

The system is a web application that stores an ordered list of books to read. Inputs are a reader's submitted title and author, and removal requests. Outputs are the rendered book list and rejection messages. Required execution flow: the application accepts submissions, validates non-empty title and author, persists the book, lists books in insertion order, and deletes on removal. The application root must contain `bin/test.sh`, which runs the complete automated test suite.

### Story Realization Map

- BOOKS-001: sources/reading-list.md (add with title and author). Requires capability and persistence. Tests in TEST-001.
- BOOKS-002: sources/reading-list.md (view in order added). Requires capability. Tests in TEST-002.
- BOOKS-003: sources/reading-list.md (remove). Requires capability and persistence. Tests in TEST-003.
- VALID-001: sources/reading-list.md (empty title rejected with clear error). Requires capability. Tests in TEST-004.
- VALID-002: sources/reading-list.md (empty author rejected with clear error). Requires capability. Tests in TEST-004.
- TEST-001 through TEST-004: test harness coverage for behaviors, sources/reading-list.md.
- TEST-005: sources/full_test.sh and sources/reading-list.md (`bin/test.sh` POSIX runner). Requires test harness and acceptance contract.

### Test and Acceptance Strategy

Focused story tests run per behavior story and are bounded to the slice each story owns (`Suite: scoped`). The terminal verification story TEST-005 depends on every implementation story and declares `Suite: full`, running `sh sources/full_test.sh` from the application root with the full unfiltered suite. Sea Trial st-001 is the project-level proof gate for the complete suite.

### Sequencing and Dependencies

- Build BOOKS-001 before BOOKS-002 and BOOKS-003, since listing and removal operate on stored books.
- VALID-001 and VALID-002 depend on BOOKS-001 (submission path).
- TEST-001 through TEST-004 follow their behavior stories.
- TEST-005 follows all implementation and test stories and gates the final build story.

### Source Conflicts and Gaps

- None. The sources do not state a persistence mechanism, UI framework, or language. These are resolved through TECHNOLOGY_STACK.md proposals and do not block planning.

## Analysis Notes
generated: 2026-10-23
blueprint: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/workspace/targets/ReadingList/blueprint

Quality: Ready
  blockers: 0
  questions: 0
  features: 3
  stories: 10
  stack: not declared
  display_name: not proposed
  short_description: not proposed

Ambiguous signals: project type detected as `web` from "web application" in sources; no screen detail given.

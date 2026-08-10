# Blueprint Analysis: ReadingList

## Commander Expectations

- assert readers can maintain an ordered personal list of books to read through a web application.
- assert invalid empty title or author submissions are rejected with a clear reason.
- assert the complete automated test suite runs through `sh bin/test.sh` and exits zero only when every test passes.

## Crew

| Crew | Charge |
|---|---|
| Commander | Defines intent and decides what done means. |
| Team Lead | Confirms epic completeness and stakeholder expectations. |
| Planning Crew | Authors atomic specifications and the ordered Manifest. |
| Shipyard Crew | Builds the tickets without synchronous Commander access. |

## Story List

### Feature: Reading List Experience

| ID | Story | High-level AC |
|---|---|---|
| READING-LIST-001 | Provide the reading-list web entry point | A reader can open the application and view the reading list and available book actions. |
| READING-LIST-002 | Add a book with title and author | When a reader submits a non-empty title and author, the application stores the book and shows it in the list. |
| READING-LIST-003 | Display books in insertion order | The application presents books in the order they were added. |
| READING-LIST-004 | Reject incomplete book submissions | If a title or author is empty, the application rejects the submission and reports the reason clearly. |
| READING-LIST-005 | Remove a book | When a reader removes a book, the application omits it from the list on the next read. |

### Feature: Verification and Test Execution

| ID | Story | High-level AC |
|---|---|---|
| VERIFICATION-001 | Provide the complete automated test runner | `sh bin/test.sh` runs the complete automated test suite from the application root and exits zero only when every test passes. |

## Surfaced Acceptance Criteria

| ID | Story ID | Criterion |
|---|---|---|
| AC-001 | READING-LIST-001 | The primary web entry point presents a usable empty-list state when no books have been added. |
| AC-002 | READING-LIST-001 | Interactive failures are shown as clear user-facing error messages. |

## Source Inventory

| Path | Content kind | Disposition | Reason |
|---|---|---|---|
| `sources/reading-list.md` | markdown | analyzed | readable UTF-8 |

## Relationship Model

| Source or group | Relationship type | Related source or group | Evidence | Delivery implication |
|---|---|---|---|---|
| `sources/reading-list.md` | instruction-to-test | `VERIFICATION-001` | The source requires automated tests and a POSIX-compatible `bin/test.sh`. | Implement the runner and preserve its command, exit code, stdout, and stderr as verification evidence. |
| `sources/reading-list.md` | dependency | `READING-LIST-002`, `READING-LIST-003`, `READING-LIST-005` | The source requires storing, listing, ordering, and removing books. | Establish the book persistence boundary before completing the dependent behaviors. |
| `sources/reading-list.md` | instruction-to-test | `READING-LIST-002`–`READING-LIST-005` | The source explicitly requires automated coverage for adding, listing, removing, and rejecting books. | Each behavior receives focused tests; the complete suite remains terminal verification. |

## Source Roles

| Path | Role | Plan disposition | Build disposition |
|---|---|---|---|
| `sources/reading-list.md` | author intent | compass | prompt-only |

## Planning Instructions

### Delivery Shape

The system is a local web application for readers. Its primary input is a title and author submitted through the web interface. It persists books, returns the collection in insertion order, and removes selected books. The delivery flow establishes the web entry point and persistence boundary, implements add/list/remove/validation behavior, then verifies all behaviors through focused tests and the complete POSIX test runner.

### Story Realization Map

| Story ID | Blueprint scope | Evidence | Related files | Delivery shape |
|---|---|---|---|---|
| READING-LIST-001 | Web entry point and list screen | `sources/reading-list.md` | Application templates and routes | capability and acceptance contract |
| READING-LIST-002 | Book creation and persistence | `sources/reading-list.md` | Persistence module, add route/form | capability and focused test |
| READING-LIST-003 | Ordered list retrieval | `sources/reading-list.md` | List query/rendering code | capability and focused test |
| READING-LIST-004 | Empty-field validation and error display | `sources/reading-list.md` | Validation logic and form error rendering | capability and focused test |
| READING-LIST-005 | Book removal | `sources/reading-list.md` | Remove route and persistence operation | capability and focused test |
| VERIFICATION-001 | Complete test execution contract | `sources/reading-list.md` | `bin/test.sh`, automated tests | test harness and terminal acceptance contract |

### Test and Acceptance Strategy

Stories READING-LIST-002 through READING-LIST-005 use focused tests for their owned behavior. READING-LIST-001 verifies the primary entry point and empty state. VERIFICATION-001 is the terminal full-suite gate and runs the complete unfiltered suite through `sh bin/test.sh`; it depends on every implementation story.

### Sequencing and Dependencies

Manifest ordering establishes the application entry point and persistence boundary before the add, list, ordering, validation, and removal stories. Focused tests accompany each behavior. The test runner is completed after the test suite exists and is the final verification story. No external service dependency is stated.

### Source Conflicts and Gaps

No source conflicts exist. The deployment target is unspecified and remains a non-blocking Commander decision. The implementation stack is proposed conventionally in `TECHNOLOGY_STACK.md`.

## Analysis Notes
generated: 2026-08-10T00:00:00-04:00
blueprint: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260810.215216/workspace/targets/ReadingList/blueprint

Quality: Questions
  blockers: 0
  questions: 2
  features: 2
  stories: 6
  stack: Python, Flask, SQLite, HTML/CSS, pytest, POSIX sh
  display_name: ReadingList
  short_description: A web application for maintaining an ordered list of books to read.

None.

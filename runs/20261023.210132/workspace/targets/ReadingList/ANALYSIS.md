# Blueprint Analysis: ReadingList

## Commander Expectations

- assert readers can maintain an ordered reading list of books through a web application.
- assert every described behavior is covered by automated tests.
- assert `sh bin/test.sh` is the complete release verification command.

## Crew

| Crew | Charge |
|---|---|
| Commander | Defines intent and decides what done means. |
| Team Lead | Confirms epic completeness and stakeholder expectations. |
| Planning Crew | Authors atomic specifications and the ordered Manifest. |
| Shipyard Crew | Builds the tickets without synchronous Commander access. |

## Story List

### Feature: Reading List Management

| ID | Story | High-level AC |
|---|---|---|
| RLB-001 | View the reading list | The reader can open the primary page and see books, or a clear empty-list state, in stored order. |
| RLB-002 | Add a book | Submitting a title and author stores the book and shows it in the list. |
| RLB-003 | Preserve addition order | Books are presented in the order they were added. |
| RLB-004 | Remove a book | Removing a book omits it from the next list read. |
| RLB-005 | Reject incomplete books | An empty title or author is rejected with a clear error message. |

### Feature: Quality Verification

| ID | Story | High-level AC |
|---|---|---|
| RLB-006 | Provide the complete test runner | `bin/test.sh` runs all automated tests and exits zero only when every test passes. |

## Story Guidance

Named stories planning must produce. Authoritative record: `STORY_GUIDANCE.json`.

None.

## Surfaced Acceptance Criteria

| ID | Story ID | Criterion |
|---|---|---|
| AC-001 | RLB-001 | The primary web entry point shall provide the reading-list workflow without requiring an undocumented route. |
| AC-002 | RLB-001 | While the list is loading, the interface shall communicate that state; when loading or retrieval fails, it shall show a clear error and preserve recoverability. |
| AC-003 | RLB-005 | Validation feedback shall identify whether the title or author is missing and shall leave the reader able to correct and resubmit. |

## Source Inventory

| Path | Content kind | Disposition | Reason |
|---|---|---|---|
| `sources/full_test.sh` | code | analyzed | readable UTF-8 |
| `sources/reading-list.md` | markdown | analyzed | readable UTF-8 |

## Relationship Model

| Source or group | Relationship type | Related source or group | Evidence | Delivery implication |
|---|---|---|---|---|
| `sources/reading-list.md` | instruction-to-test | `sources/full_test.sh` | The product prose requires automated tests and a complete test command. | Build behavior stories with focused tests, then gate release on the terminal suite story. |
| `sources/full_test.sh` | conformance harness | `bin/test.sh` | The harness dispatches to the delivered `bin/test.sh` and fails when it is absent. | Stage the harness and make the project runner executable from the application root. |
| Reading-list persistence and UI stories | dependency | `RLB-001`–`RLB-005` | Add, list, order, remove, and validation describe one maintained collection. | Establish the persistence boundary before wiring the web workflow. |

## Source Roles

| Path | Role | Plan disposition | Build disposition |
|---|---|---|---|
| `sources/reading-list.md` | normative specification | context | prompt-only |
| `sources/full_test.sh` | conformance harness | context | stage |

## Planning Instructions

### Delivery Shape

A small server-rendered web application serves a primary reading-list page. The application accepts title/author submissions, persists books, reads them in insertion order, and removes selected books. The build also provides a POSIX-compatible test runner and focused automated tests.

### Story Realization Map

| Story ID | Blueprint scope | Evidence | Related files | Delivery shape |
|---|---|---|---|---|
| RLB-001 | Primary page and ordered list read | `sources/reading-list.md` | Web route, template, list repository call | capability, integration |
| RLB-002 | Book creation workflow | `sources/reading-list.md` | Form, create route, repository, DTO | capability, integration |
| RLB-003 | Ordering contract | `sources/reading-list.md` | Ordered repository read and test | capability, test harness |
| RLB-004 | Book deletion workflow | `sources/reading-list.md` | Delete route, repository, UI action, test | capability, integration |
| RLB-005 | Input validation and feedback | `sources/reading-list.md` | Boundary validation, error rendering, tests | capability, test harness |
| RLB-006 | Complete automated verification | `sources/full_test.sh`, `sources/reading-list.md` | `bin/test.sh`, test suite | acceptance contract |

### Test and Acceptance Strategy

Stories RLB-001 through RLB-005 use focused tests for their owned behavior. RLB-006 is the sole terminal verification story and runs the complete unfiltered suite with `Suite: full`. The Sea Trials execute the staged `sources/full_test.sh`, which delegates to `bin/test.sh`.

### Sequencing and Dependencies

Create the application and persistence boundary before the routes. Implement list and create behavior before ordering, removal, and validation refinements. Add focused tests with each behavior. Build `bin/test.sh` before terminal verification; the complete suite runs only after all implementation stories.

### Source Conflicts and Gaps

No source conflicts remain. The unattended run selects a conventional local web deployment, Flask with Python, and SQLite-backed relational persistence. Identity is resolved as display name `ReadingList` with the short description “A web application for maintaining an ordered list of books to read.”

## Analysis Notes
generated: 2026-10-23
blueprint: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.210132/workspace/targets/ReadingList/blueprint

Quality: Ready
  blockers: 0
  questions: 0
  features: 2
  stories: 6
  stack: Python, Flask, SQLite, SQLAlchemy, Alembic, pytest, POSIX shell
  display_name: ReadingList
  short_description: A web application for maintaining an ordered list of books to read.

None.

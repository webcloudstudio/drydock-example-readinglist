# MANIFEST: ReadingList
updated:     2026-10-23T21:04:00+00:00
state:       approved
blocks:      6

applied_specs: |
  ARCHITECTURE.md sha256=b6aaa721727d6d785b4ddbf830818102584f78446b4f2e57ba1bfddb1dfa554a commit=5cea138dfc98c97d70b7a264c0e492cfc1820b6a applied_by=block-1 applied_at=2026-10-23T21:06:32+00:00 build_sha256=0ff1c28e7a99f4a3e5489c1ad9a83941a7848ee39af9887a1bb6115a3156d019
  ARCHITECTURE_compact.md sha256=9debdaade4762c69b0ede9ce1269bfcd5c548c90c1dc214d3457f3cc86c413a2 commit=b848881e9e50ef46517d45bd93deb3072e5d0ca8 applied_by=block-6 applied_at=2026-10-23T21:14:45+00:00 build_sha256=9debdaade4762c69b0ede9ce1269bfcd5c548c90c1dc214d3457f3cc86c413a2
  DATABASE.md sha256=0bab0628f6130ff0e1c840409170226b73ac94f3a474ecee669f2d01577bbbd7 commit=5cea138dfc98c97d70b7a264c0e492cfc1820b6a applied_by=block-4 applied_at=2026-10-23T21:11:35+00:00 build_sha256=555353ae358e91b3e2c5b9b21484e4f701115f1d89d207c0f098d337a8d4d4c3 database_operations=FEATURE-READING-LIST-001:ed05ec5c9dd3f0f2833dab43a73673b08bae38dc7954ba218f385e186444945a;FEATURE-ADD-BOOK-001:08e223410fbba0611a35a9c0f44a947971c15b333bc2353d5d5a9d0d26bd6a46;FEATURE-REMOVE-BOOK-001:c61257802083784c2ff4a4fa6d828aeaab19d2f45b7441cdd97e71b5dd7b7b22
  DATABASE_compact.md sha256=232477bf2e9d073cc69c80cbf7d3fe1e0744a54952f55e7806f26a0701a36cef commit=41fcdf8b4aa3368ce717a33149ac83bb9c89f1b3 applied_by=block-6 applied_at=2026-10-23T21:14:45+00:00 build_sha256=232477bf2e9d073cc69c80cbf7d3fe1e0744a54952f55e7806f26a0701a36cef
  FEATURE-ADD-BOOK.md sha256=4f0a0049b4a12ee66194bf88e1a80527706bcaac981164e9b84698ebf64b16ee commit=5cea138dfc98c97d70b7a264c0e492cfc1820b6a applied_by=block-4 applied_at=2026-10-23T21:11:35+00:00 build_sha256=341fd9e1bcc8af388a921f2c74560a8ca9371c4f0a5ae2a1f77bad5632eaef1d
  FEATURE-READING-LIST.md sha256=869e7a401e9a11dc9d93974b7e8bacd0ed77a95a2a5e51c968e0dbc73ec68c35 commit=5cea138dfc98c97d70b7a264c0e492cfc1820b6a applied_by=block-4 applied_at=2026-10-23T21:11:35+00:00 build_sha256=4127278f56113839822ce6f16006d09a4c800cacb137f9cf8fb3932f27ee75d2
  FEATURE-REMOVE-BOOK.md sha256=61778c0517fc3c78608e367450e801d3173dc569769718cd94577cd31d80cf88 commit=5cea138dfc98c97d70b7a264c0e492cfc1820b6a applied_by=block-4 applied_at=2026-10-23T21:11:35+00:00 build_sha256=618d2d3840ef2e80a6a9493e3a1f718ce3146b59a4eba4323d009c1c8dcdce1c
  FEATURE-VALIDATE-BOOK.md sha256=45a2fdea982a272ce49fd3bce8a04ff3c98559767c19186bfeecafc915cd7c6e commit=5cea138dfc98c97d70b7a264c0e492cfc1820b6a applied_by=block-4 applied_at=2026-10-23T21:11:35+00:00 build_sha256=dfc464cf68d5762e6c229f601643afee97d10168a840c8ef8f0aca0ab83d8178
  FEATURE-VERIFICATION.md sha256=96f43a6006bc8aa865e4127e1e20a470709a060bba6168dba7a788bcf6c7247c commit=5cea138dfc98c97d70b7a264c0e492cfc1820b6a applied_by=block-6 applied_at=2026-10-23T21:14:45+00:00 build_sha256=d3eb56cfafddecab00b3844a18539a81cac1eb2f9629f944aed61c6ecc4a42cb
  SCREEN-ReadingList.md sha256=b442ee2a69c9b9e5c92a3899500b1e0f3fd028c7fe5c8cff4df3990771bcbbfb commit=5cea138dfc98c97d70b7a264c0e492cfc1820b6a applied_by=block-5 applied_at=2026-10-23T21:13:09+00:00 build_sha256=c990a4e438f79f5a1018d8f77b7afeb0227c978f40827ae1245231759c2c4987
  UI-GENERAL.md sha256=6f2477b3375daecce60509d945b2cf8af28b9aa47a32173449c94fcf6a00196c commit=5cea138dfc98c97d70b7a264c0e492cfc1820b6a applied_by=block-3 applied_at=2026-10-23T21:08:20+00:00 build_sha256=ff7371f39db30fdea9345abea97c22a0a7092162cdbebadb4a0ace353b772c1c
  full_test.sh sha256=d4b7169755d1b5e6bf7a2a8a452d916a27904219951cacaf9cf1edb7f50f7aa2 commit=5cea138dfc98c97d70b7a264c0e492cfc1820b6a applied_by=block-6 applied_at=2026-10-23T21:14:45+00:00 build_sha256=d4b7169755d1b5e6bf7a2a8a452d916a27904219951cacaf9cf1edb7f50f7aa2
## story 1: Establish the Flask application structure and module boundaries.
id:           architecture
finding: ADVISORY: implemented, not verified — no governed acceptance command covers this story. Declare one in ACCEPTANCE.json to gate it.
evidence: evidence/block-1.md
summary:      Establish the Flask application structure and module boundaries.
type:         foundational
kind:         capability
phase:        1
block:        1
implements:   ARCHITECTURE.md
scope:        blueprint
instructions: |
  Establish the Python Flask application factory, testing client entry point, module ownership boundaries, and application configuration needed by the reading-list features. Keep persistence access behind the generated persistence package and make the primary web application runnable.
stack:        python.md, flask.md
stack_mode:   builder
size:         2562
provides:     app_server.create_app, app_server.testing.web_client
acceptance:   yes
state: closed/implemented

## story 2: Provide relational persistence for ordered books.
id:           database
finding: ADVISORY: implemented, not verified — no governed acceptance command covers this story. Declare one in ACCEPTANCE.json to gate it.
evidence: evidence/block-2.md
summary:      Provide relational persistence for ordered books.
type:         foundational
kind:         migration
phase:        1
block:        2
implements:   DATABASE.md
scope:        blueprint
instructions: |
  Declare and provision the local relational store for books, including a stable identifier, title, author, and insertion-order field. Provide the repository operations required by the reading-list workflows through the generated persistence contract.
stack:        python.md, persistence.md, sqlite.md
stack_mode:   builder
size:         7506
provides:     persistence.books
acceptance:   yes
state: closed/implemented

## story 3: Define the shared server-rendered interface patterns.
id:           ui-general
finding: ADVISORY: implemented, not verified — no governed acceptance command covers this story. Declare one in ACCEPTANCE.json to gate it.
evidence: evidence/block-3.md
summary:      Define the shared server-rendered interface patterns.
type:         foundational
kind:         capability
phase:        2
block:        3
implements:   UI-GENERAL.md
scope:        blueprint
instructions: |
  Define the shared HTML structure, accessible form controls, list presentation, empty state, validation feedback, and reusable styling conventions for the server-rendered reading-list page.
stack:        python.md, flask.md
stack_mode:   consumer
size:         2054
provides:     shared reading-list layout and feedback patterns
consumes:     app_server.create_app
depends:      architecture
acceptance:   yes
state: closed/implemented

## story 4: Serve the ordered reading-list view.
id: reading-list
finding: ADVISORY: implemented, not verified — no governed acceptance command covers this story. Declare one in ACCEPTANCE.json to gate it.
evidence: evidence/block-4.md
summary: Serve the ordered reading-list view.
type: service
kind: capability
phase: 2
block: 4
implements: FEATURE-READING-LIST.md
covers: RLB-001, RLB-003
accepts: st-003
context: ARCHITECTURE_compact.md, DATABASE_compact.md
stack: python.md, flask.md, persistence.md
stack_mode: consumer
size: 5598
provides: GET /
consumes: app_server.create_app, persistence.books.list
instructions: Implement the read workflow for the primary reading-list page. Retrieve books through the persistence contract in insertion order, render the collection or a clear empty-list state, and expose the primary GET / route.
acceptance: yes
depends: architecture, database
state: closed/implemented
scope: both

## story 5: Add a valid book to the reading list.
id: add-book
finding: ADVISORY: implemented, not verified — no governed acceptance command covers this story. Declare one in ACCEPTANCE.json to gate it.
evidence: evidence/block-4.md
summary: Add a valid book to the reading list.
type: service
kind: capability
phase: 2
block: 4
implements: FEATURE-ADD-BOOK.md
covers: RLB-002
accepts: st-002
context: ARCHITECTURE_compact.md, DATABASE_compact.md
stack: python.md, flask.md, persistence.md
stack_mode: consumer
size: 5457
provides: POST /books
consumes: app_server.create_app, persistence.books.create
instructions: Implement the valid book submission workflow at POST /books. Accept title and author form values, create the book through the persistence contract, and redirect or render the updated list so the newly stored book is visible.
acceptance: yes
depends: architecture, database
state: closed/implemented
scope: both

## story 6: Remove a selected book from the reading list.
id: remove-book
finding: ADVISORY: implemented, not verified — no governed acceptance command covers this story. Declare one in ACCEPTANCE.json to gate it.
evidence: evidence/block-4.md
summary: Remove a selected book from the reading list.
type: service
kind: capability
phase: 2
block: 4
implements: FEATURE-REMOVE-BOOK.md
covers: RLB-004
accepts: st-004
context: ARCHITECTURE_compact.md, DATABASE_compact.md
stack: python.md, flask.md, persistence.md
stack_mode: consumer
size: 5525
provides: POST /books/<book_id>/delete
consumes: app_server.create_app, persistence.books.delete
instructions: Implement removal at POST /books/<book_id>/delete. Delete only the selected persisted book through the repository contract and ensure the next reading-list request omits it.
acceptance: yes
depends: architecture, database
state: closed/implemented
scope: both

## story 7: Reject incomplete book submissions with correction feedback.
id: validate-book
finding: ADVISORY: implemented, not verified — no governed acceptance command covers this story. Declare one in ACCEPTANCE.json to gate it.
evidence: evidence/block-4.md
summary: Reject incomplete book submissions with correction feedback.
type: service
kind: capability
phase: 2
block: 4
implements: FEATURE-VALIDATE-BOOK.md
covers: RLB-005
accepts: st-005
context: ARCHITECTURE_compact.md, DATABASE_compact.md
stack: python.md, flask.md, persistence.md
stack_mode: consumer
size: 5770
provides: validation for POST /books
consumes: POST /books, app_server.create_app
instructions: Add boundary validation for POST /books. Reject an empty title, an empty author, or both before persistence, report which required field is missing, and preserve a usable form workflow so the reader can correct and resubmit.
acceptance: yes
depends: architecture, database, add-book
state: closed/implemented
scope: both

## story 8: Assemble the primary reading-list page and interactions.
id: reading-list-screen
finding: ADVISORY: implemented, not verified — every binding criterion this story passed was already green before the story built, so none measured the work. Repair the criteria in the Blueprint to exercise this story and rebuild to obtain a verdict.
evidence: evidence/block-5.md
summary: Assemble the primary reading-list page and interactions.
type: service
kind: integration
phase: 2
block: 5
implements: SCREEN-ReadingList.md
covers: RLB-006
context: ARCHITECTURE_compact.md, DATABASE_compact.md
stack: python.md, flask.md
stack_mode: consumer
size: 4568
provides: primary reading-list screen
consumes: GET /, POST /books, POST /books/<book_id>/delete
instructions: Assemble the primary server-rendered screen using the shared UI patterns and feature routes. Include the add-book form, ordered book display, empty state, validation feedback, and a removal control for each persisted book.
acceptance: yes
depends: ui-general, reading-list, add-book, remove-book, validate-book
state: closed/implemented
scope: both

## story 9: Provide the complete POSIX automated test runner.
id: verification
finding: ADVISORY: implemented, not verified — every binding criterion this story passed was already green before the story built, so none measured the work. Repair the criteria in the Blueprint to exercise this story and rebuild to obtain a verdict.
evidence: evidence/block-6.md
summary: Provide the complete POSIX automated test runner.
type: service
kind: test harness
phase: 3
block: 6
implements: FEATURE-VERIFICATION.md
accepts: st-001, st-006
context: full_test.sh, ARCHITECTURE_compact.md, DATABASE_compact.md
stack: python.md
stack_mode: consumer
size: 4087
provides: bin/test.sh, complete automated test suite
consumes: primary reading-list screen, GET /, POST /books, POST /books/<book_id>/delete
instructions: Add a POSIX-compatible executable bin/test.sh that runs the complete automated test suite from the application root and exits zero only when every test passes. Include focused automated tests for adding, ordering, removing, and rejecting incomplete books. The terminal acceptance for this story runs the staged sources/full_test.sh with Suite: full.
acceptance: yes
depends: architecture, database, ui-general, reading-list, add-book, remove-book, validate-book, reading-list-screen
state: closed/implemented
scope: target

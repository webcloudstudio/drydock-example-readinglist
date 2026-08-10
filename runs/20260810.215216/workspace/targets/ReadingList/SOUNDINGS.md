# Soundings

Per-assertion acceptance board, one row per Blueprint Programmatic Acceptance check.
`drydock plan` projects every assertion as `— UNVERIFIED`; `drydock score ac` sets the
Status column from deterministic proof results. A rerun of `drydock plan` resets Status to
`— UNVERIFIED`; rescore to refresh.

| Status | Blueprint | AC Id | Text | Evidence | Verified At |
|---|---|---|---|---|---|
| ✗ FAIL | ARCHITECTURE.md | application-factory | The application factory creates a testable Flask application. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | ARCHITECTURE.md | root-route | The application boundary exposes the reading-list entry route. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | ARCHITECTURE.md | local-boundary | The application can be configured with a local database path. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | DATABASE.md | persistence-interface | The persistence boundary stores and reads a book through its public interface. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | DATABASE.md | insertion-order | The persistence interface returns books in insertion order. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | DATABASE.md | removal | Removing a stored book makes it absent from a subsequent read. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Add-Book.md | add-route | The add route accepts a valid title and author. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Add-Book.md | add-round-trip | A successful add is visible through the public list route. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Add-Book.md | add-requires-both-fields | A valid add creates a record containing both required fields. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Remove-Book.md | removes-selected-book | A selected book is absent after removal. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Remove-Book.md | preserves-other-books | Removing one book does not remove other books. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Remove-Book.md | unknown-book-removal | Removing an unknown book does not create or alter a book. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-List-Books.md | list-route | The list route is reachable and returns an empty collection for a new store. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-List-Books.md | list-round-trip | The list route returns books persisted through the add workflow. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-List-Books.md | list-preserves-order | The route preserves insertion order independently of request order. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Validate-Book.md | rejects-empty-title | An empty title is rejected before persistence. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Validate-Book.md | rejects-empty-author | An empty author is rejected before persistence. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Validate-Book.md | accepts-complete-submission | A submission with a non-empty title and author is not rejected by validation. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | SCREEN-Reading-List.md | renders-empty-list | The primary entry point is reachable and renders the empty-list state. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | SCREEN-Reading-List.md | renders-added-book | A book added through the user workflow appears on the primary screen. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | SCREEN-Reading-List.md | submits-book-form | The screen's add interaction calls the declared creation route. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | SCREEN-Reading-List.md | submits-remove-control | The screen's remove interaction calls the declared removal route. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | SCREEN-Reading-List.md | renders-validation-error | An invalid screen submission returns to a state containing a user-facing error. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Verification.md | complete-suite-run | The complete automated test suite passes through the required POSIX runner. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Verification.md | runner-is-posix-invocable | The runner can be invoked from the application root using POSIX `sh`. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |
| ✗ FAIL | FEATURE-Verification.md | suite-covers-book-behaviors | The test suite contains executable coverage for each required book behavior. | unverified acceptance: acceptance environment unavailable: Target Python project has no .venv | 2026-08-10T22:07:38+00:00 |

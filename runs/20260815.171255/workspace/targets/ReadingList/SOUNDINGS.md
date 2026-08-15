# Soundings

Per-assertion acceptance board, one row per Blueprint Programmatic Acceptance check.
`drydock plan` projects every assertion as `— UNVERIFIED`; `drydock score ac` sets the
Status column from deterministic proof results. A rerun of `drydock plan` resets Status to
`— UNVERIFIED`; rescore to refresh.

| Status | Blueprint | AC Id | Text | Evidence | Verified At |
|---|---|---|---|---|---|
| ✓ PASS | ARCHITECTURE.md | architecture-factory | The application factory creates a runnable Flask application with an HTTP test client. |  | 2026-08-15T17:38:53+00:00 |
| ✓ PASS | ARCHITECTURE.md | architecture-isolation | Separate application instances can be created independently for isolated execution. |  | 2026-08-15T17:38:53+00:00 |
| ✓ PASS | ARCHITECTURE.md | architecture-entrypoint | The web entrypoint exposes the application factory without requiring a development server to start during import. |  | 2026-08-15T17:38:53+00:00 |
| ✓ PASS | DATABASE.md | database-add-readback | A book added through the persistence interface can be read back with the submitted fields. |  | 2026-08-15T17:38:53+00:00 |
| ✓ PASS | DATABASE.md | database-order | Ordered reads preserve the order in which books were added. |  | 2026-08-15T17:38:53+00:00 |
| ✓ PASS | DATABASE.md | database-remove | Removing an existing book makes it absent from a subsequent persistence read. |  | 2026-08-15T17:38:53+00:00 |
| ✓ PASS | DATABASE.md | database-empty | A new database returns an empty ordered collection. |  | 2026-08-15T17:38:53+00:00 |
| ✓ PASS | UI-GENERAL.md | ui-patterns-form | The shared presentation includes labeled title and author controls and a submission control. |  | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | UI-GENERAL.md | ui-patterns-empty-state | The shared presentation provides a reader-visible empty-list state. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ✓ PASS | UI-GENERAL.md | ui-patterns-removal-control | The shared presentation provides a removal control for a listed book. |  | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Book-Creation.md | book-creation-route | The book-creation route accepts a submitted title and author and returns a redirect response. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Book-Creation.md | book-creation-readback | A successfully submitted book is visible when the list is read again. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Book-Creation.md | book-creation-preserves-existing-order | Adding a new book preserves the relative order of books already present. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Ordered-List.md | ordered-list-route | The reading-list route is reachable and returns a successful response for an empty store. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Ordered-List.md | ordered-list-empty-state | An empty store produces a reader-understandable empty-list state. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Ordered-List.md | ordered-list-order | The list renders multiple books in their insertion order. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Book-Removal.md | removal-route-reachable | The removal route accepts a valid removal request. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ✓ PASS | FEATURE-Book-Removal.md | removal-persists | Removing a book makes it absent on the next public list read. |  | 2026-08-15T17:38:53+00:00 |
| ✓ PASS | FEATURE-Book-Removal.md | removal-preserves-remaining-order | Removing one book leaves the other books in their original relative order. |  | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Incomplete-Submission.md | validation-rejects-empty-title | A submission with an empty title is rejected with a client validation response. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Incomplete-Submission.md | validation-rejects-empty-author | A submission with an empty author is rejected with a client validation response. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Incomplete-Submission.md | validation-does-not-persist-invalid-submission | Invalid submissions do not appear in the public list. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Incomplete-Submission.md | validation-preserves-valid-submission | A valid submission remains supported by the creation workflow. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | SCREEN-Reading-List.md | screen-loads | The reading-list screen is reachable at its declared route. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | SCREEN-Reading-List.md | screen-accepts-book-submission | The screen supports submitting a title and author through the declared creation route. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | SCREEN-Reading-List.md | screen-supports-removal | The screen supports removing a listed book through the declared removal route. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | SCREEN-Reading-List.md | screen-supports-empty-state | The screen responds successfully when the reading list is empty. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Test-Suite.md | complete-suite | The required POSIX test launcher runs the complete automated suite successfully. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Test-Suite.md | launcher-runs-from-root | The test launcher is runnable from the application root using the required command. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |
| ~ PREPASSED | FEATURE-Test-Suite.md | behavior-suite-command-exists | The complete launcher invocation is the executable project verification boundary. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T17:38:53+00:00 |

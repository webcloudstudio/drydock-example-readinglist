<!-- Compacted from UI-GENERAL.md sha256=0b6f592e79f56bbddb07352ad5ce0b07084a40a38ed7969e14ac933aa8d25272 on 2026-08-15 by drydock build agent -->

- Single responsive reading-list screen with heading, required title/author form, submit control, ordered book list, per-book removal controls, empty state, and visible validation errors.
- Controls require labels and stable names; removal targets must use book identity, not position.
- Preserve insertion order and display understandable missing-field errors.
- CSS must provide readable typography, focus states, contrast, spacing, and responsive narrow-screen layout.
- Acceptance: GET `/` includes `name="title"`, `name="author"`, and a form; empty state mentions reading plus empty/no books; POST `/books` then GET `/` shows title, author, and removal control.

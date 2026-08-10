<!-- Compacted from FEATURE-Validate-Book.md sha256=d635661ae4a0d2413aba33e2cf94e41ac4ea817729a3f1ef68c26011843da31a on 2026-08-10 by drydock build agent -->

POST /books rejects empty or whitespace-only title or author with HTTP 400 before persistence. Valid submissions continue to persistence.

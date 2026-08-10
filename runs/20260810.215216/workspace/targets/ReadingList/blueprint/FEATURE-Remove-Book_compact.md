<!-- Compacted from FEATURE-Remove-Book.md sha256=b7500db4ae05de76e8b5251e7211a84d438b95f00632b45e302737dfa1fa70a4 on 2026-08-10 by drydock build agent -->

POST /books/{id}/remove removes only the selected local record. Subsequent GET /books omits it while preserving remaining insertion order. Unknown IDs return an allowed not-found or no-op response.

<!-- Compacted from ARCHITECTURE.md sha256=0e2bbc43335e825311da2b8fae7a89b09b02c54a15e5ee482287fae15f909d84 on 2026-08-14 by drydock build agent -->

- `create_app(test_config: dict[str, Any] | None) -> Flask` returns an isolated Flask app; optional config must support `TESTING` and `READING_LIST_DATABASE`.
- `app.routes` owns HTTP routes; `app.database` owns SQLite access. Routes must not access SQLite directly.
- Root route: `GET /`, rendering the current reading-list collection.
- Persistence uses SQLite; application is runnable from the project root via `run.py`.
- `bin/test.sh` runs the complete pytest suite.

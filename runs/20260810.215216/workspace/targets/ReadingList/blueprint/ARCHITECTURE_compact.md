<!-- Compacted from ARCHITECTURE.md sha256=9d0098fc9b7f8a2c2298515873f233aebadf9222619f3d2cc330017af7de380f on 2026-08-10 by drydock build agent -->

Flask factory via `app.create_app(config)`. Routes: `GET /`, `GET /books`, `POST /books`, `POST /books/{id}/remove`. Persistence belongs in `persistence.py`; validation in `validation.py`; rendering in `templates/`; tests in `tests/`. Local-only execution; no third-party transmission.

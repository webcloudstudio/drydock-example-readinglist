<!-- Compacted from ARCHITECTURE.md sha256=c42125d1c9a4d632e46f7b88523442ceb51348a2893aa1bb01dcd7b11bbd892b on 2026-08-15 by drydock build agent -->

Flask app factory: `from app import create_app`; supports isolated overrides including `TESTING` and `DATABASE`. HTTP routes live in `app.routes`; SQLite access is confined to typed `app.persistence`; templates/static assets live under `app/`; tests use pytest; `bin/test.sh` runs the complete suite. Root `/` must return 200, and independent app instances must not share state.

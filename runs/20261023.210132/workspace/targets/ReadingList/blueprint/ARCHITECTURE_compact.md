<!-- Compacted from ARCHITECTURE.md sha256=b6aaa721727d6d785b4ddbf830818102584f78446b4f2e57ba1bfddb1dfa554a on 2026-10-23 by drydock build agent -->

Provides `app_server.create_app()` and `app_server.testing.web_client()`. The factory composes feature-owned Flask Blueprints; feature routes own HTTP workflows, while generated `persistence` owns storage. Required routes: `GET /`, `POST /books`, and `POST /books/<book_id>/delete`. Configuration belongs to `app_server`; the primary workflow is reachable at `/`.

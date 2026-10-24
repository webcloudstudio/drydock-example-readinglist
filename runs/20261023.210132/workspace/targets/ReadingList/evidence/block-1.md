# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 2557
- execution id: 20261023.210502.052Z-4d83d2d4

## Stories built
- Establish the Flask application structure and module boundaries. (architecture) [story]

## Reusable compacts
- ARCHITECTURE_compact.md

## Stacked context
- implements: python.md (SP 761)
- compass: COMPASS.md (SP 551)
- implements: ARCHITECTURE.md (SP 723)
- stack: flask.md (SP 451)

## Build directory changes
- app_server/__init__.py
- app_server/config.py
- app_server/features/__init__.py
- app_server/features/reading_list/__init__.py
- app_server/features/reading_list/routes.py
- app_server/testing.py
- bin/test.sh
- pyproject.toml
- tests/test_architecture.py
- uv.lock

## Pre-build acceptance observation
- RED: architecture-factory (ARCHITECTURE.md)
  intent: The application exposes the selected Flask factory and testing client contracts.
  error: foundation not built: `app_server` is the package the web-server foundation (django.md, fastapi.md, flask.md) builds, and the build directory has no `app_server/`. The criterion exercises the built application, so it was not run.
- RED: architecture-testing (ARCHITECTURE.md)
  intent: The application factory can be created repeatedly for isolated automated tests.
  error: foundation not built: `app_server` is the package the web-server foundation (django.md, fastapi.md, flask.md) builds, and the build directory has no `app_server/`. The criterion exercises the built application, so it was not run.

## Post-build programmatic acceptance
- PASS: architecture-factory (ARCHITECTURE.md)
  intent: The application exposes the selected Flask factory and testing client contracts.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: architecture-testing (ARCHITECTURE.md)
  intent: The application factory can be created repeatedly for isolated automated tests.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
<reusable-compact filename="ARCHITECTURE.md">
Provides `app_server.create_app()` and `app_server.testing.web_client()`. The factory composes feature-owned Flask Blueprints; feature routes own HTTP workflows, while generated `persistence` owns storage. Required routes: `GET /`, `POST /books`, and `POST /books/<book_id>/delete`. Configuration belongs to `app_server`; the primary workflow is reachable at `/`.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- app_server/__init__.py
- app_server/config.py
- app_server/features/__init__.py
- app_server/features/reading_list/__init__.py
- app_server/features/reading_list/routes.py
- app_server/testing.py
- bin/test.sh
- pyproject.toml
- tests/test_architecture.py
- uv.lock

SUMMARY:
Implemented the Flask application factory, configuration boundary, feature Blueprint routes, testing client, POSIX test launcher, dependency manifests, and architecture tests. Pytest and the full dispatcher pass.

BLOCKERS:
- None

# Evidence: Block 3 · Foundational (block-3)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 3270
- execution id: 20261023.145511.914Z-46dec70b

## Stories built
- Provide the shared page layout and register the web server wiring in the application factory. (web-shell) [story]

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 781)
- implements: UI-GENERAL.md (SP 804)
- stack: flask.md (SP 691)

## Build directory changes
- app_server/__init__.py
- app_server/settings.py
- app_server/templates/base.html
- tests/test_base_template.py
- tests/test_create_app_wiring.py

## Pre-build acceptance observation
- RED: ui-base-template-loads (UI-GENERAL.md)
  intent: The base layout template is available to the application.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      template = 'base.html'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "ui-base-template-loads.py", line 4, in <module>
        template = app.jinja_env.get_template("base.html")
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/jinja2/environment.py", line 1016, in get_template
        return self._load_template(name, globals)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/jinja2/environment.py", line 975, in _load_template
        template = self.loader.load(self, name, self.make_globals(globals))
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/jinja2/loaders.py", line 126, in load
        source, filename, uptodate = self.get_source(environment, name)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/flask/templating.py", line 66, in get_source
        return self._get_source_fast(environment, template)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/flask/templating.py", line 100, in _get_source_fast
        raise TemplateNotFound(template)
    jinja2.exceptions.TemplateNotFound: base.html
- RED: ui-base-shows-error (UI-GENERAL.md)
  intent: The base layout renders the supplied error text in its error region.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      template = 'base.html'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "ui-base-shows-error.py", line 7, in <module>
        html = render_template("base.html", error=message)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/flask/templating.py", line 150, in render_template
        template = app.jinja_env.get_or_select_template(template_name_or_list)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/jinja2/environment.py", line 1087, in get_or_select_template
        return self.get_template(template_name_or_list, parent, globals)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/jinja2/environment.py", line 1016, in get_template
        return self._load_template(name, globals)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/jinja2/environment.py", line 975, in _load_template
        template = self.loader.load(self, name, self.make_globals(globals))
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/jinja2/loaders.py", line 126, in load
        source, filename, uptodate = self.get_source(environment, name)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/flask/templating.py", line 66, in get_source
        return self._get_source_fast(environment, template)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/flask/templating.py", line 100, in _get_source_fast
        raise TemplateNotFound(template)
    jinja2.exceptions.TemplateNotFound: base.html
- RED: ui-base-without-error (UI-GENERAL.md)
  intent: The base layout renders without an error and does not show an alert region.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      template = 'base.html'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "ui-base-without-error.py", line 6, in <module>
        html = render_template("base.html")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/flask/templating.py", line 150, in render_template
        template = app.jinja_env.get_or_select_template(template_name_or_list)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/jinja2/environment.py", line 1087, in get_or_select_template
        return self.get_template(template_name_or_list, parent, globals)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/jinja2/environment.py", line 1016, in get_template
        return self._load_template(name, globals)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/jinja2/environment.py", line 975, in _load_template
        template = self.loader.load(self, name, self.make_globals(globals))
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/jinja2/loaders.py", line 126, in load
        source, filename, uptodate = self.get_source(environment, name)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/flask/templating.py", line 66, in get_source
        return self._get_source_fast(environment, template)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/lib/python3.12/site-packages/flask/templating.py", line 100, in _get_source_fast
        raise TemplateNotFound(template)
    jinja2.exceptions.TemplateNotFound: base.html

## Post-build programmatic acceptance
- PASS: ui-base-template-loads (UI-GENERAL.md)
  intent: The base layout template is available to the application.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: ui-base-shows-error (UI-GENERAL.md)
  intent: The base layout renders the supplied error text in its error region.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: ui-base-without-error (UI-GENERAL.md)
  intent: The base layout renders without an error and does not show an alert region.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
I'll start by inspecting the build directory and the staged sources.The staged `full_test.sh` is not in this step's acceptance criteria, so I won't run it. Next I'll read the existing tests and the git-tracked config to match conventions.The foundation tests are the existing baseline. I'll run them before changing anything so I can tell pre-existing failures from new ones.Baseline is green: 7 passed. Now I'll write the implementation: a typed settings module, the base template, and the factory wiring.Now the tests. I'll read rendered HTML back through a parser rather than substring-matching it, and I'll cover the declared acceptance intents plus the edge cases.Now I'll run the full suite, including the new tests.All 26 pass (7 baseline + 19 new). Next I'll run the three declared acceptance criteria verbatim from the spec, feeding them over stdin so no scratch file lands outside the build tree.RESULT: SUCCESS

FILES CHANGED:
- app_server/__init__.py
- app_server/settings.py
- app_server/templates/base.html
- tests/test_base_template.py
- tests/test_create_app_wiring.py

SUMMARY:
- **Base layout** (`app_server/templates/base.html`): `<title>` in `block title` (default "Reading List"), `block content` inside `<main>`, and an error region that renders `<div role="alert">` only when `error` is truthy. Jinja autoescaping applies to the error text.
- **Factory wiring** (`app_server/__init__.py`): `create_app()` sets the Jinja template folder to `app_server/templates` and stores `open_database(...)` in `app.extensions["database"]`. It opens the store without connecting, so no file is created at startup. No book routes are registered.
- **Settings** (`app_server/settings.py`): a frozen `Settings` dataclass reads `DATABASE_URL`, then `DATABASE_PATH`, then defaults to `data/app.db`. This matches the lookup in `persistence/testing.py`.
- **Declared acceptance criteria** (`ui-base-template-loads`, `ui-base-shows-error`, `ui-base-without-error`): all three pass when run verbatim from the spec.
- **Test suite**: `./.venv/bin/python -m pytest -q` gives 26 passed (7 existing, 19 new). The new tests read rendered HTML back through an HTML parser rather than substring-matching it. They cover escaping, the empty and `None` error cases, title override, content-block placement, the alert sitting above content, the template folder, store round-trip through the configured DSN, lazy store opening, no book routes, and settings precedence.
- **Not run**: `sources/full_test.sh`. No criterion in this step invokes it (both ACs are `Suite: scoped`), so I left it alone.
- **Note for a later step**: `bin/test.sh` does not exist yet. `full_test.sh` will fail until a step that owns the st-001 test runner creates it. That is outside this block.

<blueprint-decisions>
[{"spec":"UI-GENERAL.md","severity":"Low","subject":"Settings module and store configuration","decision":"I added app_server/settings.py with a typed Settings dataclass to centralize the store DSN, reading DATABASE_URL, then DATABASE_PATH, then data/app.db, which mirrors persistence/testing.py. I also kept the Database handle in app.extensions['database'] rather than as a module global. Is that acceptable, or should it change on replan?"}]
</blueprint-decisions>

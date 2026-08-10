<!-- Compacted from FEATURE-Add-Book.md sha256=40aa973c8decf937a26790ebb38198f3d1c3601bc35dd669120909fab5ecea50 on 2026-08-10 by drydock build agent -->

POST /books accepts non-whitespace title and author form fields, validates before persistence, stores via BookStore.add, and redirects to the reading-list view. GET /books returns stored records as JSON with id, title, and author.

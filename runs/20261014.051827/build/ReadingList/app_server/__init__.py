"""Flask application factory for the reading list.

Opens the declared store and registers the blueprints feature stories contribute. Routes are added
only by the feature modules that declare them.
"""

from flask import Flask

from app_server.books_views import bp as books_bp
from app_server.pages import bp as pages_bp
from app_server.settings import DATABASE_EXTENSION, PROJECT_ROOT, database_dsn
from persistence import open_database

__all__ = ["create_app"]

SCHEMA_PATH = PROJECT_ROOT / "schema.sql"


def create_app() -> Flask:
    """Build the Flask application with its store, the blueprints, and the error handlers."""
    app = Flask(__name__)
    database = open_database(database_dsn())
    database.execute_script(SCHEMA_PATH.read_text(encoding="utf-8"))
    app.extensions[DATABASE_EXTENSION] = database
    app.register_blueprint(pages_bp)
    app.register_blueprint(books_bp)
    return app

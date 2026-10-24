"""HTTP boundary for reading-list workflows."""

from flask import Blueprint

reading_list = Blueprint("reading_list", __name__)

from app_server.features.reading_list import routes  # noqa: E402,F401

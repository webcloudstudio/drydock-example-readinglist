"""Foundation checks: project tree, dependency manifest, and pytest runner."""

import importlib.metadata
import sys
import tomllib
from pathlib import Path


def _load_pyproject(project_root: Path) -> dict:
    with open(project_root / "pyproject.toml", "rb") as handle:
        return tomllib.load(handle)


def test_declares_supported_python_version(project_root: Path) -> None:
    data = _load_pyproject(project_root)

    assert data["project"]["requires-python"] == ">=3.11"


def test_runtime_dependencies_include_flask(project_root: Path) -> None:
    data = _load_pyproject(project_root)

    names = [entry.lower() for entry in data["project"]["dependencies"]]
    assert any(name.startswith("flask") for name in names)


def test_dev_group_includes_pytest(project_root: Path) -> None:
    data = _load_pyproject(project_root)

    names = [entry.lower() for entry in data["dependency-groups"]["dev"]]
    assert any(name.startswith("pytest") for name in names)


def test_lockfile_exists_at_root(project_root: Path) -> None:
    assert (project_root / "uv.lock").is_file()


def test_tests_directory_and_conftest_exist(project_root: Path) -> None:
    assert (project_root / "tests").is_dir()
    assert (project_root / "tests" / "conftest.py").is_file()


def test_pytest_discovers_tests_from_project_root(project_root: Path) -> None:
    data = _load_pyproject(project_root)

    assert data["tool"]["pytest"]["ini_options"]["testpaths"] == ["tests"]


def test_running_interpreter_can_import_flask() -> None:
    import flask

    assert flask.Flask.__name__ == "Flask"
    assert importlib.metadata.version("flask").split(".")[0] == "3"


def test_python_runtime_meets_declared_minimum() -> None:
    assert sys.version_info >= (3, 11)

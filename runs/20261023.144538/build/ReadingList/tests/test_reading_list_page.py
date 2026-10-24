"""Reading list page: GET / renders the add form, the books in the order added, and the remove controls."""

from html.parser import HTMLParser
from pathlib import Path

import pytest

from app_server import create_app
from app_server.book_service import add_book, remove_book

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JSON_ACCEPT = {"Accept": "application/json"}


@pytest.fixture
def app(monkeypatch, tmp_path):
    """A fresh application over its own store, so no test touches the configured data/app.db."""
    store = tmp_path / "reading-list-page.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{store}")
    monkeypatch.delenv("DATABASE_PATH", raising=False)
    application = create_app()
    application.extensions["database"].execute_script((PROJECT_ROOT / "schema.sql").read_text())
    return application


class _Page(HTMLParser):
    """Collects the forms, the list items, and the text of every role="alert" element."""

    def __init__(self) -> None:
        super().__init__()
        self.forms: list[dict] = []
        self.inputs: list[dict] = []
        self.items: list[dict] = []
        self.alerts: list[str] = []
        self.buttons: list[str] = []
        self._form: dict | None = None
        self._item: dict | None = None
        self._alert_depth = 0
        self._alert_text: list[str] = []
        self._button_text: list[str] | None = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if self._alert_depth:
            self._alert_depth += 1
        elif attributes.get("role") == "alert":
            self._alert_depth = 1
            self._alert_text = []
        if tag == "form":
            self._form = {"method": attributes.get("method"), "action": attributes.get("action"), "inputs": []}
            self.forms.append(self._form)
        elif tag == "input":
            self.inputs.append(attributes)
            if self._form is not None:
                self._form["inputs"].append(attributes)
        elif tag == "li":
            self._item = {"title": "", "author": "", "action": None}
            self.items.append(self._item)
        elif tag == "button":
            self._button_text = []
        elif tag == "span" and self._item is not None:
            self._item["_field"] = attributes.get("class")
        if tag == "form" and self._item is not None:
            self._item["action"] = attributes.get("action")

    def handle_endtag(self, tag):
        if self._alert_depth:
            self._alert_depth -= 1
            if self._alert_depth == 0:
                self.alerts.append("".join(self._alert_text))
        if tag == "form":
            self._form = None
        elif tag == "li":
            self._item = None
        elif tag == "button" and self._button_text is not None:
            self.buttons.append("".join(self._button_text).strip())
            self._button_text = None

    def handle_data(self, data):
        if self._alert_depth:
            self._alert_text.append(data)
        if self._button_text is not None:
            self._button_text.append(data)
        if self._item is not None and self._item.get("_field"):
            field = self._item.pop("_field")
            self._item[field] += data.strip()
            self._item["_field"] = None


def _parse(html: str) -> _Page:
    page = _Page()
    page.feed(html)
    page.close()
    return page


def _listed_titles(page: _Page) -> list[str]:
    return [item["title"] for item in page.items]


def test_index_answers_200_with_html(app):
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.mimetype == "text/html"


def test_index_on_empty_store_shows_empty_state_and_no_list_items(app):
    page = _parse(app.test_client().get("/").get_data(as_text=True))

    assert page.items == []
    assert page.alerts == []


def test_index_lists_books_in_the_order_added(app):
    database = app.extensions["database"]
    for title in ["First", "Second", "Third"]:
        add_book(database, title=title, author="Order Author")

    page = _parse(app.test_client().get("/").get_data(as_text=True))

    assert _listed_titles(page) == ["First", "Second", "Third"]


def test_index_shows_each_book_author(app):
    add_book(app.extensions["database"], title="Dune", author="Frank Herbert")

    page = _parse(app.test_client().get("/").get_data(as_text=True))

    assert [item["author"] for item in page.items] == ["Frank Herbert"]


def test_index_lists_one_book_when_exactly_one_is_stored(app):
    add_book(app.extensions["database"], title="Only", author="Solo")

    page = _parse(app.test_client().get("/").get_data(as_text=True))

    assert _listed_titles(page) == ["Only"]


def test_index_shows_a_book_added_through_post(app):
    client = app.test_client()
    client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})

    page = _parse(client.get("/").get_data(as_text=True))

    assert _listed_titles(page) == ["Dune"]


def test_index_has_add_form_posting_title_and_author_to_books(app):
    page = _parse(app.test_client().get("/").get_data(as_text=True))

    add_forms = [form for form in page.forms if form["action"] == "/books"]
    assert len(add_forms) == 1
    assert add_forms[0]["method"] == "post"
    names = {attributes.get("name") for attributes in add_forms[0]["inputs"]}
    assert {"title", "author"} <= names
    assert "Add book" in page.buttons


def test_index_has_one_remove_form_per_book_posting_to_its_delete_route(app):
    database = app.extensions["database"]
    first = add_book(database, title="First", author="A").id
    second = add_book(database, title="Second", author="B").id

    page = _parse(app.test_client().get("/").get_data(as_text=True))

    remove_actions = [item["action"] for item in page.items]
    assert remove_actions == [f"/books/{first}/delete", f"/books/{second}/delete"]


def test_index_remove_control_is_a_post_form(app):
    add_book(app.extensions["database"], title="Dune", author="Frank Herbert")

    page = _parse(app.test_client().get("/").get_data(as_text=True))

    remove_forms = [form for form in page.forms if form["action"] and form["action"].endswith("/delete")]
    assert len(remove_forms) == 1
    assert remove_forms[0]["method"] == "post"
    assert "Remove" in page.buttons


def test_index_has_no_remove_control_when_no_books_exist(app):
    page = _parse(app.test_client().get("/").get_data(as_text=True))

    assert [form for form in page.forms if form["action"] and form["action"].endswith("/delete")] == []


def test_index_after_removal_no_longer_lists_the_removed_book(app):
    database = app.extensions["database"]
    keep = add_book(database, title="Keep", author="A").id
    drop = add_book(database, title="Drop", author="B").id
    remove_book(database, drop)

    page = _parse(app.test_client().get("/").get_data(as_text=True))

    assert _listed_titles(page) == ["Keep"]
    assert [item["action"] for item in page.items] == [f"/books/{keep}/delete"]


def test_index_escapes_book_titles(app):
    add_book(app.extensions["database"], title="<b>bold</b>", author="A")

    html = app.test_client().get("/").get_data(as_text=True)

    assert "<b>bold</b>" not in html
    assert _listed_titles(_parse(html)) == ["<b>bold</b>"]


def test_rejected_html_submission_rerenders_page_with_reason_and_stored_books(app):
    client = app.test_client()
    client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})

    response = client.post("/books", data={"title": "", "author": "Nobody"})
    page = _parse(response.get_data(as_text=True))

    assert response.status_code == 400
    assert response.mimetype == "text/html"
    assert page.alerts == ["rejected: title is empty"]
    assert _listed_titles(page) == ["Dune"]
    assert any(form["action"] == "/books" for form in page.forms)


def test_rejected_author_submission_shows_author_reason_on_page(app):
    response = app.test_client().post("/books", data={"title": "Dune", "author": " "})

    assert _parse(response.get_data(as_text=True)).alerts == ["rejected: author is empty"]


def test_index_has_no_alert_when_nothing_was_rejected(app):
    page = _parse(app.test_client().get("/").get_data(as_text=True))

    assert page.alerts == []


def test_index_keeps_working_after_rejection(app):
    client = app.test_client()
    client.post("/books", data={"title": "", "author": "Nobody"})

    response = client.get("/")

    assert response.status_code == 200
    assert _parse(response.get_data(as_text=True)).alerts == []


def test_rejected_json_submission_still_answers_json_not_page(app):
    response = app.test_client().post(
        "/books", data={"title": "", "author": "Nobody"}, headers=JSON_ACCEPT
    )

    assert response.mimetype == "application/json"
    assert response.get_json()["field"] == "title"

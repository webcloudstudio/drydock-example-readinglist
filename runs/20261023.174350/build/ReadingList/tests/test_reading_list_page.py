"""Reading list page: GET / renders the list and forms; POST /add and POST /remove/{id} act and redirect."""

from dataclasses import dataclass, field
from html.parser import HTMLParser

import pytest
from flask.testing import FlaskClient


@dataclass
class _Item:
    title: str = ""
    author: str = ""
    remove_action: str | None = None


@dataclass
class _Page:
    items: list[_Item] = field(default_factory=list)
    error: str | None = None
    inputs: dict[str, str] = field(default_factory=dict)
    form_actions: list[str] = field(default_factory=list)
    script_tags: int = 0
    shows_no_books_message: bool = False


class _PageParser(HTMLParser):
    """Collects the page's structure: list items, the error region, form fields, and scripts."""

    def __init__(self) -> None:
        super().__init__()
        self.page = _Page()
        self._item: _Item | None = None
        self._capture: str | None = None
        self._in_empty_message = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "script":
            self.page.script_tags += 1
        elif tag == "form":
            self.page.form_actions.append(attributes.get("action") or "")
            if self._item is not None:
                self._item.remove_action = attributes.get("action")
        elif tag == "input":
            self.page.inputs[attributes.get("name") or ""] = attributes.get("value") or ""
        elif tag == "li":
            self._item = _Item()
        elif tag == "span" and self._item is not None:
            self._capture = attributes.get("class")
        elif tag == "p" and attributes.get("role") == "alert":
            self._capture = "error"
            self.page.error = ""
        elif tag == "p":
            self._in_empty_message = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "li" and self._item is not None:
            self.page.items.append(self._item)
            self._item = None
        elif tag in ("span", "p"):
            self._capture = None
            self._in_empty_message = False

    def handle_data(self, data: str) -> None:
        if self._capture == "title" and self._item is not None:
            self._item.title += data
        elif self._capture == "author" and self._item is not None:
            self._item.author += data
        elif self._capture == "error" and self.page.error is not None:
            self.page.error += data
        elif self._in_empty_message and data.strip() == "No books yet.":
            self.page.shows_no_books_message = True


def _page(client: FlaskClient) -> _Page:
    response = client.get("/")
    assert response.status_code == 200
    parser = _PageParser()
    parser.feed(response.get_data(as_text=True))
    return parser.page


def _add(client: FlaskClient, title: str, author: str = "A") -> int:
    return client.post("/books", json={"title": title, "author": author}).get_json()["id"]


def _listed_ids(client: FlaskClient) -> list[int]:
    return [book["id"] for book in client.get("/books").get_json()]


# GET /


def test_index_answers_200_with_html(fresh_client: FlaskClient) -> None:
    response = fresh_client.get("/")

    assert response.status_code == 200
    assert response.mimetype == "text/html"


def test_index_on_empty_store_shows_no_books_message(fresh_client: FlaskClient) -> None:
    page = _page(fresh_client)

    assert page.items == []
    assert page.shows_no_books_message is True


def test_index_with_books_does_not_show_empty_message(fresh_client: FlaskClient) -> None:
    _add(fresh_client, "Dune")

    assert _page(fresh_client).shows_no_books_message is False


def test_index_lists_each_book_with_its_title_and_author(fresh_client: FlaskClient) -> None:
    _add(fresh_client, "Dune", "Frank Herbert")
    _add(fresh_client, "Emma", "Jane Austen")

    items = _page(fresh_client).items

    assert [(item.title, item.author) for item in items] == [
        ("Dune", "Frank Herbert"),
        ("Emma", "Jane Austen"),
    ]


def test_index_lists_books_in_the_order_they_were_added(fresh_client: FlaskClient) -> None:
    titles = ["Zebra", "Apple", "Mango"]
    for title in titles:
        _add(fresh_client, title)

    assert [item.title for item in _page(fresh_client).items] == titles


def test_index_escapes_book_text_so_markup_is_shown_literally(fresh_client: FlaskClient) -> None:
    _add(fresh_client, "<b>Bold</b>", "A")

    items = _page(fresh_client).items

    assert [item.title for item in items] == ["<b>Bold</b>"]


def test_index_on_plain_load_shows_no_error_region(fresh_client: FlaskClient) -> None:
    assert _page(fresh_client).error is None


def test_index_has_add_form_with_title_and_author_fields(fresh_client: FlaskClient) -> None:
    page = _page(fresh_client)

    assert "/add" in page.form_actions
    assert set(page.inputs) >= {"title", "author"}


def test_index_gives_each_book_a_remove_form_for_its_id(fresh_client: FlaskClient) -> None:
    ids = [_add(fresh_client, f"Book {n}") for n in range(3)]

    remove_actions = [item.remove_action for item in _page(fresh_client).items]

    assert remove_actions == [f"/remove/{book_id}" for book_id in ids]


def test_index_uses_no_script_tags(fresh_client: FlaskClient) -> None:
    assert _page(fresh_client).script_tags == 0


# POST /add


def test_add_valid_book_answers_303_redirecting_to_index(fresh_client: FlaskClient) -> None:
    response = fresh_client.post("/add", data={"title": "Dune", "author": "Frank Herbert"})

    assert response.status_code == 303
    assert response.headers["Location"] == "/"


def test_add_valid_book_stores_it_readable_through_the_list(fresh_client: FlaskClient) -> None:
    fresh_client.post("/add", data={"title": "Dune", "author": "Frank Herbert"})

    listed = fresh_client.get("/books").get_json()

    assert [(book["title"], book["author"]) for book in listed] == [("Dune", "Frank Herbert")]


def test_added_book_appears_at_the_end_of_the_page_list(fresh_client: FlaskClient) -> None:
    _add(fresh_client, "First")

    fresh_client.post("/add", data={"title": "Second", "author": "A"})

    assert [item.title for item in _page(fresh_client).items] == ["First", "Second"]


@pytest.mark.parametrize(
    "form",
    [
        {"title": "", "author": "Frank Herbert"},
        {"title": "Dune", "author": ""},
        {"title": "", "author": ""},
        {"title": "   ", "author": "Frank Herbert"},
        {"title": "Dune", "author": "   "},
        {"author": "Frank Herbert"},
        {"title": "Dune"},
        {},
    ],
)
def test_add_rejects_empty_or_missing_fields_with_400(fresh_client: FlaskClient, form: dict) -> None:
    response = fresh_client.post("/add", data=form)

    assert response.status_code == 400


def test_add_rejection_renders_visible_error_region(fresh_client: FlaskClient) -> None:
    rejected = fresh_client.post("/add", data={"title": "", "author": "Frank Herbert"})

    parser = _PageParser()
    parser.feed(rejected.get_data(as_text=True))

    assert parser.page.error is not None
    assert parser.page.error.strip() != ""


def test_add_rejection_stores_nothing(fresh_client: FlaskClient) -> None:
    _add(fresh_client, "Existing")
    before = _listed_ids(fresh_client)

    fresh_client.post("/add", data={"title": "", "author": "Frank Herbert"})

    assert _listed_ids(fresh_client) == before


def test_add_rejection_leaves_the_list_unchanged_on_the_page(fresh_client: FlaskClient) -> None:
    _add(fresh_client, "Existing", "Someone")
    before = [(item.title, item.author) for item in _page(fresh_client).items]

    fresh_client.post("/add", data={"title": "Dune", "author": "  "})

    assert [(item.title, item.author) for item in _page(fresh_client).items] == before


def test_add_rejection_echoes_entered_values_into_the_form(fresh_client: FlaskClient) -> None:
    response = fresh_client.post("/add", data={"title": "Dune", "author": "  "})

    parser = _PageParser()
    parser.feed(response.get_data(as_text=True))

    assert parser.page.inputs["title"] == "Dune"
    assert parser.page.inputs["author"] == "  "


def test_add_rejection_does_not_show_an_error_on_the_next_plain_load(fresh_client: FlaskClient) -> None:
    fresh_client.post("/add", data={"title": "", "author": "A"})

    assert _page(fresh_client).error is None


# POST /remove/{book_id}


def test_remove_answers_303_redirecting_to_index(fresh_client: FlaskClient) -> None:
    book_id = _add(fresh_client, "Dune")

    response = fresh_client.post(f"/remove/{book_id}")

    assert response.status_code == 303
    assert response.headers["Location"] == "/"


def test_removed_book_is_absent_from_the_page(fresh_client: FlaskClient) -> None:
    book_id = _add(fresh_client, "Dune")

    fresh_client.post(f"/remove/{book_id}")

    assert _page(fresh_client).items == []


def test_removed_book_is_absent_from_the_next_list_read(fresh_client: FlaskClient) -> None:
    book_id = _add(fresh_client, "Dune")

    fresh_client.post(f"/remove/{book_id}")

    assert book_id not in _listed_ids(fresh_client)


def test_removed_book_does_not_reappear_on_later_page_loads(fresh_client: FlaskClient) -> None:
    book_id = _add(fresh_client, "Dune")
    fresh_client.post(f"/remove/{book_id}")

    first = _page(fresh_client)
    second = _page(fresh_client)

    assert first.items == []
    assert second.items == []


def test_removing_a_middle_book_keeps_the_others_in_order(fresh_client: FlaskClient) -> None:
    _add(fresh_client, "First")
    middle = _add(fresh_client, "Middle")
    _add(fresh_client, "Last")

    fresh_client.post(f"/remove/{middle}")

    assert [item.title for item in _page(fresh_client).items] == ["First", "Last"]


def test_removing_the_last_book_shows_the_empty_message(fresh_client: FlaskClient) -> None:
    book_id = _add(fresh_client, "Dune")

    fresh_client.post(f"/remove/{book_id}")

    assert _page(fresh_client).shows_no_books_message is True


def test_removing_an_unknown_id_answers_303_redirecting_to_index(fresh_client: FlaskClient) -> None:
    response = fresh_client.post("/remove/999999")

    assert response.status_code == 303
    assert response.headers["Location"] == "/"


def test_removing_an_unknown_id_leaves_the_list_unchanged(fresh_client: FlaskClient) -> None:
    created = [_add(fresh_client, f"Book {n}") for n in range(2)]

    fresh_client.post("/remove/999999")

    assert _listed_ids(fresh_client) == created


def test_removing_the_same_book_twice_answers_303_both_times(fresh_client: FlaskClient) -> None:
    book_id = _add(fresh_client, "Dune")

    first = fresh_client.post(f"/remove/{book_id}")
    second = fresh_client.post(f"/remove/{book_id}")

    assert first.status_code == 303
    assert second.status_code == 303

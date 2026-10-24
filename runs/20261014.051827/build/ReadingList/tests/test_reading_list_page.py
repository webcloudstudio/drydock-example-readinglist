from html.parser import HTMLParser

import pytest


class _ElementCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.elements: list[tuple[str, dict[str, str]]] = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, {name: value or "" for name, value in attrs}))


def _elements(body: str) -> list[tuple[str, dict[str, str]]]:
    collector = _ElementCollector()
    collector.feed(body)
    collector.close()
    return collector.elements


def _by_id(elements, element_id):
    matches = [attrs for _, attrs in elements if attrs.get("id") == element_id]
    assert len(matches) == 1, f"expected exactly one element with id {element_id!r}"
    return matches[0]


def _tag_for_id(elements, element_id):
    matches = [tag for tag, attrs in elements if attrs.get("id") == element_id]
    assert len(matches) == 1, f"expected exactly one element with id {element_id!r}"
    return matches[0]


@pytest.fixture
def page(web_client):
    response = web_client.get("/")
    return response.get_data(as_text=True)


def test_get_root_returns_200_html(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.mimetype == "text/html"


def test_root_page_is_repeatable(web_client):
    first = web_client.get("/").get_data(as_text=True)
    second = web_client.get("/").get_data(as_text=True)
    assert first == second


def test_root_rejects_post_with_405(web_client):
    assert web_client.post("/").status_code == 405


def test_root_page_form_posts_to_books(page):
    form = _by_id(_elements(page), "add-book")
    assert form["method"] == "post"
    assert form["action"] == "/books"


def test_root_page_has_text_input_for_title(page):
    elements = _elements(page)
    title = _by_id(elements, "title")
    assert title["name"] == "title"
    assert title["type"] == "text"


def test_root_page_has_text_input_for_author(page):
    elements = _elements(page)
    author = _by_id(elements, "author")
    assert author["name"] == "author"
    assert author["type"] == "text"


def test_root_page_has_exactly_one_submit_control(page):
    elements = _elements(page)
    submit_buttons = [attrs for tag, attrs in elements if tag == "button" and attrs.get("type") == "submit"]
    assert len(submit_buttons) == 1


def test_root_page_has_error_slot_for_title_beside_form(page):
    assert _tag_for_id(_elements(page), "title-error") == "span"


def test_root_page_has_error_slot_for_author_beside_form(page):
    assert _tag_for_id(_elements(page), "author-error") == "span"


def test_root_page_has_ordered_list_for_books(page):
    assert _tag_for_id(_elements(page), "books") == "ol"


def test_root_page_does_not_embed_stored_books(web_client):
    before = web_client.get("/").get_data(as_text=True)
    web_client.post("/books", json={"title": "Dune", "author": "Frank Herbert"})
    after = web_client.get("/").get_data(as_text=True)
    assert before == after


def test_routes_the_page_calls_add_list_and_remove_a_book(web_client):
    added = web_client.post("/books", json={"title": "Dune", "author": "Frank Herbert"})
    assert added.status_code == 201
    book_id = added.get_json()["id"]

    listing = web_client.get("/books")
    assert listing.status_code == 200
    assert listing.get_json() == [{"id": book_id, "title": "Dune", "author": "Frank Herbert"}]

    removed = web_client.delete(f"/books/{book_id}")
    assert removed.status_code == 204

    assert web_client.get("/books").get_json() == []


def test_routes_the_page_calls_keep_books_in_the_order_added(web_client):
    first = web_client.post("/books", json={"title": "A", "author": "One"}).get_json()
    second = web_client.post("/books", json={"title": "B", "author": "Two"}).get_json()
    third = web_client.post("/books", json={"title": "C", "author": "Three"}).get_json()
    assert [book["id"] for book in web_client.get("/books").get_json()] == [first["id"], second["id"], third["id"]]


def test_removing_unknown_book_returns_404_for_the_page(web_client):
    assert web_client.delete("/books/999999999").status_code == 404


def test_submission_with_empty_title_returns_400_naming_title_for_the_page(web_client):
    response = web_client.post("/books", json={"title": "", "author": "Frank Herbert"})
    assert response.status_code == 400
    assert response.get_json() == {"field": "title"}


def test_submission_with_empty_author_returns_400_naming_author_for_the_page(web_client):
    response = web_client.post("/books", json={"title": "Dune", "author": ""})
    assert response.status_code == 400
    assert response.get_json() == {"field": "author"}

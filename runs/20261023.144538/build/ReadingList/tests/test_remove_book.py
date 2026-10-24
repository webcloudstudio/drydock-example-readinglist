"""Remove a book: POST /books/{id}/delete removes a stored book, and answers 404 for an unknown id.

Every test reaches removal only through the public HTTP routes. Each test creates the books it
needs through POST /books, reads their ids back from GET /books, and removes the books it created
before finishing. Titles carry a unique marker so the shared store can hold them safely.
"""

import uuid

import pytest


def _unique(label: str) -> str:
    """Return a title no other test or run has used, so the shared store can hold it safely."""
    return f"RemoveTest-{label}-{uuid.uuid4().hex}"


@pytest.fixture
def owned_ids(web_client):
    """Collect the ids a test adds, then remove exactly those books that are still listed afterwards."""
    ids: list[int] = []
    yield ids
    listed = {row["id"] for row in _listing(web_client)}
    for book_id in ids:
        if book_id in listed:
            web_client.post(f"/books/{book_id}/delete")


def _listing(client) -> list[dict]:
    """Return every listed book, read back through GET /books, in the order listed."""
    return client.get("/books").get_json()


def _add(client, owned_ids: list[int], label: str) -> int:
    """Add a book through POST /books, read its id back through GET /books, and own it."""
    title = _unique(label)
    response = client.post("/books", data={"title": title, "author": "Remove Author"})
    assert response.status_code == 303
    matches = [row["id"] for row in _listing(client) if row["title"] == title]
    assert len(matches) == 1
    owned_ids.append(matches[0])
    return matches[0]


def _owned_listing(client, owned_ids: list[int]) -> list[int]:
    """Return the ids of the books this test owns that are still listed, in the order listed."""
    return [row["id"] for row in _listing(client) if row["id"] in owned_ids]


def _unknown_id(client) -> int:
    """Return an id no listed book carries: one past the highest listed id, offset well clear of it."""
    return max((row["id"] for row in _listing(client)), default=0) + 100000


def test_removing_a_known_book_answers_303_to_start_page(web_client, owned_ids):
    book_id = _add(web_client, owned_ids, "redirect")

    response = web_client.post(f"/books/{book_id}/delete")

    assert response.status_code == 303
    assert response.headers["Location"] == "/"


def test_removed_book_is_absent_from_the_next_listing(web_client, owned_ids):
    book_id = _add(web_client, owned_ids, "omitted")

    web_client.post(f"/books/{book_id}/delete")

    assert book_id not in [row["id"] for row in _listing(web_client)]


def test_removing_one_book_leaves_the_others_listed(web_client, owned_ids):
    first = _add(web_client, owned_ids, "others-first")
    removed = _add(web_client, owned_ids, "others-removed")
    last = _add(web_client, owned_ids, "others-last")

    web_client.post(f"/books/{removed}/delete")

    listed = _owned_listing(web_client, owned_ids)
    assert first in listed
    assert last in listed
    assert removed not in listed


def test_removing_the_middle_book_keeps_the_others_in_their_original_order(web_client, owned_ids):
    first = _add(web_client, owned_ids, "middle-first")
    middle = _add(web_client, owned_ids, "middle-middle")
    last = _add(web_client, owned_ids, "middle-last")

    web_client.post(f"/books/{middle}/delete")

    assert _owned_listing(web_client, owned_ids) == [first, last]


def test_removing_the_first_book_keeps_the_rest_in_order(web_client, owned_ids):
    first = _add(web_client, owned_ids, "first-first")
    second = _add(web_client, owned_ids, "first-second")
    third = _add(web_client, owned_ids, "first-third")

    web_client.post(f"/books/{first}/delete")

    assert _owned_listing(web_client, owned_ids) == [second, third]


def test_removing_the_last_book_keeps_the_rest_in_order(web_client, owned_ids):
    first = _add(web_client, owned_ids, "last-first")
    second = _add(web_client, owned_ids, "last-second")
    last = _add(web_client, owned_ids, "last-last")

    web_client.post(f"/books/{last}/delete")

    assert _owned_listing(web_client, owned_ids) == [first, second]


def test_remaining_books_keep_their_id_title_and_author(web_client, owned_ids):
    first = _add(web_client, owned_ids, "keep-first")
    middle = _add(web_client, owned_ids, "keep-middle")
    last = _add(web_client, owned_ids, "keep-last")
    before = {row["id"]: row for row in _listing(web_client) if row["id"] in owned_ids}

    web_client.post(f"/books/{middle}/delete")

    after = {row["id"]: row for row in _listing(web_client) if row["id"] in owned_ids}
    assert after == {first: before[first], last: before[last]}


def test_unknown_id_answers_404(web_client, owned_ids):
    _add(web_client, owned_ids, "unknown")

    response = web_client.post(f"/books/{_unknown_id(web_client)}/delete")

    assert response.status_code == 404


def test_unknown_id_removes_nothing(web_client, owned_ids):
    first = _add(web_client, owned_ids, "unknown-first")
    second = _add(web_client, owned_ids, "unknown-second")

    web_client.post(f"/books/{_unknown_id(web_client)}/delete")

    assert _owned_listing(web_client, owned_ids) == [first, second]


def test_removing_the_same_book_twice_answers_303_then_404(web_client, owned_ids):
    book_id = _add(web_client, owned_ids, "twice")

    first = web_client.post(f"/books/{book_id}/delete")
    second = web_client.post(f"/books/{book_id}/delete")

    assert first.status_code == 303
    assert second.status_code == 404


def test_removing_the_same_book_twice_does_not_disturb_the_other_books(web_client, owned_ids):
    first = _add(web_client, owned_ids, "twice-first")
    removed = _add(web_client, owned_ids, "twice-removed")
    last = _add(web_client, owned_ids, "twice-last")

    web_client.post(f"/books/{removed}/delete")
    web_client.post(f"/books/{removed}/delete")

    assert _owned_listing(web_client, owned_ids) == [first, last]


def test_non_integer_id_answers_404_and_removes_nothing(web_client, owned_ids):
    book_id = _add(web_client, owned_ids, "non-integer")

    response = web_client.post("/books/not-a-number/delete")

    assert response.status_code == 404
    assert _owned_listing(web_client, owned_ids) == [book_id]


def test_get_on_delete_path_is_not_a_removal(web_client, owned_ids):
    book_id = _add(web_client, owned_ids, "get-method")

    response = web_client.get(f"/books/{book_id}/delete")

    assert response.status_code == 405
    assert _owned_listing(web_client, owned_ids) == [book_id]

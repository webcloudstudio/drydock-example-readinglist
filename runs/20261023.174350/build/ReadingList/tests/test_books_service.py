"""Book service: add, list, remove, and validate, exercised directly against a per-test store."""

import pytest

from app_server.services import books as book_service
from persistence import Database
from persistence.schema import Book


def test_add_book_returns_stored_book_with_supplied_fields(fresh_db: Database) -> None:
    book = book_service.add_book(fresh_db, "Dune", "Frank Herbert")

    assert isinstance(book, Book)
    assert isinstance(book.id, int)
    assert book.title == "Dune"
    assert book.author == "Frank Herbert"


def test_add_book_persists_the_book(fresh_db: Database) -> None:
    book = book_service.add_book(fresh_db, "Emma", "Jane Austen")

    assert fresh_db.books.get(id=book.id) == book


def test_add_book_rejects_empty_title_without_storing(fresh_db: Database) -> None:
    with pytest.raises(ValueError, match="title"):
        book_service.add_book(fresh_db, "", "Jane Austen")

    assert book_service.list_books(fresh_db) == []


def test_list_books_on_empty_store_returns_empty_list(fresh_db: Database) -> None:
    assert book_service.list_books(fresh_db) == []


def test_list_books_returns_books_in_order_added(fresh_db: Database) -> None:
    added = [book_service.add_book(fresh_db, f"Title {n}", "A") for n in range(3)]

    assert book_service.list_books(fresh_db) == added


def test_remove_book_returns_true_and_drops_book_from_list(fresh_db: Database) -> None:
    keep = book_service.add_book(fresh_db, "Keep", "A")
    gone = book_service.add_book(fresh_db, "Gone", "A")

    assert book_service.remove_book(fresh_db, gone.id) is True

    assert book_service.list_books(fresh_db) == [keep]


def test_remove_book_returns_false_for_unknown_id(fresh_db: Database) -> None:
    assert book_service.remove_book(fresh_db, 999999) is False


def test_remove_book_second_removal_returns_false(fresh_db: Database) -> None:
    book = book_service.add_book(fresh_db, "Once", "A")
    book_service.remove_book(fresh_db, book.id)

    assert book_service.remove_book(fresh_db, book.id) is False


@pytest.mark.parametrize(
    "title, author",
    [("Dune", "Frank Herbert"), ("  Dune  ", "  Frank Herbert  "), ("T", "A")],
)
def test_validate_book_input_accepts_non_blank_text(title: str, author: str) -> None:
    assert book_service.validate_book_input(title, author) is None


@pytest.mark.parametrize(
    "title, author, field",
    [
        ("", "A", "title"),
        ("   ", "A", "title"),
        (None, "A", "title"),
        (42, "A", "title"),
        ("T", "", "author"),
        ("T", "\t\n", "author"),
        ("T", None, "author"),
    ],
)
def test_validate_book_input_names_the_offending_field(title, author, field: str) -> None:
    with pytest.raises(ValueError) as error:
        book_service.validate_book_input(title, author)

    assert field in str(error.value)


def test_validate_book_input_names_both_fields_when_both_are_blank() -> None:
    with pytest.raises(ValueError) as error:
        book_service.validate_book_input("", "")

    assert "title" in str(error.value)
    assert "author" in str(error.value)

import pytest

from persistence import PersistenceError, UnknownOperation
from persistence.schema import Book
from persistence.testing import db_session as open_session


def test_new_store_lists_no_books(db_session):
    assert db_session.books.list() == []


def test_create_returns_id_and_get_reads_back_the_book(db_session):
    book_id = db_session.books.create(title="Dune", author="Frank Herbert")
    assert db_session.books.get(id=book_id) == Book(id=book_id, title="Dune", author="Frank Herbert")


def test_get_returns_none_for_absent_id(db_session):
    assert db_session.books.get(id=999) is None


def test_list_returns_books_in_insertion_order(db_session):
    first = db_session.books.create(title="A", author="One")
    second = db_session.books.create(title="B", author="Two")
    third = db_session.books.create(title="C", author="Three")
    assert [book.id for book in db_session.books.list()] == [first, second, third]


def test_delete_removes_only_the_named_book(db_session):
    keep = db_session.books.create(title="Keep", author="Author")
    drop = db_session.books.create(title="Drop", author="Author")
    assert db_session.books.delete(id=drop) == 1
    assert db_session.books.get(id=drop) is None
    assert db_session.books.get(id=keep).title == "Keep"


def test_delete_of_absent_id_removes_nothing(db_session):
    db_session.books.create(title="Only", author="Author")
    assert db_session.books.delete(id=999) == 0
    assert len(db_session.books.list()) == 1


def test_undeclared_verb_raises_unknown_operation(db_session):
    with pytest.raises(UnknownOperation):
        db_session.books.update(id=1, title="Nope")


def test_stores_are_isolated_between_sessions():
    with open_session() as first:
        first.books.create(title="Only in first", author="Author")
    with open_session() as second:
        assert second.books.list() == []


def test_persistence_error_is_a_runtime_error():
    assert issubclass(PersistenceError, RuntimeError)

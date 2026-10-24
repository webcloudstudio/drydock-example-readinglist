"""Books persistence: the declared repository operations, read back through the public interface."""

from persistence import Database


def test_create_returns_stored_book_with_supplied_fields(db_session: Database) -> None:
    row = db_session.books.create(title="Dune", author="Frank Herbert")

    assert row.id is not None
    assert row.title == "Dune"
    assert row.author == "Frank Herbert"


def test_create_assigns_distinct_ids(db_session: Database) -> None:
    first = db_session.books.create(title="First", author="A")
    second = db_session.books.create(title="Second", author="A")

    assert first.id != second.id


def test_get_reads_back_created_book(db_session: Database) -> None:
    created = db_session.books.create(title="Emma", author="Jane Austen")

    fetched = db_session.books.get(id=created.id)

    assert fetched.id == created.id
    assert fetched.title == "Emma"
    assert fetched.author == "Jane Austen"


def test_get_returns_none_for_unknown_id(db_session: Database) -> None:
    created = db_session.books.create(title="Gone", author="A")
    db_session.books.delete(id=created.id)

    assert db_session.books.get(id=created.id) is None


def test_list_returns_books_in_order_added(db_session: Database) -> None:
    titles = ["ac-list-first", "ac-list-second", "ac-list-third"]
    created_ids = [db_session.books.create(title=t, author="ac-list-author").id for t in titles]

    listed_ids = [row.id for row in db_session.books.list()]

    mine = [i for i in listed_ids if i in created_ids]
    assert mine == created_ids


def test_delete_removes_book_from_next_list(db_session: Database) -> None:
    keep = db_session.books.create(title="ac-delete-keep", author="ac-delete-author")
    gone = db_session.books.create(title="ac-delete-gone", author="ac-delete-author")

    db_session.books.delete(id=gone.id)

    listed_ids = [row.id for row in db_session.books.list()]
    assert gone.id not in listed_ids
    assert keep.id in listed_ids


def test_created_book_is_visible_in_the_same_transaction(db_session: Database) -> None:
    before = {row.id for row in db_session.books.list()}

    created = db_session.books.create(title="Visible", author="A")

    after = {row.id for row in db_session.books.list()}
    assert after == before | {created.id}

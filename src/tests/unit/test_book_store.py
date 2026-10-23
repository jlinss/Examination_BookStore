from src.book_store import BookStore

def test_add_book():
    store = BookStore()

    book = store.addBook("New Book Added", "Test Python")

    assert book["title"] == "New Book Added"
    assert book["author"] == "Test Python"
    assert book["id"] == 1



def test_two_books_dif_id():
    store = BookStore()

    first_book = store.addBook("New Book Added", "Test Python")
    second_book = store.addBook("New Book Added Two", "Test Python")

    assert first_book["id"] != second_book["id"]

    assert len(store.books) == 2





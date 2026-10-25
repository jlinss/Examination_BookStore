from src.book_store import BookStore


def test_add_book():
    store = BookStore()

    book = store.addBook("Testbok", "Testförfattare")

    assert book["id"] == 1
    assert book["title"] == "Testbok"
    assert book["author"] == "Testförfattare"
    assert len(store.books) == 1


def test_add_book_to_favorites():
    store = BookStore()
    book = store.addBook("Testbok", "Testförfattare")

    result = store.toggleFavorite(book["id"])

    assert result is True
    assert book in store.favorites_books.books


def test_remove_book_from_favorites():
    store = BookStore()
    book = store.addBook("Testbok", "Testförfattare")

    store.toggleFavorite(book["id"])
    store.toggleFavorite(book["id"])

    assert book not in store.favorites_books.books


def test_repeated_toggle_favorite_calls():
    store = BookStore()
    book = store.addBook("Testbok", "Testförfattare")

    store.toggleFavorite(book["id"])
    assert book in store.favorites_books.books

    store.toggleFavorite(book["id"])
    assert book not in store.favorites_books.books

    store.toggleFavorite(book["id"])
    assert book in store.favorites_books.books


def test_book_store_and_favorite_books_work_together():
    store = BookStore()
    book1 = store.addBook("Bok ett", "Författare ett")
    book2 = store.addBook("Bok två", "Författare två")

    store.toggleFavorite(book1["id"])
    store.toggleFavorite(book2["id"])

    assert len(store.books) == 2
    assert len(store.favorites_books.books) == 2

    store.toggleFavorite(book1["id"])

    assert book1 not in store.favorites_books.books
    assert book2 in store.favorites_books.books

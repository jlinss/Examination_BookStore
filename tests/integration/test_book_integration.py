from src.book_store import BookStore
from src.fav_books import FavoriteBooks
from playwright.sync_api import sync_playwright


def test_book_store_uses_favorite_book():
    store = BookStore()

    assert isinstance(store.favorites_books, FavoriteBooks)


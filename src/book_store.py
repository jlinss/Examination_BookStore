from src.fav_books import FavoriteBooks

class BookStore:
    def __init__(self, books=None):
        self.books = []
        self.favorites_books = FavoriteBooks()
        self.next_id = 1

        if books:
            for book in books:
                self.addBook(book["title"], book["author"])


    def addBook(self, title, author):
        book = {
            "id": self.next_id,
            "title": title,
            "author": author,
        }

        self.books.append(book)
        self.next_id += 1

        return book


    def toggleFavorite(self, book_id):
        book = next (
            (book for book in self.books if book["id"] == book_id),
            None
        )

        if book is None:
            return False

        if book in self.favorites_books.books:
            self.favorites_books.remove(book)
        else:
            self.favorites_books.add(book)

        return True

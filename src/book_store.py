from src.fav_books import FavoriteBooks
class BookStore:
    def __init__(self):
        self.books = []
        self.favorite_books = FavoriteBooks()
        self.next_id = 1

        if books:
            for book in books:
                self.addBook(book["title"], book["author"])


    def addBook(self, author, title):
        book = {
            "id": self.next_id,
            "title": title,
            "author": author,
        }
from src.fav_books import FavoriteBooks


def test_add_book():
    favorites = FavoriteBooks()
    book = {"id": 1, "title": "New Book Added", "author": "Test Python"}

    favorites.add(book)

    assert book in favorites.books


def test_remove_book():
    favorites = FavoriteBooks()
    book = {"id": 1, "title": "New Book Added", "author": "Test Python"}

    favorites.remove(book)

    assert book not in favorites.books


def test_remove_book_unexistent():
    favorites = FavoriteBooks()
    book = {"id": 1, "title": "New Book Added", "author": "Test Python"}

    favorites.remove(book)

    assert favorites.books == []


def test_add_book_twice():
    favorites = FavoriteBooks()
    book = {"id": 1, "title": "New Book Added", "author": "Test Python"}

    favorites.add(book)
    favorites.add(book)

    assert len(favorites.books) == 1


"""{ id: 1, title: "Ormar på ett plan: En Python-berättelse", author: "Guido van Rossum" },
{ id: 2, title: "The Pragmatic Procrastinator", author: "Dave Thomasson" },)
{ id: 3, title: "Python för folk som hatar ormar", author: "Monty Pythonsson" },
{ id: 4, title: "Why Your Tests Are Lying to You", author: "Kent Backdoor" },
{ id: 5, title: "Playwright: Click It Till You Make It", author: "Microslop Browserdóttir" },
{ id: 6, title: "Git Blame and Other Ways to Lose Friends", author: "Linus Torvalds" },
{ id: 7, title: "Learn Python in 21 Years", author: "Sams Teachyourself" },
{ id: 8, title: "Agile Is a Feeling", author: "Jeff Sutherland" },
{ id: 9, title: "Playwright: Waiting for Selectors", author: "Samuel Barclay Beckett" },
{ id: 10, title: "Stack Overflow: A Love Story", author: "Copy Pasta" },
{ id: 11, title: "My First Regex (And Last)", author: "Larry Wallström" },
{ id: 12, title: "The Developer Who Knew Nothing", author: "George R.R. Martin" },
{ id: 13, title: "The Bugs are Coming", author: "George R.R. Martin" },"""

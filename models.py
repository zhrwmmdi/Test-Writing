class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __str__(self):
        return f"{self.title} by {self.author} ({self.copies} copy available)"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name == other.name
        return False

    def borrow_book(self, book):
        if book.copies > 0:
            book.copies -= 1
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.copies += 1
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"{self.name} (Borrowed books: {len(self.borrowed_books)})"


class Library:
    books = []
    users = []

    @classmethod
    def add_book(cls, book):
        if isinstance(book, list):
            cls.books.extend(book)
        else:
            cls.books.append(book)

    @classmethod
    def add_user(cls, user):
        if isinstance(user, list):
            cls.users.extend(user)
        else:
            cls.users.append(user)

    @classmethod
    def find_book(cls, title):
        for book in cls.books:
            if book.title == title:
                return book
        return None

    @classmethod
    def find_user(cls, name):
        for user in cls.users:
            if user.name == name:
                return user
        return None

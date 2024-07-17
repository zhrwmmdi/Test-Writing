class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        copies (int): The number of copies available in the library.

    Methods:
        __eq__(other): Checks equality with another Book instance.
        __str__(): Returns a string representation of the book.
    """
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
    """
    Represents a user of the library.

    Attributes:
        name (str): The name of the user.
        borrowed_books (list): A list of books currently borrowed by the user.

    Methods:
        __eq__(other): Checks equality with another User instance.
        borrow_book(book): Allows the user to borrow a book if available.
        return_book(book): Allows the user to return a borrowed book.
        __str__(): Returns a string representation of the user.
    """
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
    """
    Represents the library management system.

    Attributes:
        books (list): A list of books available in the library.
        users (list): A list of registered users in the library.

    Methods:
        add_book(book): Adds a book or a list of books to the library.
        add_user(user): Adds a user or a list of users to the library.
        find_book(title): Finds a book by title in the library.
        find_user(name): Finds a user by name in the library.
    """
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

import unittest

from models import User, Book, Library


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.b1 = Book('13 reasons why', 'John', 5)
        self.b3 = Book('Maskh', 'Kafka', 1)
        self.b4 = Book('Gratitude', 'Randa Bran', 0)
        self.b2 = Book('Why do men love bitches?', 'Sheri', 2)
        self.b5 = Book('Why do men love bitches?', 'Sheri', 7)
        self.u2 = User('Reza')
        self.u1 = User('Zahra')
        self.u3 = User('Elham')
        self.u4 = User('Majid')
        self.u5 = User('Reza')

        books = [self.b1, self.b2]
        users = [self.u1, self.u2]

        Library.add_book(books)
        Library.add_user(users)

        Library.add_book(self.b3)
        Library.add_user(self.u3)

    def tearDown(self):
        print('TEST COMPLETED SUCCESSFULLY!')


class LibraryTestCase(BaseTest):

    def setUp(self):
        super().setUp()

    def test_attributes(self):
        self.assertTrue(hasattr(Library, 'books'))
        self.assertTrue(hasattr(Library, 'users'))

    def test_add_book(self):
        self.assertIn(self.b1, Library.books)
        self.assertIn(self.b3, Library.books)
        self.assertNotIn(self.b4, Library.books)

    def test_add_user(self):
        self.assertIn(self.u1, Library.users)
        self.assertIn(self.u3, Library.users)
        self.assertNotIn(self.u4, Library.users)

    def test_find_user(self):
        self.assertIsNone(Library.find_user(self.u4))
        found_user = Library.find_user('Zahra')
        self.assertEqual(found_user, self.u1)

    def test_find_book(self):
        self.assertIsNone(Library.find_book(self.b4))
        found_book = Library.find_book('13 reasons why')
        self.assertEqual(found_book, self.b1)


class UserTestCase(BaseTest):

    def setUp(self):
        super().setUp()

    def test_attributes(self):
        self.assertTrue(hasattr(self.u1, 'name'))
        self.assertTrue(hasattr(self.u1, 'borrowed_books'))

        user_pr = self.u1.__str__()
        self.assertEqual(user_pr, 'Zahra (Borrowed books: 0)')

        self.assertFalse(self.u1.__eq__(self.b1))
        self.assertTrue(self.u2.__eq__(self.u5))

    def test_user_borrow_book(self):
        self.assertTrue(self.u1.borrow_book(self.b1))
        self.assertFalse(self.u1.borrow_book(self.b4))

        self.assertEqual(self.b1.copies, 4)
        self.assertIn(self.b1, self.u1.borrowed_books)

    def test_return_book(self):
        self.u1.borrow_book(self.b2)
        self.u1.return_book(self.b2)

        self.assertTrue(self.b2.copies == 2)
        self.assertNotIn(self.b2, self.u2.borrowed_books)
        self.assertFalse(self.u2.return_book(self.b2))  # redundant


class BookTestCase(BaseTest):

    def setUp(self):
        super().setUp()

    def test_attributes(self):
        self.assertTrue(hasattr(self.b1, 'title'))
        self.assertTrue(hasattr(self.b1, 'author'))
        self.assertTrue(hasattr(self.b1, 'copies'))

        book_pr = self.b1.__str__()
        self.assertEqual(book_pr, '13 reasons why by John (5 copy available)')

        self.assertTrue(self.b2.__eq__(self.b5))
        self.assertFalse(self.b1.__eq__(self.u1))

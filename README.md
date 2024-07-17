# Library Management System

This project is here to demonstrate my skills in project test writing, it is a 
simple library management system that allows users to borrow and return books. 
It demonstrates basic object-oriented programming concepts in Python, with an 
emphasis on unit testing.


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contact Information](#contact-information)

## Introduction
This project is primarily developed to demonstrate proficiency in writing unit 
tests. It is a simple Library Management System that provides functionalities 
for adding books and users, borrowing and returning books, and tracking the 
availability of books. Each component of the library management system is 
accompanied by comprehensive unit tests to ensure the reliability and 
correctness of the system.

The project leverages Python's unittest framework to create, manage, and run 
tests, ensuring that all functionalities are working as intended.


## Features

- **Book Management**: Add and manage books in the library.
- **User Management**: Add users to the library and manage the borrowed books.
- **Borrowing and Returning**: Users can borrow books if available and return
them when finished.


## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/zhrwmmdi/Test-Writing.git
    cd Test
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies** (if any):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can use the classes to create books, users, and manage the library. Here’s a simple example:

```python
from library_management.book import Book
from library_management.user import User
from library_management.library import Library

# Create books
book1 = Book("1984", "George Orwell", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 2)

# Add books to the library
Library.add_book(book1)
Library.add_book(book2)

# Create a user
user = User("Alice")

# Add user to the library
Library.add_user(user)

# User borrows a book
user.borrow_book(book1)

# Check borrowed books
print(user)
```
## Testing
To ensure code functionality, unit tests are provided in the tests/unit_tests 
directory. You can run the tests using:
```bash
python -m unittest discover -s tests
```
## Contact Information
Author: Zahra Mohammadi

Email: zahra.mmdi2003@gmail.com



📚 Library Management System

Project Description
The Library Management System is a menu-driven Python application that helps manage books and library members. It allows users to add and remove books, register members, borrow and return books, search for books, and display borrowed books.
The system uses Object-Oriented Programming (OOP) concepts and stores library information in a JSON file so that the data can be saved and loaded even after the program is closed.

Features

- Add Books: Add new books with a unique book ID, title, and author.
- Remove Books: Remove books that are not currently borrowed.
- Register Members: Register new library members with unique member IDs.
- Borrow Books: Allow members to borrow available books.
- Return Books: Allow members to return books they have borrowed.
- Borrowing Rules:
  - A book can be borrowed by only one member at a time.
  - A member can borrow a maximum of 3 books.
  - A member cannot borrow the same book twice.
  - Only the member who borrowed a book can return it.
- **Search Books:** Search for books by title or author.
- **Display All Books:** View all books in the library with their availability status.
- **Display Borrowed Books:** View borrowed books and the names of the members holding them.
- **JSON Storage:** Save library data to a JSON file and load it when the program starts.

Classes Used

1. Book
Represents an individual book in the library.
- `book id`: Unique ID of the book.
- `title`: Name of the book.
- `author`: Name of the book's author.
- `is borrowed`: Indicates whether the book is borrowed.
- `borrowed by`: Stores the ID of the member who borrowed the book.

Methods:
- `__str__()`: Returns a readable description of the book.
- `__repr__()`: Returns a developer-friendly representation of the book.

2. Member
Represents a registered library member.
- `member id`: Unique ID of the member.
- `name`: Name of the member.
- `borrowed books`: Stores the IDs of books borrowed by the member.

Methods:
- `__str__()`: Returns a readable description of the member.
- `__repr__()`: Returns a developer-friendly representation of the member.

3. Library
Manages all books and members and performs library operations.

Attributes:
- `books`: Dictionary containing all book objects.
- `members`: Dictionary containing all member objects.

Methods:
- `add book()`: Adds a book to the library.
- `remove book()`: Removes a book if it is not borrowed.
- `register member()`: Registers a new member.
- `borrow book()`: Allows a member to borrow a book.
- `return book()`: Allows a member to return a book.
- `search books()`: Searches books by title or author.
- `display books()`: Displays all books.
- `display borrowed books()`: Displays borrowed books and their holders.
- `save to file()`: Saves library data into a JSON file.
- `load from file()`: Loads saved library data from a JSON file.
- `__str__()` and `__repr__()`: Provide string representations of the library.

Learning Outcomes

- Understanding classes and objects in Python.
- Applying Object-Oriented Programming concepts.
- Using constructors and special methods such as `__str__()` and `__repr__()`.
- Working with dictionaries and lists.
- Implementing real-world borrowing and returning rules.
- Performing file handling using JSON.
- Understanding class methods using `@classmethod`.
- Building a menu-driven application.

Conclusion

The Library Management System provides a simple way to manage books and members using Python. It demonstrates the practical use of OOP, data structures, and JSON file handling in a real-world application.
"""Classes: Book, Member and Library 
• Add and remove books; register members 
• Borrow and return, with rules: no double-borrowing, and a maximum of 3 books per member 
• Search books by title or author 
• List all borrowed books and who holds them 
• Save and load library data to JSON; menu-driven interface 
•  str  and  repr  on every class"""
import json
import os
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrowed_by = None

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

    def __repr__(self):
        return f"Book({self.book_id!r}, {self.title!r}, {self.author!r})"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"

    def __repr__(self):
        return f"Member({self.member_id!r}, {self.name!r})"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def __str__(self):
        return f"Library: {len(self.books)} books, {len(self.members)} members"
    def __repr__(self):
        return f"Library(books={len(self.books)}, members={len(self.members)})"
    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists.")
            return
        self.books[book.book_id] = book
        print("Book added successfully.")
    def remove_book(self, book_id):
        book = self.books.get(book_id)

        if book is None:
            print("Book not found.")
        elif book.is_borrowed:
            print("Cannot remove a borrowed book.")
        else:
            del self.books[book_id]
            print("Book removed successfully.")
    def register_member(self, member):
        if member.member_id in self.members:
            print("Member ID already exists.")
            return

        self.members[member.member_id] = member
        print("Member registered successfully.")

    def borrow_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)
        if book is None:
            print("Book not found.")
            return
        if member is None:
            print("Member not found.")
            return
        if book.is_borrowed:
            print("This book is already borrowed.")
            return
        if len(member.borrowed_books) >= 3:
            print("Maximum limit of 3 books reached.")
            return

        book.is_borrowed = True
        book.borrowed_by = member_id
        member.borrowed_books.append(book_id)
        print("Book borrowed successfully.")

    def return_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)

        if book is None or member is None:
            print("Book or member not found.")
            return
        if not book.is_borrowed:
            print("Book is not currently borrowed.")
            return
        if book.borrowed_by != member_id:
            print("This book was not borrowed by this member.")
            return

        book.is_borrowed = False
        book.borrowed_by = None
        member.borrowed_books.remove(book_id)
        print("Book returned successfully.")

    def search_books(self, keyword):
        keyword = keyword.lower()
        found = False

        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                print(book)
                found = True
        if not found:
            print("No matching books found.")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books.values():
            print(f"ID: {book.book_id} | {book}")

    def display_borrowed_books(self):
        found = False
        for book in self.books.values():
            if book.is_borrowed:
                member = self.members.get(book.borrowed_by)
                if member:
                    print( f"{book.title} - Held by: "f"{member.name} (ID: {member.member_id})" )
                    found = True
        if not found:
            print("No books are currently borrowed.")

    def save_to_file(self, filename="library.json"):
        data = {
            "books": [
                {"book_id": book.book_id,"title": book.title,"author": book.author,"is_borrowed": book.is_borrowed,"borrowed_by": book.borrowed_by}
                for book in self.books.values()
            ],
            "members": [
                {"member_id": member.member_id,"name": member.name,"borrowed_books": member.borrowed_books}
                for member in self.members.values()
            ]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Library data saved successfully.")

    @classmethod
    def load_from_file(cls, filename="library.json"):
        library = cls()

        if not os.path.exists(filename):
            return library
        with open(filename, "r") as file:
                data = json.load(file)

        for item in data.get("books", []):
                book = Book(item["book_id"],item["title"],item["author"])
                book.is_borrowed = item["is_borrowed"]
                book.borrowed_by = item["borrowed_by"]
                library.books[book.book_id] = book

        for item in data.get("members", []):
                member = Member(item["member_id"],item["name"])
                member.borrowed_books = item["borrowed_books"]
                library.members[member.member_id] = member
        print("Library data loaded successfully.")
            # return cls()
        return library

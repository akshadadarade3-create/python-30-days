from library_management import Book, Member, Library
def main():
    library = Library.load_from_file()
    while True:
        print("\n1. Add Book \n2.Remove Book \n3. Register Member\n4. Borrow Book\n5. Return Book\n6. Search Books\n7. Display All Books\n8. Display Borrowed Books\n9. Save Library Data\n10. Exit")
    
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            book_id = input("Enter book ID: ").strip()
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()

            if not book_id or not title or not author:
                print("All details are required.")
            else:
                book = Book(book_id, title, author)
                library.add_book(book)
        elif choice == "2":
            book_id = input("Enter book ID: ").strip()
            library.remove_book(book_id)
        elif choice == "3":
            member_id = input("Enter member ID: ").strip()
            name = input("Enter member name: ").strip()

            if not member_id or not name:
                print("All details are required.")
            else:
                member = Member(member_id, name)
                library.register_member(member)
        
        elif choice == "4":
            book_id = input("Enter book ID: ").strip()
            member_id = input("Enter member ID: ").strip()
            library.borrow_book(book_id, member_id)

        elif choice == "5":
            book_id = input("Enter book ID: ").strip()
            member_id = input("Enter member ID: ").strip()
            library.return_book(book_id, member_id)

        elif choice == "6":
            keyword = input("Enter title or author: ").strip()
            library.search_books(keyword)
        elif choice == "7":
            library.display_books()
        elif choice == "8":
            library.display_borrowed_books()
        elif choice == "9":
            library.save_to_file()
        elif choice == "10":
            library.save_to_file()
            print("Exit")
            break
        else:
            print("Enter a valid number")

if __name__ == "__main__":
    main()


# Library Management System (OOP)

class Library:
    def __init__(self):
        # Store book titles and their availability
        self.books = {}

    def add_book(self, title):
        title = title.strip()

        if not title:
            print("Book title cannot be empty.")
        elif title in self.books:
            print("Book already exists in the library.")
        else:
            self.books[title] = True
            print(f"'{title}' added successfully.")

    def remove_book(self, title):
        if title not in self.books:
            print("Book not found in the library.")
        elif not self.books[title]:
            print("Cannot remove an issued book.")
        else:
            del self.books[title]
            print(f"'{title}' removed successfully.")

    def issue_book(self, title):
        if title not in self.books:
            print("Book not found in the library.")
        elif not self.books[title]:
            print("Book is already issued.")
        else:
            self.books[title] = False
            print(f"'{title}' issued successfully.")

    def return_book(self, title):
        if title not in self.books:
            print("Book not found in the library.")
        elif self.books[title]:
            print("This book was not issued.")
        else:
            self.books[title] = True
            print(f"'{title}' returned successfully.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
            return

        print("\nLibrary Books:")
        for title, available in self.books.items():
            status = "Available" if available else "Issued"
            print(f"{title} - {status}")


# Main program
library = Library()

library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Object-Oriented Programming")

library.display_books()

library.issue_book("Python Programming")
library.display_books()

library.return_book("Python Programming")
library.remove_book("Data Structures")

library.display_books()

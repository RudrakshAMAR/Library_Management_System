import os
from datetime import datetime
from models import Book, Member, Loan
from storage import read_csv, write_csv, append_csv
from auth import login, get_role

BOOKS_FILE = "data/books.csv"
MEMBERS_FILE = "data/members.csv"
LOANS_FILE = "data/loans.csv"

# Add a new book to the library
def add_book():
    isbn = input("ISBN: ")
    title = input("Title: ")
    author = input("Author: ")
    total = int(input("Total Copies: "))
    available = total
    book = {"isbn": isbn, "title": title, "author": author, "total": total, "available": available}
    append_csv(BOOKS_FILE, book, ["isbn", "title", "author", "total", "available"])
    print(f"Book '{title}' added.")

# Search for books by title or author
def search_books():
    books = read_csv(BOOKS_FILE)
    keyword = input("Enter book title or author: ").lower()
    results = [book for book in books if keyword in book['title'].lower() or keyword in book['author'].lower()]
    print("Search Results:")
    for book in results:
        print(f"{book['title']} by {book['author']} (Available: {book['available']})")

# Issue a book to a member
def issue_book():
    member_id = input("Member ID: ")
    isbn = input("ISBN of the book to issue: ")
    loans = read_csv(LOANS_FILE)
    loan_id = str(len(loans) + 1)
    issue_date = datetime.today().strftime('%Y-%m-%d')
    due_date = (datetime.today() + timedelta(days=14)).strftime('%Y-%m-%d')
    loan = {"loan_id": loan_id, "member_id": member_id, "isbn": isbn, "issue_date": issue_date, "due_date": due_date, "return_date": ""}
    append_csv(LOANS_FILE, loan, ["loan_id", "member_id", "isbn", "issue_date", "due_date", "return_date"])
    print("Book issued.")

# Return a book
def return_book():
    loan_id = input("Loan ID to return: ")
    loans = read_csv(LOANS_FILE)
    for loan in loans:
        if loan["loan_id"] == loan_id:
            loan["return_date"] = datetime.today().strftime('%Y-%m-%d')
            write_csv(LOANS_FILE, loans, ["loan_id", "member_id", "isbn", "issue_date", "due_date", "return_date"])
            print("Book returned.")
            return
    print("Loan ID not found.")

# Librarian menu options
def librarian_menu():
    while True:
        print("\n1. Add Book\n2. Issue Book\n3. Return Book\n4. Search Books\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            search_books()
        elif choice == "5":
            break

# Member menu options
def member_menu():
    while True:
        print("\n1. Search Books\n2. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            search_books()
        elif choice == "2":
            break

# Main function to start the application
def main():
    role = get_role()
    user = login(role)
    print(f"Welcome, {user}!")
    if role == "Librarian":
        librarian_menu()
    else:
        member_menu()

if __name__ == "__main__":
    main()

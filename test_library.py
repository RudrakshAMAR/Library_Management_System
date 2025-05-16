import pytest
from storage import read_csv, write_csv, append_csv

BOOKS_FILE = "data/books.csv"

def cleanup_test_book(isbn):
    books = read_csv(BOOKS_FILE)
    books = [book for book in books if book['isbn'] != isbn]
    if books:
        fieldnames = books[0].keys()
    else:
        fieldnames = ['isbn', 'title', 'author', 'total', 'available']
    write_csv(BOOKS_FILE, books, fieldnames=fieldnames)

def test_add_book():
    test_book = {
        "isbn": "1234567890",
        "title": "Test Book",
        "author": "Test Author",
        "total": "3",
        "available": "3"
    }

    append_csv(BOOKS_FILE, test_book, ["isbn", "title", "author", "total", "available"])

    books = read_csv(BOOKS_FILE)
    added_book = next((book for book in books if book['isbn'] == test_book["isbn"]), None)

    assert added_book is not None
    assert added_book['title'] == test_book['title']
    assert added_book['author'] == test_book['author']
    assert added_book['total'] == test_book['total']
    assert added_book['available'] == test_book['available']

    cleanup_test_book(test_book["isbn"])

def test_search_books():
    test_book = {
        "isbn": "9876543210",
        "title": "Search Test",
        "author": "Tester",
        "total": "2",
        "available": "2"
    }

    append_csv(BOOKS_FILE, test_book, ["isbn", "title", "author", "total", "available"])

    books = read_csv(BOOKS_FILE)
    found_books = [book for book in books if "Search" in book['title']]

    assert len(found_books) > 0
    assert found_books[0]['title'] == test_book['title']

    cleanup_test_book(test_book["isbn"])

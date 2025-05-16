# Library Management System

## Overview
This is a simple Library Management System built in Python. It supports two roles:
- **Librarian:** Can add books, issue books, return books, and search for books.
- **Member:** Can search for books.

The system uses CSV files to store data about books, members, and loans.

## Features
- Role-based login (Librarian/Member)
- Add new books (Librarian)
- Search books by title or author
- Issue books to members (Librarian)
- Return books (Librarian)
- Data persistence using CSV files

## Setup
1. Make sure you have Python 3 installed.
2. Download or clone the repository.
3. Ensure the `data/` folder contains `books.csv`, `members.csv`, and `loans.csv`.
4. Run the main program:

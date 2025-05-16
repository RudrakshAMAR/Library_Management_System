from datetime import datetime

class Book:
    def __init__(self, isbn, title, author, total, available):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total = total
        self.available = available

class Member:
    def __init__(self, member_id, name, email, join_date=None):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.join_date = join_date or datetime.today().strftime('%Y-%m-%d')

class Loan:
    def __init__(self, loan_id, member_id, isbn, issue_date, due_date, return_date=""):
        self.loan_id = loan_id
        self.member_id = member_id
        self.isbn = isbn
        self.issue_date = issue_date
        self.due_date = due_date
        self.return_date = return_date

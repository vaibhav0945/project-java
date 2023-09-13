import datetime

class Transaction:
    def __init__(self, student, book):
        self.student = student
        self.book = book
        self.issue_date = datetime.datetime.now()
        self.due_date = self.issue_date + datetime.timedelta(days=15)  # 15-day reading period
        self.return_date = None
        self.fine = 0

    def return_book(self):
        self.return_date = datetime.datetime.now()
        if self.return_date > self.due_date:
            days_overdue = (self.return_date - self.due_date).days
            self.fine = days_overdue * 1  # Adjust the fine rate as needed
        self.book.mark_as_available()

    def to_dict(self):
        return {
            "student_id": self.student.student_id,
            "book_id": self.book.book_id,
            "issue_date": self.issue_date.strftime("%Y-%m-%d"),
            "due_date": self.due_date.strftime("%Y-%m-%d"),
            "return_date": self.return_date.strftime("%Y-%m-%d") if self.return_date else None,
            "fine": self.fine
        }

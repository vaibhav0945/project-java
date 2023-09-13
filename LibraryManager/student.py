class Student:

    def __init__(self, student_id, name, address):
        self.student_id = student_id
        self.name = name
        self.address = address
        self.books_issued = []
        self.fine = 0
        Student.reading_period = 15
        self.transactions = []

    def issue_book(self, book):
        self.books_issued.append(book)
        transaction = Transaction(self, book)
        self.transactions.append(transaction)

    def return_book(self, book):
        self.books_issued.remove(book)
        # Implement logic to return a book
        for transaction in self.transactions:
            if transaction.book == book and not transaction.return_date:
                transaction.return_book()
                return

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "address": self.address,
            "books_issued": [book.book_id for book in self.books_issued],
            "fine": self.fine
        }

    def no_of_books_issued(self):
        return len(self.books_issued)

    def calculate_fine(self):
        total_fine = sum(transaction.fine for transaction in self.transactions if transaction.fine > 0)
        return total_fine


# import json
#
# class Book:
#     def __init__(self, book_id, title, author, is_available=True):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.is_available = is_available
#
#     def assign_book(self):
#         # Implement logic to assign a book to a student
#
#     def mark_as_lost(self):
#         self.is_available = False
#
#     def mark_as_available(self):
#         self.is_available = True
#
#     def to_dict(self):
#         return {
#             "book_id": self.book_id,
#             "title": self.title,
#             "author": self.author,
#             "is_available": self.is_available
#         }
#
#     @classmethod
#     def from_dict(cls, data):
#         return cls(
#             book_id=data["book_id"],
#             title=data["title"],
#             author=data["author"],
#             is_available=data["is_available"]
#         )
#
#     @staticmethod
#     def save_to_json(books):
#         with open("books.json", "w") as file:
#             data = [book.to_dict() for book in books]
#             json.dump(data, file)
#
#     @staticmethod
#     def load_from_json():
#         try:
#             with open("books.json", "r") as file:
#                 data = json.load(file)
#                 return [Book.from_dict(item) for item in data]
#         except FileNotFoundError:
#             return []
#
# # Similar modifications for other entity classes (Student, Staff, Author)
# def save_all_data(books, students, staff, authors):
#     Book.save_to_json(books)
#     # Similar calls for other entities
#
# def load_all_data():
#     books = Book.load_from_json()
#     students = Student.load_from_json()
#     staff = Staff.load_from_json()
#     authors = Author.load_from_json()
#     return books, students, staff, authors
#
# if __name__ == "__main__":
#     books, students, staff, authors = load_all_data()
#
#     while True:
#         print("Library Management System")
#         print("1. Add Book")
#         print("2. Add Borrower")
#         # ... (other menu options)
#
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#             title = input("Enter book title: ")
#             author = input("Enter author: ")
#             isbn = input("Enter ISBN: ")
#             book = Book(len(books) + 1, title, author, is_available=True)
#             books.append(book)
#         # ... (other menu options)
#
#         save_all_data(books, students, staff, authors)
#
# # Inside your main loop (while True):
# if choice == "2":
#     name = input("Enter student name: ")
#     address = input("Enter student address: ")
#     student_id = len(students) + 1  # Generate a unique student ID
#     student = {
#         "student_id": student_id,
#         "name": name,
#         "address": address,
#         "books_issued": [],
#         "fine": 0
#     }
#     students.append(student)
#     print(f"Student added successfully. Student ID: {student_id}")
#
# # Inside your main loop (while True)
# if choice == "3":
#     book_id = int(input("Enter book ID: "))
#     borrower_id = int(input("Enter borrower ID: "))
#     if assign_book(books, students, book_id, borrower_id):
#         print("Book assigned successfully.")
#     else:
#         print("Book not available or invalid book/borrower ID.")
#
# if choice == "4":
#     book_id = int(input("Enter book ID: "))
#     if return_book(books, students, book_id):
#         print("Book returned successfully.")
#     else:
#         print("Book not found or overdue.")
#
#
# # ... (other menu options)
#
# # Implement assign_book and return_book functions for handling book assignments and returns.
#
# def assign_book(books, students, book_id, borrower_id):
#     book = find_book_by_id(books, book_id)
#     student = find_student_by_id(students, borrower_id)
#
#     if book and student:
#         if book["is_available"]:
#             book["is_available"] = False
#             student["books_issued"].append(book_id)
#             return True
#     return False
#
#
# def return_book(books, students, book_id):
#     book = find_book_by_id(books, book_id)
#
#     if book and not book["is_available"]:
#         book["is_available"] = True
#         for student in students:
#             if book_id in student["books_issued"]:
#                 student["books_issued"].remove(book_id)
#         return True
#     return False
#
#
# # Implement find_book_by_id and find_student_by_id functions for searching books and students by ID.
#
# def find_book_by_id(books, book_id):
#     for book in books:
#         if book["book_id"] == book_id:
#             return book
#     return None
#
#
# def find_student_by_id(students, student_id):
#     for student in students:
#         if student["student_id"] == student_id:
#             return student
#     return None
#
#
# from datetime import datetime, timedelta
#
# # Inside your Book class:
# class Book:
#     # ... (previous code)
#
#     def calculate_fine(self, return_date):
#         due_date = datetime.strptime(return_date, "%Y-%m-%d")
#         if self.is_available:
#             return 0  # No fine if the book is available
#         elif due_date < datetime.now():
#             # Calculate fine for overdue books (e.g., $1 per day)
#             days_overdue = (datetime.now() - due_date).days
#             return days_overdue * 1  # Adjust the fine rate as needed
#         else:
#             return 0  # No fine if returned on or before the due date
#
#
# # Inside your assign_book function:
# def assign_book(books, students, book_id, borrower_id):
#     book = find_book_by_id(books, book_id)
#     student = find_student_by_id(students, borrower_id)
#
#     if book and student:
#         if book["is_available"]:
#             book["is_available"] = False
#             due_date = datetime.now() + timedelta(days=15)  # 15-day reading period
#             student["books_issued"].append({"book_id": book_id, "due_date": due_date.strftime("%Y-%m-%d")})
#             return True
#     return False
#
# # Inside your main loop:
# if choice == "5":
#     student_id = int(input("Enter student ID: "))
#     student = find_student_by_id(students, student_id)
#     if student:
#         print("Books Borrowed:")
#         for record in student["books_issued"]:
#             book = find_book_by_id(books, record["book_id"])
#             print(f"Book ID: {book['book_id']}, Title: {book['title']}, Due Date: {record['due_date']}")
#     else:
#         print("Student not found.")
#
#
# # Inside your Book class:
# class Book:
#     # ... (previous code)
#
#     def reserve_book(self, student_id):
#         if not self.is_available:
#             if "reserved_by" not in self:
#                 self["reserved_by"] = student_id
#                 return True
#         return False
#
#     def release_reservation(self):
#         if "reserved_by" in self:
#             del self["reserved_by"]
#
#
# # Inside your return_book function:
# def return_book(books, students, book_id):
#     book = find_book_by_id(books, book_id)
#
#     if book:
#         if not book["is_available"]:
#             due_date = datetime.strptime(book["due_date"], "%Y-%m-%d")
#             if datetime.now() > due_date:
#                 # Calculate and collect fines
#                 fine = book.calculate_fine(datetime.now().strftime("%Y-%m-%d"))
#                 students = [s for s in students if book_id not in [b["book_id"] for b in s["books_issued"]]]
#                 book["is_available"] = True
#                 return True, fine
#             else:
#                 students = [s for s in students if book_id not in [b["book_id"] for b in s["books_issued"]]]
#                 book["is_available"] = True
#                 return True, 0  # No fine if returned on or before the due date
#     return False, 0
#
#

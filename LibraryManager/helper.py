class Helper:
    def find_book_by_id(books, book_id):
        for book in books:
            if book["book_id"] == book_id:
                return book
        return None

    def search_book_by_name(books, title):
        found_books = []
        for book in books:
            if title.lower() in book.title.lower():
                found_books.append(book)
        return found_books
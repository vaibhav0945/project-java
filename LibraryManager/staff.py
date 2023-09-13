class Staff:
    def __init__(self, staff_id, name, address):
        self.staff_id = staff_id
        self.name = name
        self.address = address

    def to_dict(self):
        return {
            "staff_id": self.staff_id,
            "name": self.name,
            "address": self.address
        }

    def add_book(self, book):

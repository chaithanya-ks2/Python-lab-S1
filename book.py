class Publisher:
    book_catalog = {}
    def __init__(self, name="ABC"):
        self.name = name
        self.books = []
        self.authors = []
    def add_book(self, author, title):
        if author in self.book_catalog.keys():
            self.book_catalog[author] += [title]
        else:
            self.book_catalog[author] = [title]



class Books(Publisher):
    def __init__(self, title, author):
        super().__init__()
        self.title = title
        self.author = author


class Python(Books):
    def __init__(Self, price, no_pages):
        super.__init__()
        self.price = price
        self.no_pages = no_pages



pub1 = Publisher("ABC")
print(pub1.name)
pub1.add_book("Abhishek", "Gokul")
print(pub1.book_catalog)
pub1.add_book("Abhishek", "Bhavana")
print(pub1.book_catalog)

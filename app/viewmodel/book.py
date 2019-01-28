"""
created by caiminming
"""


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, books, keyword):
        self.total = books.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in books.books]


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages'] or ''
        self.author = book['author']
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']

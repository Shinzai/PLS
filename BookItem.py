import Book

class BookItem(Book.Book):
    def __init__(self, Book, itemId, status):
        self.status = status
        self.itemId = itemId
        self.book = Book

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def getItemId(self):
        return self.itemId

    def getBook(self):
        return self.book

    def getBookTitle(self):
        return self.book.getTitle()

    def getBookAuthor(self):
        return self.book.getAuthor()
    
    def getBookCountry(self):
        return self.book.getCountry()

    def getBookYear(self):
        return self.book.getYear()

    def getBookPages(self):
        return self.book.getYear()
    
    def getBookLink(self):
        return self.book.getLink()

    def getBookLanguage(self):
        return self.book.getLanguage()

    def getBookImagelink(self):
        return self.book.getImagelink()
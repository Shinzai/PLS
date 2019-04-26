class BookItem():
    def __init__(self, Book, ItemId, status=True):
        self.status = status
        self.ItemId = ItemId
        self.book = Book

    def getStatus(self):
        if self.status == True:
            return 'The book is available.'
        else:
            return 'The book is unavailable'
           
    def getItemId(self):
        return self.ItemId

    def getBook(self):
        return self.book
        
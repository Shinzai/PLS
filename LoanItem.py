class LoanItem():

    def __init__(self, customer, bookItem, dateLoaned, dateEnd, CopyID):
        self.customer = customer
        self.bookItem = bookItem
        self.dateLoaned = dateLoaned
        self.dateEnd = dateEnd
        self.CopyID = CopyID


    def getCustomer(self):
        return self.customer

    def getBookItem(self):
        return self.bookItem

    def getDateLoaned(self):
        return self.dateLoaned

    def getDateEnd(self):
        return self.dateEnd
    
    

class Author():

    def __init__(self, name, age, *writtenBooks):
        self.name = name
        self.age = age
        self.writtenBooks = writtenBooks
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
        
    def getWrittenBooks(self):
        return self.writtenBooks
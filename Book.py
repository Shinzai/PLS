class Book():
    def __init__(self, author,country,imageLink,language,link,pages,title,year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.title = title
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getLanguage(self):
        return self.language

    def getPages(self):
        return self.pages

    def getYear(self):
        return self.year

    def getCountry(self):
        return self.country
    
    def getLink(self):
        return self.link

    def getImagelink(self):
        return self.imageLink
    
    
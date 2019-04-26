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
    
    def getAuthor(self):
        return self.author
    
    def getCountry(self):
        return self.country
    
    def getImageLink(self):
        return self.imageLink
    
    def getLanguage(self):
        return self.language
    
    def getLink(self):
        return self.link
    
    def getPages(self):
        return self.pages
    
    def getTitle(self):
        return self.title
    
    def getYear(self):
        return self.year

    def DisplayBookDetails(self,author,country,imageLink,language,link,pages,title,year):
        return 'The author is: ' + author + '\nThe book details are: ' + country + ', ' + imageLink + ', ' + language + ', ' + link + ', ' + pages + ', ' + title + ', ' + year + '.'



        
    



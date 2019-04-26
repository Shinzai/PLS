class Person():
    def __init__(self, id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber):
        self.id = id
        self.gender = gender
        self.nationality = nationality
        self.firstName = firstName
        self.lastName = lastName
        self.streetAddress = streetAddress
        self.zipCode = zipCode
        self.city = city
        self.emailAddress = emailAddress
        self.username = username
        self.phoneNumber = phoneNumber
    
    def getId(self):
        return self.id

    def getGender(self):
        return self.gender
    
    def getNationality(self):
        return self.nationality

    def getName(self):
        return self.firstName + " " + self.lastName

    def getAddress(self):
        return self.streetAddress

    def getZip(self):
        return self.zipCode

    def getCity(self):
        return self.city

    def getMail(self):
        return self.emailAddress

    def getUsername(self):
        return self.username

    def getPhone(self):
        return self.phoneNumber



class librarian(Person):
    def __init__(self, id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber):
        super().__init__(id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber)
        self.name = self.firstName + " " + self.lastName

class customer(Person):
    def __init__(self, id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber):
            super().__init__(id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber)
        

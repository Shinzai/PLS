class customer(object):

    def __init__(self, id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber):
        self.id = id
        self.firstName = firstName
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
        

    def printCustomer(self): 
        return self.firstName + " " + self.lastName + "\nID", self.id



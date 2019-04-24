class librarian(Person):

    def __init__(self,name,username):
        super().__init__(id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber)
        self.name = firstName + " " + lastName
        self.username = username

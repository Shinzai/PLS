import csv
import json

class Person():
    def __init__(self, id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber, status):
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
        self.status = status
    
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

    def getStatus(self):
        return self.status

class librarian(Person):
    def __init__(self, id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber, status):
        super().__init__(id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber, status)
        self.name = self.firstName + " " + self.lastName
        self.customerListData = []

    def backupData(self, customerList):
        for x in customerList:
            self.customerListData.append(x)

        with open('C:/temp/customers_backup.csv', mode='w', encoding = 'utf-8') as finalCsv:
            finalCsv_writer = csv.writer(finalCsv, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for x in self.customerListData:
                finalCsv_writer.writerow([x.id, x.gender, x.firstName, x.lastName, x.streetAddress, x.zipCode, x.city, x.emailAddress, x.username, x.phoneNumber])
        

    def loadData(self, listOfCustomers):
        with open('C:/temp/customers_backup.csv', mode='r', encoding = 'utf-8') as csv_file1:
            csv_reader1 = csv.DictReader(csv_file1)
            count = 0
            for row in csv_reader1:
                if count == 0:
                    count += 1
                csvCustomer = customer(count, f'{row["Gender"]}', f'{row["NameSet"]}', f'{row["GivenName"]}', f'{row["Surname"]}', f'{row["StreetAddress"]}', f'{row["ZipCode"]}', f'{row["City"]}', f'{row["EmailAddress"]}', f'{row["Username"]}', f'{row["TelephoneNumber"]}', f'{row["Status"]}')
                listOfCustomers.append(csvCustomer)
                count += 1
            return listOfCustomers

class customer(Person):
    def __init__(self, id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber, status):
            super().__init__(id, gender, nationality, firstName, lastName, streetAddress, zipCode, city, emailAddress, username, phoneNumber, status)

    def getUsername(self):
        return self.username
        

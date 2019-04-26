import json
import csv
import Person

customers = []
librarians = []

with open('librarian.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    count = 0
    for row in csv_reader:
        if count == 0:
            count += 1
        newLibrarian = Person.librarian(count, f'{row["Gender"]}', f'{row["NameSet"]}', f'{row["GivenName"]}', f'{row["Surname"]}', f'{row["StreetAddress"]}', f'{row["ZipCode"]}', f'{row["City"]}', f'{row["EmailAddress"]}', f'{row["Username"]}', f'{row["TelephoneNumber"]}')
        librarians.append(newLibrarian)

done = False         

while (done == False):
    userInput = input("Username: ")
    for x in librarians:
        if userInput == x.username:
            print("Welcome " + x.name)
            working = True
            while working == True:

                action = input("What would you like to do? type help for more information.\n")
                if action == "help":
                    print("Add Customer = customer.add\nLoad customers from csv file = customer.loadcsv\nload books from json file = book.loadjson\nlogout from system = logout\n")

                elif action == "customer.add":
                    id = len(customers) + 1
                    gender = input("Male or Female?\n")
                    nationality = input("Nationality?\n")
                    firstName = input("First name?\n")
                    lastName = input("Last name?\n")
                    streetAddress = input("Street address?\n")
                    zipCode = input("Zip code?\n")
                    city = input("City?\n")
                    email = input("Email address?\n")
                    phone = input("Phone number?\n")
                    username = input("What do you want to use as user name?\n")
                    
                    newCustomer =  Person.customer(id,gender,nationality,firstName,lastName,streetAddress, zipCode, city, email, username, phone)
                    customers.append(newCustomer)
                
                elif action == "customer.list":
                    if len(customers) >= 1:
                        for y in customers:
                            print(y.firstName + " " + y.lastName)
                    else:
                        print("No customers loaded!")

                elif action == "load.data":
                    customers = x.loadData(customers)

                elif action == "backup":
                    x.backupData(customers)
                    print("Data back-up made in C:\\temp")

                elif action == "quit":
                    working = False
    
    for x in customers:
        if userInput == x.username:
            print("Welcome " + x.firstName + " " + x.lastName)
    
            

    

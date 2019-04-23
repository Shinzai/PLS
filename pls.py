import json
import csv
import customer
import librarian

customers = []
librarians = []

with open('librarian.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    count = 0
    for row in csv_reader:
        if count == 0:
            count += 1
        newLibrarian = librarian.librarian(f'{row["name"]}', f'{row["username"]}')
        librarians.append(newLibrarian)

with open('customers.csv', mode='r', encoding = 'utf-8') as csv_file1:
    csv_reader1 = csv.DictReader(csv_file1)
    count = 0
    for row in csv_reader1:
        if count == 0:
            count += 1
        csvCustomer = customer.customer(count, f'{row["Gender"]}', f'{row["NameSet"]}', f'{row["GivenName"]}', f'{row["Surname"]}', f'{row["StreetAddress"]}', f'{row["ZipCode"]}', f'{row["City"]}', f'{row["EmailAddress"]}', f'{row["Username"]}', f'{row["TelephoneNumber"]}')
        customers.append(csvCustomer)
        count += 1

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
                    
                    # madeCustomer = librarian.customer.customer(id,gender,nationality,firstName,lastName,streetAddress, zipCode, city, email, username, phone)
                    # customers.append(madeCustomer)
                    newCustomer =  customer.customer(id,gender,nationality,firstName,lastName,streetAddress, zipCode, city, email, username, phone)
                    customers.append(newCustomer)
                
                elif action == "customer.list":
                    for x in customers:
                        print(x.firstName + " " + x.lastName)

                elif action == "quit":
                    with open('customers2.csv', mode='w', encoding = 'utf-8') as finalCsv:
                        finalCsv_writer = csv.writer(finalCsv, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        for x in customers:
                            finalCsv_writer.writerow([x.id, x.gender, x.firstName, x.lastName, x.streetAddress, x.zipCode, x.city, x.emailAddress, x.username, x.phoneNumber])
                    working = False
    
    for x in customers:
        if userInput == x.username:
            print("Welcome " + x.firstName + " " + x.lastName)
    
            

    
import json
import customer



data = {}
data['customers'] = []

done = False

while (done == False):
    userinput = input("\nWho is using the system?\nChoose Librarian or Customer.\n")
    if userinput == "Librarian" or userinput == "librarian":
        print("Librarian logged in.")
        librarianLoggedOn = True
        while librarianLoggedOn == True:
            userinput = input("What would you like to do? type help for more information.\n")
            if userinput == "help":
                print("Add Customer = customer.add\nLoad customers from csv file = customer.loadcsv\nload books from json file = book.loadjson\nlogout from system = logout\n")

            elif userinput == "customer.add":
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
                
                newCustomer = customer.customer(0,gender,nationality,firstName,lastName,streetAddress,zipCode,city,email,username,phone)
                print("New customer made!\n" + newCustomer.firstName + " " + newCustomer.lastName + "\nUsername: " + newCustomer.username + ".\n")
                
                data['customers'].append({
                    'Number':newCustomer.id,
                    'Gender':newCustomer.gender,
                    'firstName':newCustomer.firstName,
                    'lastName':newCustomer.lastName
                })

                with open('data.json','w') as outfile:
                    json.dump(data,outfile)

            
            elif userinput == "customer.load":
                print("load csv")
                print(len(data['customer']))

            elif userinput == "book.loadjson":
                print("load json")

            elif userinput == "logout":
                librarianLoggedOn = False


    elif userinput == "Customer" or userinput == "customer":
        print("Customer")


    else:
        print("wrong input")

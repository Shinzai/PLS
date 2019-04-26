import json
import csv
import Person
import Book
import BookItem
import uuid
import LoanItem
import datetime
import os

customers = []
librarians = []
books = []
bookItems = []
loanAdministration = []

now = datetime.datetime.now()
today = str(datetime.datetime.now().date())
weekLater = str((datetime.datetime.now() + datetime.timedelta(days=7)).date())

print(today, "\n", weekLater)


with open('librarian.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    count = 0
    for row in csv_reader:
        if count == 0:
            count += 1
        newLibrarian = Person.librarian(count, f'{row["Gender"]}', f'{row["NameSet"]}', f'{row["GivenName"]}', f'{row["Surname"]}', f'{row["StreetAddress"]}', f'{row["ZipCode"]}', f'{row["City"]}', f'{row["EmailAddress"]}', f'{row["Username"]}', f'{row["TelephoneNumber"]}', f'{row["Status"]}')
        librarians.append(newLibrarian)

with open('data/customers.csv', mode='r', encoding = 'UTF-8') as csv_file1:
    csv_reader1 = csv.DictReader(csv_file1)
    count = 0
    for row in csv_reader1:
        if count == 0:
            count += 1
        csvCustomer = Person.customer(count, f'{row["Gender"]}', f'{row["NameSet"]}', f'{row["GivenName"]}', f'{row["Surname"]}', f'{row["StreetAddress"]}', f'{row["ZipCode"]}', f'{row["City"]}', f'{row["EmailAddress"]}', f'{row["Username"]}', f'{row["TelephoneNumber"]}', f'{row["Status"]}')
        customers.append(csvCustomer)
        count += 1

with open('data/booksset1.json') as json_file:
    data = json.load(json_file)
    for p in data:
        newbook = Book.Book(p['author'], p['country'], p['imageLink'], p['language'], p['link'], p['pages'], p['title'], p['year'])
        books.append(newbook)

with open('data/bookitems.json') as getBookItems:
    bookData = json.load(getBookItems)
    for bd in bookData:
        booktitlename = bookData[bd]["title"]
        for booklist in books:
            if booklist.getTitle() == booktitlename:
                newBookItem = BookItem.BookItem(booklist, bookData[bd]["CopyID"], bookData[bd]["status"])
                bookItems.append(newBookItem)

with open('data/loanAdministration.json') as loanAdminFile:

    check = os.stat('G:/#Github/PLS/data/loanAdministration.json').st_size==0

    if check == False:

        loanData = json.load(loanAdminFile)
        for ld in loanData:
            customerusername = loanData[ld]["customerusername"]
            bookItemID = loanData[ld]["CopyID"]
            loandate = loanData[ld]["loandate"]
            enddate = loanData[ld]["endLoanDate"]
            for c in customers:
                if c.getUsername() == customerusername:
                    customer = c
            for bt in bookItems:
                if bt.getItemId() == bookItemID:
                    newLoanItem = LoanItem.LoanItem(customer, bt, loandate, enddate, bookItemID)
                    loanAdministration.append(newLoanItem)
    else:
        print("No Loans found.")

done = False

while (done == False):
    userInput = input("Username: ")
    for x in librarians:
        if userInput == x.username:
            print("Welcome " + x.name)
            working = True
            while (working == True):
                action = input("What would you like to do? Enter help for more information.\n")
                if action == "help":
                    print("Add customer = customer.add\Block customers account = customer.block\nUnblock customers account = customer.unblock")
                
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
                    
                    newCustomer =  Person.customer(id,gender,nationality,firstName,lastName,streetAddress, zipCode, city, email, username, phone, "active")
                    customers.append(newCustomer)

                elif action == "customer.block":
                    block = input("Who do you want to block? Please use customer.list for usernames.\n")
                    for c in customers:
                        if (c.username == block):
                            c.status = "unactive"

                elif action == "customer.unblock":
                    unblock = input("Who do you want to unblock? Please use customer.list for usernames.\n")
                    for c in customers:
                        if (c.username == unblock):
                            c.status = "active"

                elif action == "customer.list":
                    if len(customers) >= 1:
                        for c in customers:
                            print(c.firstName + " " + c.lastName + "\nUsername: " + c.username + "\nStatus: " + c.status + "\n")

                elif action == "add.bookitem":
                    whatBook = input("Choose what book you want to add. Give the specific title.\n")
                    for b in books:
                        if whatBook == b.getTitle():
                            thisBook = input("Do you want to add the book: " + b.getTitle() + "?\nType 'add' to add the book or 'cancel' to cancel this action.\n")
                            if thisBook == "add":
                                if len(bookItems) > 0:
                                    bookItems.reverse
                                    for s in bookItems:
                                        if s.getBookTitle() == b.getTitle():
                                            newBookItem = BookItem.BookItem(b, str(uuid.uuid4()), "available")
                                            bookItems.append(newBookItem)
                                            break
                                        else:
                                            newBookItem = BookItem.BookItem(b, str(uuid.uuid4()), "available")
                                            bookItems.append(newBookItem)
                                    bookItems.reverse
                                else:
                                    newBookItem = BookItem.BookItem(b, str(uuid.uuid4()), "available")
                                    bookItems.append(newBookItem)
                            elif thisBook == "cancel":
                                break

                elif action == "list.bookitems":
                    # for bi in bookItems:
                    #     print(bi.getBookInfo)
                    for testbooks in bookItems:
                        print("Title: ", testbooks.getBookTitle() , "\nCopyID: " , testbooks.getItemId(), "\nStatus: ", testbooks.getStatus(), "\n")
                
                elif action == "find.book":
                    whatBook = input("Choose what book you want to add. Give the specific title.\n")
                    for b in books:
                        if whatBook == b.getTitle():
                            print("Title: ", b.getTitle(), "\nAuthor: ", b.getAuthor(), "\nCountry: ", b.getCountry(), "\nLanguage: ", b.getLanguage(), "\nYear: ", b.getYear(), "\nPages: ", b.getPages(), "\n")
                
                elif action == "loan.administration":
                    for item in loanAdministration:
                        print("Bookinformation: \n\t", item.getBookItem().getBookTitle(), "\n\t", item.getBookItem().getBookAuthor(), "\nLend by customer: ", item.getCustomer().getName(), " on ", item.getDateLoaned(), "\nExpected return date: ", item.getDateEnd())
                
                
                elif action == "logout":
                    working = False

                    with open('data/customers.csv', mode = 'w', encoding = 'UTF-8', newline = '') as customerFile:
                        customerWriter = csv.writer(customerFile, delimiter = ',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
                        customerFile.truncate()
                        customerWriter.writerow(['Number', 'Gender', 'NameSet', 'GivenName', 'Surname', 'StreetAddress', 'ZipCode', 'City', 'EmailAddress', 'Username', 'TelephoneNumber', 'Status'])
                        for c in customers:
                            customerWriter.writerow([c.id, c.gender, c.nationality, c.firstName, c.lastName, c.streetAddress, c.zipCode, c.city, c.emailAddress, c.username, c.phoneNumber, c.status])

                    # print(bookItems['bookitems']['Title'])

                    with open('data/bookitems.json', 'w') as bookItemsFile:
                        itemList = {}
                        bookcounter = 1
                        for z in bookItems:
                            
                            r = {
                                "book" + str(bookcounter):{
                                    "title": z.getBookTitle(),
                                    "author": z.getBookAuthor(),
                                    "country": z.getBookCountry(),
                                    "imageLink": z.getBookImagelink(),
                                    "language": z.getBookLanguage(),
                                    "pages": z.getBookPages(),
                                    "year": z.getBookYear(),
                                    "link": z.getBookLink(),
                                    "status": z.getStatus(),
                                    "CopyID": z.getItemId()
                                }
                            }
                            bookcounter += 1
                            itemList.update(r)

                        json.dump(itemList, bookItemsFile)

    for x in customers:
        if x.getUsername() == userInput:
            print("Welcome " + x.firstName + " " + x.lastName + "\n")
            checking = True
            while checking == True:
                action = input("What do you want to do? Type help for more information.\n")
                if action == "help":
                    print("Find a book = find.book\n Lend a book = lend.book\n Return book = return.book\nLogout from the system = logout\n")

                elif action == "lend.book":
                    searchMethod = input("How do you want to search for a book? Choose:\nTitle, Author or Year\n")
                    if searchMethod == "Title":
                        whatBook = input("Please type the book title.\n")
                        for bi in bookItems:
                            if bi.getBookTitle() == whatBook:
                                newLoan = LoanItem.LoanItem(x, bi, today, weekLater)
                                bi.setStatus("unavailable")
                                loanAdministration.append(newLoan)
                                break

                elif action == "find.book":
                    searchMethod = input("How do you want to search for a book? Choose:\nTitle, Author or Year\n")
                    if searchMethod == "Title":
                        whatBook = input("Please type the book title.\n")
                        for bi in bookItems:
                            if bi.getBookTitle() == whatBook:
                                print("\nTitle: ", bi.getBookTitle(), "\nAuthor: ", bi.getBookAuthor(), "\nAvailability: ", bi.getStatus(), "\n")
                                
                elif action == "logout":
                    checking = False

                    with open('data/loanAdministration.json','w') as loanItemsFile:
                        loanList = {}
                        loancounter = 1

                        for l in loanAdministration:
                            m = {
                                "loan" + str(loancounter):{
                                    "customerusername":l.getCustomer().getUsername(),
                                    "customername":l.getCustomer().getName(),
                                    "booktitle":l.getBookItem().getBookTitle(),
                                    "bookauthor":l.getBookItem().getBookAuthor(),
                                    "loandate":l.getDateLoaned(),
                                    "endLoanDate":l.getDateEnd(),
                                    "CopyID":l.getBookItem().getItemId()
                                }
                            }               
                            loancounter += 1
                            loanList.update(m)
                        json.dump(loanList, loanItemsFile)

                    with open('data/bookitems.json', 'w') as bookItemsFile:
                        itemList = {}
                        bookcounter = 1
                        for z in bookItems:
                            
                            r = {
                                "book" + str(bookcounter):{
                                    "title": z.getBookTitle(),
                                    "author": z.getBookAuthor(),
                                    "country": z.getBookCountry(),
                                    "imageLink": z.getBookImagelink(),
                                    "language": z.getBookLanguage(),
                                    "pages": z.getBookPages(),
                                    "year": z.getBookYear(),
                                    "link": z.getBookLink(),
                                    "status": z.getStatus(),
                                    "CopyID": z.getItemId()
                                }
                            }
                            bookcounter += 1
                            itemList.update(r)

                        json.dump(itemList, bookItemsFile)
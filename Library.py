import json
import csv
import Person
import Book
import BookItem
import uuid
import LoanItem
import datetime
import os
from shutil import copyfile

customers = []
librarians = []
books = []
bookItems = []
loanAdministration = []

now = datetime.datetime.now()
today = str(datetime.datetime.now().date())
weekLater = str((datetime.datetime.now() + datetime.timedelta(days=7)).date())

librarianFileStatus = os.path.isfile('data/librarians.csv')
customerFileStatus = os.path.isfile('data/customers.csv')
bookssetFileStatus = os.path.isfile('data/booksset.json')
bookitemFileStatus = os.path.isfile('data/bookitems.json')
loanAdministrationFileStatus = os.path.isfile('data/loanAdministration.json')


if librarianFileStatus == True:
    with open('data/librarians.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        count = 0
        for row in csv_reader:
            if count == 0:
                count += 1
            newLibrarian = Person.librarian(count, f'{row["Gender"]}', f'{row["NameSet"]}', f'{row["GivenName"]}', f'{row["Surname"]}', f'{row["StreetAddress"]}', f'{row["ZipCode"]}', f'{row["City"]}', f'{row["EmailAddress"]}', f'{row["Username"]}', f'{row["TelephoneNumber"]}', f'{row["Status"]}')
            librarians.append(newLibrarian)
elif librarianFileStatus == False:
    newLibrarian = Person.librarian(1, 'x','x','x','x','x','x','x','x','admin','x','active')
    librarians.append(newLibrarian)

if customerFileStatus == True:
    with open('data/customers.csv', mode='r', encoding = 'UTF-8') as csv_file1:
        csv_reader1 = csv.DictReader(csv_file1)
        count = 0
        for row in csv_reader1:
            if count == 0:
                count += 1
            csvCustomer = Person.customer(count, f'{row["Gender"]}', f'{row["NameSet"]}', f'{row["GivenName"]}', f'{row["Surname"]}', f'{row["StreetAddress"]}', f'{row["ZipCode"]}', f'{row["City"]}', f'{row["EmailAddress"]}', f'{row["Username"]}', f'{row["TelephoneNumber"]}', f'{row["Status"]}')
            customers.append(csvCustomer)
            count += 1

if bookssetFileStatus == True:
    with open('data/booksset.json') as json_file:
        data = json.load(json_file)
        for p in data:
            newbook = Book.Book(p['author'], p['country'], p['imageLink'], p['language'], p['link'], p['pages'], p['title'], p['year'])
            books.append(newbook)

if bookitemFileStatus == True:
    with open('data/bookitems.json') as getBookItems:

        check = os.stat('data/bookitems.json').st_size==0

        if check == False:

            bookData = json.load(getBookItems)
            for bd in bookData:
                booktitlename = bookData[bd]["title"]
                for booklist in books:
                    if booklist.getTitle() == booktitlename:
                        newBookItem = BookItem.BookItem(booklist, bookData[bd]["CopyID"], bookData[bd]["status"])
                        bookItems.append(newBookItem)
        else:
            print("No book items found.")

if loanAdministrationFileStatus == True:
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
            print("No loans found.")

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
                                    for s in bookItems:
                                        if s.getBookTitle() == b.getTitle():
                                            newBookItem = BookItem.BookItem(b, str(uuid.uuid4()), "available")
                                            bookItems.append(newBookItem)  
                                else:
                                    newBookItem = BookItem.BookItem(b, str(uuid.uuid4()), "available")
                                    bookItems.append(newBookItem)
                            elif thisBook == "cancel":
                                break

                elif action == "list.bookitems":
                    # for bi in bookItems:
                    #     print(bi.getBookInfo)
                    for testbooks in bookItems:
                        print("\nTitle: ", testbooks.getBookTitle() , "\nCopyID: " , testbooks.getItemId(), "\nStatus: ", testbooks.getStatus(), "\n")

                elif action == "available.bookitems":
                    for testbooks in bookItems:
                        if testbooks.getStatus() == "available":
                            print("\nTitle: ", testbooks.getBookTitle() , "\nCopyID: " , testbooks.getItemId(), "\nStatus: ", testbooks.getStatus(), "\n")

                elif action == "list.books":
                    for realBooks in books:
                        print("\nTitle: ", realBooks.getTitle(), "\nAuthor: ", realBooks.getAuthor(), "\nLanguage: ", realBooks.getLanguage(), "\nPages: ", realBooks.getPages(), "\nYear: ", realBooks.getYear(), "\nCountry: ", realBooks.getCountry(), "\n")
                
                elif action == "find.book":
                    whatBook = input("Choose what book you want to add. Give the specific title.\n")
                    for b in books:
                        if whatBook == b.getTitle():
                            print("\nTitle: ", b.getTitle(), "\nAuthor: ", b.getAuthor(), "\nCountry: ", b.getCountry(), "\nLanguage: ", b.getLanguage(), "\nYear: ", b.getYear(), "\nPages: ", b.getPages(), "\n")
                
                elif action == "loan.administration":
                    for item in loanAdministration:
                        print("\nBookinformation: \n\tTitle:\t", item.getBookItem().getBookTitle(), "\n\tAuthor:\t", item.getBookItem().getBookAuthor(), "\nLend by customer: ", item.getCustomer().getName(), " on ", item.getDateLoaned(), "\nExpected return date: ", item.getDateEnd(), "\nCopy ID:\t", item.getBookItem().getItemId(), "\n")
                
                elif action == "make.backup":

                    with open('data/backup/customers.csv', mode = 'w', encoding = 'UTF-8', newline = '') as customerFile:
                        customerWriter = csv.writer(customerFile, delimiter = ',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
                        customerFile.truncate()
                        customerWriter.writerow(['Number', 'Gender', 'NameSet', 'GivenName', 'Surname', 'StreetAddress', 'ZipCode', 'City', 'EmailAddress', 'Username', 'TelephoneNumber', 'Status'])
                        for c in customers:
                            customerWriter.writerow([c.id, c.gender, c.nationality, c.firstName, c.lastName, c.streetAddress, c.zipCode, c.city, c.emailAddress, c.username, c.phoneNumber, c.status])

                    with open('data/backup/bookitems.json', 'w') as bookItemsFile:
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

                    with open('data/backup/loanAdministration.json','w') as loanItemsBackup:
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
                        json.dump(loanList, loanItemsBackup)

                    with open('data/backup/librarians.csv', mode = 'w', encoding = 'UTF-8', newline = '') as librariansBackup:
                        librarianWriter = csv.writer(librariansBackup, delimiter = ',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
                        librariansBackup.truncate()
                        librarianWriter.writerow(['Number', 'Gender', 'NameSet', 'GivenName', 'Surname', 'StreetAddress', 'ZipCode', 'City', 'EmailAddress', 'Username', 'TelephoneNumber', 'Status'])
                        for c in librarians:
                            librarianWriter.writerow([c.id, c.gender, c.nationality, c.firstName, c.lastName, c.streetAddress, c.zipCode, c.city, c.emailAddress, c.username, c.phoneNumber, c.status])            

                    copyfile('data/booksset1.json', 'data/backup/booksset.json')
                
                elif action == "recover.backup":
                    copyfile('data/backup/bookitems.json', 'data/bookitems.json')
                    copyfile('data/backup/booksset.json', 'data/booksset.json')
                    copyfile('data/backup/customers.csv', 'data/customers.csv')
                    copyfile('data/backup/librarians.csv', 'data/librarians.csv')
                    copyfile('data/backup/loanAdministration.json', 'data/loanAdministration.json')


                elif action == "logout":
                    working = False

                    with open('data/customers.csv', mode = 'w', encoding = 'UTF-8', newline = '') as customerFile:
                        customerWriter = csv.writer(customerFile, delimiter = ',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
                        customerFile.truncate()
                        customerWriter.writerow(['Number', 'Gender', 'NameSet', 'GivenName', 'Surname', 'StreetAddress', 'ZipCode', 'City', 'EmailAddress', 'Username', 'TelephoneNumber', 'Status'])
                        for c in customers:
                            customerWriter.writerow([c.id, c.gender, c.nationality, c.firstName, c.lastName, c.streetAddress, c.zipCode, c.city, c.emailAddress, c.username, c.phoneNumber, c.status])

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
            if x.getStatus() == "active":
                print("Welcome " + x.firstName + " " + x.lastName + "\n")
                checking = True
                while checking == True:

                    action = input("What do you want to do? Type help for more information.\n")

                    if action == "help":
                        print("Find a book = find.book\nLend a book = lend.book\nReturn book = return.book\nLook for available books = available.books\nShow books in your possession = my.books\nLogout from the system = logout\n")

                    elif action == "lend.book":
                        searchMethod = input("How do you want to search for a book? Choose:\nTitle, Author or Year\n")
                        if searchMethod == "Title":
                            whatBook = input("Please type the book title.\n")
                            for bi in bookItems:
                                if bi.getBookTitle() == whatBook:
                                    newLoan = LoanItem.LoanItem(x, bi, today, weekLater, bi.getItemId())
                                    bi.setStatus("unavailable")
                                    loanAdministration.append(newLoan)
                                    break

                    elif action == "find.book":
                        searchMethod = input("\nHow do you want to search for a book? Choose:\nTitle, Author or Year\n")
                        if searchMethod == "Title":
                            whatBook = input("\nPlease type the book title.\n")
                            for bi in bookItems:
                                if bi.getBookTitle() == whatBook:
                                    print("\nTitle: ", bi.getBookTitle(), "\nAuthor: ", bi.getBookAuthor(), "\nAvailability: ", bi.getStatus(), "\n")
                        
                        elif searchMethod == "Author":
                            whichAuthor = input("\nPlease type the authors name\n")
                            for bi in bookItems:
                                if bi.getBookAuthor() == whichAuthor:
                                    print("\nTitle: ", bi.getBookTitle(), "\nAuthor: ", bi.getBookAuthor(), "\nAvailability: ", bi.getStatus(), "\n")
                        
                        elif searchMethod == "Year":
                            whatYear = input("\nPlease type the year of the book\n")
                            for bi in bookItems:
                                if bi.getBookYear() == whatYear:
                                    print("\nTitle: ", bi.getBookTitle(), "\nAuthor: ", bi.getBookAuthor(), "\nAvailability: ", bi.getStatus(), "\n")

                    elif action == "available.books":
                        for testbooks in bookItems:
                            if testbooks.getStatus() == "available":
                                print("\nTitle: ", testbooks.getBookTitle() , "\nCopyID: " , testbooks.getItemId(), "\nStatus: ", testbooks.getStatus(), "\n")
                                    
                    elif action == "my.books":
                        for booksInLoan in loanAdministration:
                            if booksInLoan.getCustomer().getUsername() == x.getUsername():
                                print("Bookinformation: \n\tTitle: ", booksInLoan.getBookItem().getBookTitle(), "\n\tAuthor: ", booksInLoan.getBookItem().getBookAuthor(), "\n\tReturn Date: ", booksInLoan.getDateEnd(), "\nCopyID: ", booksInLoan.getBookItem().getItemId(), "\n")

                    elif action == "return.book":
                        whatBook = input("\nWhich book would you like to return? Type the copy id.\n")
                        for booksInLoan in loanAdministration:
                            if booksInLoan.getCustomer().getUsername() == x.getUsername():
                                if whatBook == booksInLoan.getBookItem().getItemId():
                                    print("Bookinformation: \n\tTitle: ", booksInLoan.getBookItem().getBookTitle(), "\n\tAuthor: ", booksInLoan.getBookItem().getBookAuthor(), "\n\tReturn Date: ", booksInLoan.getDateEnd(), "\n")
                                    booksInLoan.getBookItem().setStatus("available")
                                    for loan in loanAdministration:
                                        if loan.getBookItem().getItemId == booksInLoan.getBookItem().getItemId():
                                            loanAdministration.remove(booksInLoan)

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
            else:
                print("This user is blocked.")
            
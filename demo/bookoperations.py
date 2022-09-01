import time
from filehandler import appendnewbook, getallBooks, deletbookfromfile, searchbook, updateBookinfile

def askforInt(message):
    value = input(message)
    if value.isdigit():
        value= int(value)
        return value
    return askforInt(message)

def askforinputstring(message):
    value = input(message)
    if value.isspace() or value.isdigit():
        print("---- please provide suitable value ----")
        return askforinputstring(message)

    return  value

def generateid():
    id = round(time.time())
    return id


def listallbooks():
    ## get books from the file
    books = getallBooks()
    print(books)
    # then display them


def createBook():
    title = askforinputstring("please enter title ")
    description = askforinputstring("please enter description ")
    print(title, description)
    # save title, description, and id for the book in file
    # id:title:description
    id = generateid()
    book_details=f"{id}:{title}:{description}\n"
    print(book_details)
    ## save this new book to the file books.txt
    added = appendnewbook(book_details)
    if added:
        print("---- New book created successfully ---")
        listallbooks()



def deletebook():
    #1- list all books
    listallbooks()
    # 2- ask user to enter id the of book he wants to delete
    book_id= askforInt("please enter the id of the book you want to delete")
    print(book_id)
    # 3- check if the  book with this id exists in the file
    res=deletbookfromfile(book_id)
    if res:
        print("book deleted successfully")

def editBookdetails(book_index, book_id):
    print(f"------------------- update book{book_id} --------------------")
    title = askforinputstring("please enter title ")
    description = askforinputstring("please enter description ")
    book_details = f"{book_id}:{title}:{description}\n"
    ### update data in file
    updated = updateBookinfile(book_index, book_details)


def editbook():
    # 1- list all books
    listallbooks()
    # 2- ask user to enter id the of book he wants to delete
    book_id = askforInt("please enter the id of the book you want to edit ")
    ### check if book exists
    bookindex = searchbook(book_id)
    print(bookindex)
    if isinstance(bookindex, int):
        print("found")
        editBookdetails(bookindex, book_id)
    else:
        print("notfound")
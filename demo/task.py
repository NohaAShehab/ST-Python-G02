

""" system to add new book-->

each book --> id , title , description

CRUD, create, retrieve , update delete
"""
from bookoperations import createBook, listallbooks, deletebook, editbook

def mainmenu():
    choice = input("please enter c for create , l for listing all books, e for edit, d for delete ")
    if choice == 'l':
        listallbooks()

    elif choice =='c':
        ## ask user to enter the book details, save it to the file
        createBook()

    elif choice=="d":
        deletebook()

    elif choice=="e":
        editbook()

    else:
        print("incorrect choice ")
        return  mainmenu()


mainmenu()
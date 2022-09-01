def writebookstothefile(books):
    try:
        fileobj  = open("books.txt", "w")
    except Exception as e:
        print(e)
    else:
        fileobj.writelines(books)
        fileobj.close()
        return True

def appendnewbook(bookdetails):
    try:
        fileobj  = open("books.txt", "a")
    except Exception as e:
        print(e)
    else:
        fileobj.write(bookdetails)
        fileobj.close()
        return True


def getallBooks():
    try:
        fileobj = open("books.txt", "r")
    except Exception as e:
        print(e)
    else:
        books = fileobj.readlines()
        fileobj.close()
        return books



def searchbook(book_id):
    allbooks = getallBooks()
    for book in allbooks:
        book_info = book.split(":")
        if book_info[0]==str(book_id):
            book_index = allbooks.index(book)
            return book_index


def deletbookfromfile(book_id):
    book_index = searchbook(book_id)
    allbooks=getallBooks()
    del allbooks[book_index]
    deleted=writebookstothefile(allbooks)
    return deleted



def updateBookinfile(book_index, updated_data):
    allbooks = getallBooks()
    allbooks[book_index]= updated_data
    updated = writebookstothefile(allbooks)
    return updated

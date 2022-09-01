
print("--------------------- dealing with files -----------------")

"""you to deal with file ---> save data , read configuration from a file ---> writefile ---> send email

1- open  the file (specify operation you want to apply on (read, write, append)

2- do operation (read , write, append) 

3- close file 
"""

############################################### Open file #####################################
"1- open file for read ---> "
"""
    open(filename, mode)
    open(filename) ---> open file with mode read
    if file is not exist  ---> exceoption will be raised 
    
    filemodes 
    r ---> read
    w ---> write
    a ---> append
"""
#
# try:
#     # fileobj= open("users.txt")
#     fileobj = open("files/users.txt", "r")  # TextIOWrapper
# except Exception as e:
#     print(e)
# else:
#     print("file is opended successfully")
#     print(fileobj) # filename, mode of opening
#
#     ### read data from the file
#     filedata =fileobj.read() # read file content into one string
#     print(filedata)
#     fileobj.close()


############3 read file content line by line


# try:
#     # fileobj= open("users.txt")
#     fileobj = open("files/users.txt", "r")  # TextIOWrapper
# except Exception as e:
#     print(e)
# else:
#     print("file is opended successfully")
#     print(fileobj) # filename, mode of opening
#
#     ### read data from the file
#     filedata =fileobj.readline() # read line from the file
#     print(filedata)
#     filedata = fileobj.readline()
#     print(filedata)
#     fileobj.close()

""" 3- read the file content (read all lines ))"""


# try:
#     # fileobj= open("users.txt")
#     fileobj = open("files/users.txt", "r")  # TextIOWrapper
# except Exception as e:
#     print(e)
# else:
#     print("file is opended successfully")
#     print(fileobj) # filename, mode of opening
#
#     ### read data from the file
#     filedata =fileobj.readlines() # read file content into a list line by line
#     print(filedata)
#
#     fileobj.close()


"""4- iterate the file object """


try:
    # fileobj= open("users.txt")
    fileobj = open("files/users.txt", "r")  # TextIOWrapper
except Exception as e:
    print(e)
else:
    print("file is opended successfully")
    for l in fileobj:
        print(f"line = {l}")
    fileobj.close()




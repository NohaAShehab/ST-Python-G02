print("------------- append data to the file ------------------")
"""
    if you open the file with append mode 
    if file exists ---> append data at the end of the file 
    if the file not exits ---> create new file 
"""
try:
    fileobj = open("files/userinfo.txt", "a")  # this will remove any content in the file
except Exception as e:
    print(e)
else:
    print(fileobj)
    fileobj.write("bla bla bla \n")
    fileobj.close()
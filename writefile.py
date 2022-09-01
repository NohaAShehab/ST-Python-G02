print("--------------- write data to the file --------------- ")
"""
    mode write-- open the file for writing from the beginning of the file
    -- if the file not exists python will try create it 
"""

# try:
#     fileobj = open("files/mycv.txt", "w")  # this will remove any content in the file
# except Exception as e:
#     print(e)
# else:
#     print(fileobj)
#     # fileobj.write("Good afternoon python team\n")
#     # fileobj.write("###################################")
#     # fileobj.write("------------- My name is Noha ------------------------")
#     fileobj.close()

############################################

try:
    fileobj = open("files/mycv.txt", "w")  # this will remove any content in the file
except Exception as e:
    print(e)
else:
    print(fileobj)
    fileobj.writelines(["Ahmed\n", "Ali\n", 'Test\n'])
    fileobj.close()




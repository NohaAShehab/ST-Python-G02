
print("------------------- Modules ---------------------- ")

# # import os
# #
# # print(os.getcwd())  # pwd -->
# #
# # print(os.getlogin())
#
# ##########################################
# import re
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# # email = 'noha@gmail.com'
# # print(re.match(regex, email))   # this will return match object ---> True
# email = 'noha@gma'
# print(re.match(regex, email))   # if not will retrun None
#########################################################

# l = ["ahmed", "iti", "python", "mansoura",333]
# name,*course,city  = l
#
#
# with open("files/user.txt") as myfile:
#     print(myfile.read())
###################################3 list comprehension

# " generate list of numbers from 1 to 10"
# # nums = list(range(1,11,2))
# # nums  = [x for x in range(1,11) if x%2==0]
# nums  = [x*x for x in range(1,11) if x%2==0]

######################################

l = ["ahmed", "ali", "abdelrahman", "nesma", "eman", 'asmaa']

# for i in l:
#     print(i, l.index(i))

""" create index for the iterable """
l = enumerate(l)
print(l) #  enumrate object

# for item in l:
#     print(item, type(item))  # tuple(index, value at index)

for index, item in l :
    print(f"index = {index}, item={item}")
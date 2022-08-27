
print("              Strings ")
# set of chars
#
# """
#     string ---> set of char --> treated like array
#     # You can access chars using index --> starts from 0
#
# """
# "1- get len of the string"
# message = "Hello World"
# print(len(message))
#
# "2- you can access chars at any position in the string"
# print(message[4])
#
#
# "3- get part from the string "
# print(message[2:7])  # get string from start to end-1
#
# "4- count no of char in string"
# print(message.count("l"))
#
# "5- get the index of certain char"
# print(message.index("l"))  # get the index of the first occurrence of the object
#
#
# "6- conactentation"
# firstname = "Noha "
# midname = "Abdelahady "
# lastname ="Shehab"
#
# fullname = firstname + midname + midname + lastname
# print(fullname)
#
# "7- interpolation"
# fullname  = firstname+ midname*2 + lastname
# print(fullname)

"8- Capalize lower"

p = "i love Egypt"

print("    ===> ", p.capitalize())

print(p.isupper()) # check if all chars are upper , islower is the opposite

print(p.lower())  #
print(p.upper())

# ########################## replace
message = "hello world  0"

print(message.replace("0", "@"))  # works only with char

" 10 - format "
#
# temp = "My name is {0} I works {1}  "
#
# print(temp.format("noha", "iti"))
#
# print(temp.format("Ahmed", "University"))


# temp = "My name is {0} I works {1} since {2}"
#
# print(temp.format("noha", "iti", 2022))  # you must pass the parameters according to the order
#
# print(temp.format("Ahmed",2022 , "University"))


# temp = "My name is {name} I works {work} since {year}"
#
# print(temp.format(name="noha", year=2022, work="iti"))  # you must pass the parameters according to the order
#
# # print(temp.format("Ahmed",2022 , "University"))


######################## f-format string
name = "Noha"
work = "iti"
temp = f"My name is {name} I works at {work} "
print(temp)

# ######################################
# "Test value in the string"
# myvar = '10'
# print(myvar.isdigit())  # return true if the value in the string is numeric value
# print(myvar.isnumeric())
#
# mystr = "                  "
# print(mystr.isspace())
#
# mystr = 'iti itii iti '
# print(mystr.isalpha()) # check if the string consists of only chars
#
# mystr = 'itiitiiit'
# print(mystr.isalpha())
#
#
# ##################
# str = "                 test                       "
# print(str)
# print(str.strip())  # remove space form both edges
# print(str.rstrip())  # remove space form end of the string
# print(str.lstrip())  # remove space form string of the string

# ################################## strip to remove  chars

message = '      @ welcome to Python @    '
print(message.strip("@ "))  # remove spaces or any specified chars from the edges
#############################################################################33














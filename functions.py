print("-------- functions ----------------- ")

""" set of lines are used to perform certain task ,====> this can be called and more 


NO function hositing in python
"""

# ######################## functions with known predefined number of arguments
# def getfullname(firstname, lastname):
#     fullname = f"{firstname} {lastname}"
#     # return fullname
#
#
#
# myname = getfullname("Noha", "Shehab") ## object from None ----> Falsy values


############################################################
"2- function returns with multiple results ? "

# def getfullname(firstname, lastname):  # arguments
#     fullname = f"{firstname} {lastname}"
#     # return fullname
#     return firstname, lastname, fullname, 10
#
#
# myname = getfullname("Noha", "Shehab")  # parameters
# # the function return is added to a tuple
# myname = getfullname("Noha")

# #################################################3
"3- function with default arguments "

#
# def getfullname(firstname="", lastname=""):  # arguments
#     fullname = f"{firstname} {lastname}"
#     print(f"firstname= {firstname}, lastname={lastname}")
#     # return fullname
#     return firstname, lastname, fullname
#
#
# n = getfullname("Noha")
# getfullname(lastname="ahmed", firstname="Ali")





# ################################### functions with variable number of arguments

# print("iti", "Ahmed", "Ali" ,"test")


# def get_students(*names):
#     print(names, end="        $ ")  # tuple
#
# get_students()
# get_students("Ahmed", "ALI")
# get_students("test", "bla bla", "python")

# ###################################### function with variable number of parameters --> unknown keys?

def introduceyourself(**kwargs):
    print(kwargs)  # dictionary
    pass

introduceyourself(name="Ahmed")
introduceyourself(firstname="omar", lastname="ahmed", lives_in="cairo")
introduceyourself()

temp ="I love {lang}"
print(temp.format(lang="python"))



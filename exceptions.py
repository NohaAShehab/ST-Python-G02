

# # print("noha"   # syntax error
# print("-------------------------Exceptions ---------------------")
# # print(name)  # runtime erro =---> exceoption
#
# print("000000000000000000000000000000000")
# print(7/0)

# ############### logical errors

# def sumnum(num1,num2):
#     return num1*num2
#
# s = sumnum(10, 20)


# ################  Exception handling ############
# try:
#     print(course)
# except:
#     print("Variable course is not defined ")
#
# print("------------------")

#####################################33

# try:
#     # print(course)  # NameNotFound
#     print(7/0)
# except Exception as e:
#     print(e)
#
# # DivisionByZeroError

############################
# course = "Python"
# try:
#     print(course)
# except Exception as e:
#     print(e)
# else:
#     print("printed successfully ")
# finally:
#     print("this block is executed ---> wether there is problem or not ")
#
# print("------------------------  ")

##################################33 Raising Exception##############################

def divnum():
    num1 = input("please enter num1 : ")
    if num1.isdigit():
        num1 = int(num1)
    else:
        raise Exception("Cannot divide string by number or other string")

    num2 = input("please enter num2: ")
    if num2.isdigit():
        num2= int(num2)

    div = num1/num2
    print(div)


divnum()




















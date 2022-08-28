print("----------------- Scopes-------------------------")

"""
    scopes: 
        local scope --> any variable defined inside any function
        === local variables cannot be accessed outside the function
        global ---> any variable defined in the script ((out side the function)) 

"""
# "course variable is variable in the global scope, can be accessed anywhere in the script "
# course = "python"
#
# print(course)
# print("-------------------")
#################################### 2- #######################################
# "2- you access global variable from the function -read , print the variable-"
# course = "Python"
#
#
# def testglobal():
#     print(f" from inside the function course = {course}")
#
#
# testglobal()

###########################################
"2- modify global variable from the function "
# course = "Python"
#
# def testglobal():
#     course = 'django'  # create new local variable in the function scope
#     print(f" from inside the function course = {course}")
#
#
# testglobal()
# print(f" After the function ,,,,, course = {course}")

###########################################
# course = "Python"
#
#
# def testglobal():
#     global course
#     course = 'django'  # create new local variable in the function scope
#     print(f" from inside the function course = {course}")
#
#
# testglobal()
# print(f" After the function ,,,,, course = {course}")


# ##################################### function inside function #########################################

# stdname = "Ahmed Ismail"
#
# username= input('please enter your name : ')
# l = [4,5,55]
# print(f"Hello {username} {l}")
"""
    local variable inside any function can be accessed for read/ print from anywhere inside the inner functions
"""
# def outerfun():
#     track = "opensource"  # local variable for the outer function
#     print(f"form the outerfun track= {track} ")
#
#     def innerfun():
#         print(f"form the inner function track= {track} ")
#
#     innerfun()
#
#
#
# outerfun()

#############################3
"try to modify the track variable "


# def outerfun():
#     track = "opensource"  # local variable for the outer function
#
#     def innerfun():
#         track = "Ai"  # local variable for  the inner function
#         print(f"form the inner function track= {track} ")
#
#     innerfun()
#     print(f"form the outerfun track= {track} ")
# outerfun()

##################################################################################3

def outerfun():
    track = "opensource"  # local variable for the outer function

    def innerfun():
        nonlocal track
        track = "Ai"  # local variable for  the inner function
        print(f"form the inner function track= {track} ")

    innerfun()
    print(f"form the outerfun track= {track} ")


outerfun()

print("------------------ Modules--------------------")
"""
    any pyton file is called a module 
"""

# """ 1- import the module then access its parts """
# import validation
#
# res = validation.askforint()


# """ 2- import part of the file ....."""
#
# from validation import askforint as test
#
# sal=test("please enter salary")
#
# from  validation import  g
# print(g)
#
# g= 1000

#####################
# import math
#
# print(math.pi)

# #################### import from package
# import itipackage.basemodule
#
# res=itipackage.basemodule.validatestr("    Nohaaaaaaaaaaa   ")


# import itipackage.basemodule as bm
#
# res=bm.validatestr("    Nohaaaaaaaaaaa   ")



# from itipackage.basemodule import validatestr
# r = validatestr("            hello               ")
#########################################
# import testpkg.greetingmodule
#
#
# testpkg.greetingmodule.sayhello("Noha")

from testpkg import sayhello

sayhello("Ahmed")












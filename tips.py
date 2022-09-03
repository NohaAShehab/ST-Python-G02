"""

Lambda expression ---> anonymous function ((function without name)) ---
"""

### function add 4 to x

# myfun = lambda x: x+4
# res=myfun(20)
# print(res)


###### function may return another function


# def addnums(num1, num2):
#     res  = num1 + num2
#     print(res)
#     return lambda num: res*num
#
# x = addnums(4,5)
# print(x, type(x))
# print(x(10))
#
# print(addnums(6,7)(10))

############################## Map , filter

# l = [3,4,5,6,777]
# newl = map(lambda x:x*5, l)
# print(newl)  #map object
# print(list(newl))

###############################

#
# l = [3,4,5,6,777]
# newl = filter(lambda x:x%3==0, l)
# print(newl)  #map object
# print(list(newl))
#
###################################
# swap
#
# x = 10
# y = 'iti'
#
# x,y = y,x
# # ############ swap
# # z= x
# # x = y
# # y = z
# ############# iterable
#
# l = ["Ahmed", "Mohamed", "Omar", "Ali", "Test"]
#
# # for name in l:
# #     print(name)
#
# l = iter(l) # iter object
# print(next(l))
# #
# #
# #
# #
# print(next(l))
# #
# #
# #
# #
# print(next(l))
# #
# #
# #
# #
# print(next(l))
# #
# #
# #
# #
# print(next(l))
#
# #
# #
# #
# #
# print(next(l))

# ####################################################################
## generate counter ---> 1 ------> 1000000000

l = [i for i in range(100)]

# generators

def counter_million():
    for i in range(100):
        yield i

mygen = counter_million()
print(mygen)

print(next(mygen))

for i in mygen:
    print(i)









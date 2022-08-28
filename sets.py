print("data structures")
#
# """ sets one of the basic data structure in python
#
#     sets are mutable datatypes
# """
#
# "1- to define a set "
#
# s = set([])  # set can hold different values with different datatypes
# myset = {"abc", "iti", 'python',"abc", "iti"}
#
# """
#         sets doesn't allow duplicates in values
#         items in the set are not sorted
#         no index to access the set items
# """
# # myset2 = {}  # this dictionary not set
#
# "1- you get the len of set"
# print(len(myset))
#
# "2- update the set ? "
# myset.update(['test', "django"])
#
#
# "3- add element to the set  added to random position "
# myset.add("new element")
#
# "4- pop element from the set"
# popped = myset.pop()  # remove one element randomly from the set
#
# "5- remove certain element "
# myset.remove("python")

# ############################ list , tuples


myinfo = ["noha", "iti", "engineering", "mansoura"]

"""
    dictionary ---> is one of the non primitive data structure in python 
    
    ---> key value pair 
    --> keys should string 
    --> there is no duplication in the keys 
"""

"1- to define a dictionary "
d = {}
mydic = dict([("name", "noha")])
info = {"name": "noha"}

"2- get the len of the dic "
print(len(info))
"3- access element in the dictionary ? using the key "
myinfo = {"name": "noha", "work": "iti"}
print(myinfo["work"])
myinfo["work"] = "Information Technology Institue"

"4- add new element (key: value) to the dic"
myinfo["certified"] = "Information Technology Institue"

"5- remove key-value pair from dic"
# del myinfo["work"]
popped_item = myinfo.pop("work")

"6-get keys of dic"
fullinfo = {
    "name": "ahmed",
    "track": "python",
    "course": ["python", "django", "postgres", 'js'],
    "year": 2022
}

keys = fullinfo.keys()  # object ---> dict_keys
print(keys, type(keys))

keys = list(keys)


"7- get the values of dic"
values = fullinfo.values()
print(values)

"8-  pair of key , value "
dic_info = fullinfo.items()  # object from  dict_items
print(dic_info)


# "9- concatenation is not allowed"
# d1 = {"course" : "python"}
# d2 = {"track": "opensource"}
#
# d3 = d1 + d2  # unsupported operand type(s) for +: 'dict' and 'dict'


"9- update dictionary "
d1 = {"course" : "python"}
d2 = {"track": "opensource"}


d1.update(d2)# unsupported operand type(s) for +: 'dict' and 'dict'

"10- check if item in a dic"
print("ahmed" in fullinfo)  # this will search in dict_keys
print("ahmed" in fullinfo.values())

"11- loop over dic"

# for item in fullinfo:
#     print(f"item = {item}")  # keys,
#     print(f"item = {item}, {fullinfo[item]}")  # keys,


# for key, val in fullinfo.items():
#     print(f"key = {key}, val= {val}")

"12- remove all keypairs in the dictionary "
# fullinfo.clear()
#
#
# del fullinfo
"cast dic to a list"

list_info = list(fullinfo)







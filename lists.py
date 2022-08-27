print("------------- lists -------------------")
#
#
# "in python , we don't have built in arrays "
#
# "we have lists "
#
# "1- to create a list "
# l  = []
# l2= list([])
#
# "2- list hold different values with different data types"
# track = ['python', 20, "August", 2022, 4,  "python",True, 6.6, "python",["python", "django"]]
#
# "3- get len of the list "
# print(len(track))
#
"4- lists are mutable datatypes ? --> you can modify list content after creation "
# track[1] = "iti"  # modify existing value
#
"5- append item to the end of list"
# track.append("item added")
#
"6- insert new item to the list at certain index"
# track.insert(3, "inserted")
#
"7- pop element from the list "
# popped = track.pop()  # remove last element in the array and returns with it
#
"8- pop accept index "
# popped_2 = track.pop(3)  # pop item at certain index
#
"9- remove item "
# track.remove("python")  # remove the first occurrence of the element form the list
#
"10- count element in the list "
# print(track.count("python"))
#
# "11- concatenation"
# # l1 = ["python", "django", 10]
# # l2 = ["summer", "August"]
# # l3 = l1+ l2
#
# "12- extend"
# l1 = ["python", "django", 10]
# l2 = ["summer", "August"]
# l1.extend(l2)
#

'13 - you can sort the elements in the list ---> all the list items must be from the same type'
nums = [4,5,6,7,77,8,9,999]
nums.sort()  # sort the list in the same variable
nums.sort(reverse=True)
# # sorted
ll = ["MM", "Ali", "Omar"]
ll.sort()

"14-  reverse "
track = ['python', 20, "August", 2022, 4,  "python",True, 6.6, "python", ["python", "django"]]
track.reverse()


"15- min , max  ---> works on list consists of items from the same type "
ll = ["MM", "Ali", "Omar"]
print(min(ll))


"16- loop over the list "
items = ['python', 20, "August", 2022, 4,  "python",True, 6.6, "python"]
#
# for abbass in items:
#     print(abbass)


"17 membership --> check if the value in the list ---> "
items = ['python', 20, "August", 2022, 4,  "python",True, 6.6, "python"]
print("August" in items)



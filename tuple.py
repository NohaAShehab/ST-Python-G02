print("tuples ")

"tuple ---> is a type of sequences , immutable datatype"

"1- to create a tuple "
t  = ()
t2= tuple([])

"2- tuple hold different values with different data types"
track = ('python', 20, "August", 2022, 4,  "python",True, 6.6, "python",["python", "django"])
#

"3- get len of the list "
print(len(track))

"10- count element in the tuple "
print(track.count("python"))

"11- concatenation"
t1 = ("python", "django", 10)
t2 = ("summer", "August")
t3 = t1+ t2

"15- min , max  ---> works on list consists of items from the same type "
tt = ("MM", "Ali", "Omar")
print(min(tt))

"16- loop over the list "

items = ('python', 20, "August", 2022, 4,  "python",True, 6.6, "python")

for i in items:
    print(i)
"17 membership --> check if the value in the tuple ---> "

print("August" in items)

# ############ casting between list and tuple ?

# t = ("Ahmed", "python", "iti")
#
# t= list(t)
myl =["a", "b", "c"]

myl = tuple(myl)

####################
"tuple of one item ? "

oneitem = ("test",)

###########################

"remove variable from memory in the runtime"
# print(t1)
# del t1

#########3 get index of item in list or typle

print(items.index("August"))


###########################################
"Ask the user to inter input "


num = input("please eneter number ")
# this function returns with string
# print(num, type(num))
if num.isdigit():
    num = int(num)






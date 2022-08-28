# def askforint(message="please enter number"):
#     num = input(message)
#     if num.isdigit():
#         num =int(num)
#         return num
#     return

# def askforint(message="please enter number"):
#     while True:
#         num = input(message)
#         if num.isdigit():
#             num =int(num)
#             return num
#         print("|..............please try agian ............")
#     return


# ########################## Recursion

print("############################################################")
def askforint(message="please enter number"):
    num = input(message)
    if num.isdigit():
        num = int(num)
        return num
    print("|..............please try again ............|")
    return askforint(message)




g = 9.81


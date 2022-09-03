"""
    OOP-Principles
    1- Abstraction
    2- Inheritance
    3- Encapsulation
    4- Polymorphism

"""


#
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name
#         self.email = email
#         self.salary= salary
#
#     def printEmp(self):
#         print(f"My name is {self.name}")
#
#     @classmethod
#     def createNewEmp(cls,name):
#         return cls(name,"default@gmail.com",1000)


#     @staticmethod
#     def calNetSal(salary):
#         return  salary*.86

# ######################################## Inheritance ####################################
# class Person:
#     def __init__(self, name, bdate):
#         self.name = name
#         self.bdate = bdate
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# class Employee(Person):
#     pass
#
#
# e = Employee("Ahmed", 2000)
###################################################33


# class Person:
#     def __init__(self, name, bdate):
#         self.name = name
#         self.bdate = bdate
#
#     def speak(self):
#         print(f"My name is {self.name}")

#
# class Employee(Person):
#     def __init__(self, name, bdate, email, salary):
#         super().__init__(name, bdate)
#         self.email = email
#         self.salary = salary
#
#     ### overriding
#     def speak(self):
#         super().speak()
#         print(f"email = {self.email}, salary = {self.salary}")
#
#
# e = Employee("Ahmed", 2000, "ahmed@gmail.com", 10000)
# e.speak()
################################################# inheritance
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#     # pass
# class Employee:
#     def __init__(self, salary):
#         self.salary = salary
#
# class Engineer(Person, Employee):  # mutiple inheritance
#     def __init__(self, name, sep, salary):
#         super().__init__(name)
#         Employee.__init__(self, salary)
#         self.sep = sep
#
# e = Engineer("Ahmed", "CS")

##################################################################################

class Employee:
    def __init__(self,name, email, salary):
        self.name = name
        self.email = email
        self.salary= salary
    #
    # def printEmp(self):
    #     print(f"My name is {self.name}")

    def printEmp(self,message=""):
        print(f"My name is {self.name} : {message}")

e = Employee("ahmed", "ahmed@gmail", 1000)
e.printEmp("hiiiii")



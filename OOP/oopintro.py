print("----------------- OOP --------------------- ")

# employee1 ={
#     "name":"noha",
#     "works":"iti",
#     'mail':"noha@gmail.com"}
#
#
# employee2 ={
#     "empname":"Ahmed",
#     "works":"iti",
#     'mail':"ahmed@gmail.com"}
""" class ---> blueprint for a type ---> user defined datatype 
-- you can define object properties , methods 

"""
# class Employee:
#     pass
#
#
# "to take object from employee"
# e = Employee()
# print(e)

""" to define the properties related to the object """

# class Employee:
#     def __init__(self):  # self ---> constructor function ---> calling while creating new object
#         print(f"{self}----->self") #self --> refers to the object address in memory
#         self.name = 'empname'
#         self.id = 1
#         self.email = "email"
#         self.salary= 1000
#
# e = Employee()
# print(e)
# e3 = Employee()
##############################################################3
"customize object creation "
# class Employee:
#     def __init__(self,name, id, email, salary):  # self ---> constructor function ---> calling while creating new object
#         self.name = name
#         self.id = id
#         self.email = email
#         self.salary= salary
#
# e = Employee("ahmed", 20, "ahmed@gmail.com", 2000)
# e3 = Employee("test", 100, "test@gmail.com", 3000)
# #######
# print(e.name)
# print(e3.salary)
# e3.salary= 8000


""" classes and dictionary """

# class Employee:
#     def __init__(self,name, id, email, salary):  # self ---> constructor function ---> calling while creating new object
#         self.name = name
#         self.id = id
#         self.email = email
#         self.salary= salary
#
#
# e = Employee("ahmed", 10, "ahmed@gmail.com", 2000)
# print(e.__dict__)

#########################################
# class Employee:
#     def __init__(self,name, id, email, salary):
#         self.name = name  # instance variables
#         self.id = id
#         self.email = email
#         self.salary= salary
#
#     # instance method
#     def emp_details(self): # self--> represent address of current instance
#         print(f"Name: {self.name}, email:{self.email}")
#
#
# e = Employee("noha", 1, "noha@gamil.com", 1000)
# e.emp_details()
# e2 = Employee("Ali", 3, "ali@gamil.com", 1000)
# e2.emp_details()
###############################################################################################
""" class variable
    you need a property that is not depend on the instance ---> 
    but shared between all instances (related to the class) 
    
    --> you can access it using class itself
 
"""
# class Employee:
#     nationality = "Egyptian"
#     no_of_employees = 0
#     def __init__(self,name, id, email, salary):
#         self.name = name  # instance variables
#         self.id = id
#         self.email = email
#         self.salary= salary
#         Employee.no_of_employees +=1
#
#
#     # instance method
#     def emp_details(self): # self--> represent address of current instance
#         print(f"Name: {self.name}, email:{self.email}")
#
#
# e = Employee("noha", 1, "noha@gamil.com", 1000)
# e.emp_details()
# e2 = Employee("Ali", 3, "ali@gamil.com", 1000)
# e2.emp_details()
# print(Employee.nationality)
# Employee.nationality = "Test"

###########################3 check this


# class Employee(object):
#     nationality = "Egyptian"
#     no_of_employees = 0
#     __slots__ = ["name", "id", "salary", "email"]
#
#
#     def __init__(self,name, id, email, salary):
#         self.name = name  # instance variables
#         self.id = id
#         self.email = email
#         self.salary= salary
#         Employee.no_of_employees +=1
#     # instance method
#     def emp_details(self): # self--> represent address of current instance
#         print(f"Name: {self.name}, email:{self.email}")
#
#
# e = Employee("noha", 1, "noha@gamil.com", 1000)
# e2 = Employee("Ali", 3, "ali@gamil.com", 1000)
# e3 = Employee("Mostafa", 3, "Mostafa@gamil.com", 1000)
#
# print(Employee.nationality)
# # e.nationality = "American"  #### add new instance variable to this object  nationality
# print(Employee.nationality)
# Employee.nationality  ="British"
#
# # e.test = "nnnnnnnnnnnnnn"

############## class methods
""" class method ---> method shared between all instances in the class
    you call it either using class name or using object (instance) 
    cls ---> represent the class 
    class method ----> object factory >>> ----> create new object from the class , 
    ---> extend employees
"""


# class Employee(object):
#     nationality = "Egyptian"  # class variable
#     no_of_employees = 0
#
#     def __init__(self,name, id, email, salary):
#         self.name = name  # instance variables
#         self.id = id
#         self.email = email
#         self.salary= salary
#         Employee.no_of_employees +=1
#     # instance method
#     def emp_details(self): # self--> represent address of current instance
#         print(f"Name: {self.name}, email:{self.email}")
#
#     @classmethod
#     def get_number_of_employees(cls):
#         # print(cls)  # this is the class Employee
#         # print(Employee)
#         return cls.no_of_employees
#
#     @classmethod
#     def createEmployee(cls, name):
#         return cls(name,cls.no_of_employees+1, f"{name}@gmail.com", 10000)
#
#     @classmethod
#     def addEmployee(cls, emp1, emp2):
#         name= f"{emp1.name} {emp2.name}"
#         return cls(name,cls.no_of_employees+1, f"{name}@gmail.com", 10000)


#
# e = Employee("Ahmed", 20, "ahmed@gmail.com", 80000)
# e3 = Employee("Ahmed", 20, "ahmed@gmail.com", 80000)
#
# # print(Employee.get_number_of_employees())
# e4 = Employee.createEmployee("noha")
# e5 = Employee.addEmployee(e,e3)


############################################################

"""static method ---> function doesn't depend on the instance or on the class but helper function 
you can access it using classname or isntance name 
"""

class Employee(object):
    nationality = "Egyptian"  # class variable
    no_of_employees = 0

    def __init__(self,name, id, email, salary):
        self.name = name  # instance variables
        self.id = id
        self.email = email
        self.salary= salary
        Employee.no_of_employees +=1
    # instance method
    def emp_details(self): # self--> represent address of current instance
        print(f"Name: {self.name}, email:{self.email}")

    @classmethod
    def createEmployee(cls, name):
        return cls(name,cls.no_of_employees+1, f"{name}@gmail.com", 10000)

    @staticmethod
    def calnetsal(salary):
        return salary * .86


e = Employee("ahmed", 10, "ahmed@gmail.com", 6000)

# def calnetsal(salary):
#     return salary*.86
#
# print(calnetsal(e.salary))
# print(calnetsal(100000))
print(Employee.calnetsal(e.salary))
print(e.calnetsal(e.salary))
print(Employee.calnetsal(30000))















l = [1,3,4,5]
l2 = [3,5,6,6]
l.extend(l2)












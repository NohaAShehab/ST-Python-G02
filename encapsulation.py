"""
    Access modifiers
    public  ---> can be accessed using the instance object anywhere
    protected ---> _variablename ---> can be access only using self in the class or derived class
    private ---> __variablename  ---> can be accessed only in their class

    static ------> class variable
"""
#
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name
#         self._email = email  # protected ()
#         self.__salary =salary
#
#
# e = Employee("Nesma", "nesma@gmail.com", 10000)
# # print(e._email) #ethically
# # print(e.__salary)
# print(e.__dict__)
# #######################################################3


# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name
#         self._email = email  # protected ()
#         self.__salary =salary
#
#
# e = Employee("Nesma", "nesma@gmail.com", 10000)
# # print(e._email) #ethically
# # print(e.__salary)
# print(e.__dict__)



# #############################################

# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name
#         self._email = email  # protected ()
#         self.__salary =salary
#
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name
#         self._email = email  # protected ()
#         self.__salary =salary
#
#     # setters and getters for the object
#     def setSalary(self, sal):
#         if isinstance(sal, int):
#             self.__salary = sal
#         else:
#             self.__salary= 0
#             # raise TypeError("Salary must be number")
#
#     def getSalary(self):
#         return self.__salary
#
#     # calculated property
#     @property
#     def netSalary(self):
#         return self.__salary*.86
#
#
# e = Employee("Nesma", "nesma@gmail.com", 10000)
# e.setSalary("test")
# print(e.getSalary())
# print(e.name)
# print(e.netSalary)
# print(e.__dict__)

################################################################33
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name
#         self._email = email  # protected ()
#         self.__salary =salary

class Employee:
    def __init__(self,name, email, salary):
        self.name = name
        self._email = email  # protected ()
        self.salary = salary

    # setters and getters for the object

    @property
    def salary(self):
        self.__salary +=100
        return self.__salary

    @salary.setter
    def salary(self, sal):
        if isinstance(sal, int):
            self.__salary = sal
        else:
            self.__salary= 0


    # def setSalary(self, sal):
    #     if isinstance(sal, int):
    #         self.__salary = sal
    #     else:
    #         self.__salary= 0
    #         # raise TypeError("Salary must be number")
    #
    # def getSalary(self):
    #     return self.__salary

    # calculated property
    @property
    def netSalary(self):
        return self.__salary*.86


e = Employee("Nesma", "nesma@gmail.com", "one thousand")
print(e.netSalary)
print(e.salary)
print(e.__dict__)



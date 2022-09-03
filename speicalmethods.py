"""All the classes in python ---> inherits from class object """

class Employee:
    def __init__(self,name, email, salary):
        self.name = name
        self._email = email  # protected ()
        self.salary = salary

    def __str__(self):
        # must return with string
        return f"Employee({self.name},{self._email},{self.salary})"

    def __len__(self):
        #must retrun with int
        return len(self.__dict__)

    def __call__(self, *args, **kwargs):
        print("object is called ")
        self.name= input("please enter name ")
        self.salary = input("pleas")

e= Employee("mohamedEldosky", "meldosky@gmail.com", 10000)
# print(e)
print(len(e))

e()
se = ["Employee", "Rohit", 21, "entry", 1000]


def code(se):
    print(f"{se[1]} is writiing code ...")

#class
class Employee:
    #class attribute
    alias="Keyboard Magician"
    def __init__(self, name, age, level, salary):
        #instance attributes 
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    #instance function
    def codeclass(self):
        print(f"{self.name} is writiing code ...")

#instance
emp1 = Employee("Rohit", 21, "entry", 1000)
print(emp1.name, emp1.age)
print(Employee.alias)
code (se)
emp1.codeclass()


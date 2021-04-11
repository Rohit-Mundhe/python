se = ["Employee", "Rohit", 21, "entry", 1000]

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

#instance
emp1 = Employee("Rohit", 21, "entry", 1000)
print(emp1.name, emp1.age)
print(Employee.alias)

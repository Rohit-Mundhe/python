#inherits, extend, override 
class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
    def work(self):
        print(f"{self.name} is woking ....")



class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level=level
    def debug(self):
        print(f"{self.name} is debugging...")
    def work(self): #override function
        print(f"{self.name} is coding  ....")

    

class Designer(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name , age , salary)
    def draw(self):
        print(f"{self.name} is drawing")
    

se= SoftwareEngineer("Rohit", 21, 6000, "Junior")
print (se.name, se.age)
se.work()
print(se.level)
se.debug()


d= Designer('Vijay', 14, 7000)
print(d.name, d.age,)
d.work()
d.draw()



#polymorphism


employees =[
    SoftwareEngineer("max", 25, 6000, "Junior"),
    SoftwareEngineer("Lisa", 28, 7000, "Semior"),
    Designer("Philipp", 27, 7000)
]


def motivate_employees (employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)
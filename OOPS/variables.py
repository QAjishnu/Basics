#class variable and instance variable

'''class variable are those which are defined under class.
These are constant no matter how many objects u created.'''

'''instance variable are those are defined under constructor. 
It is different for each object'''

class Employee:
     company ="Aristocrat"

     def __init__(self, name, salary):
            self.name = name
            self.salary = salary

e1 = Employee("Anshul", 5000000)
e2 = Employee("Aman", 60000)

print(e1.company)
print(e1.salary)
print(e1.name)

#It means child class can use properties and methods of parent class.
from OOPS.constructor import Employee
from constructor import Student

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

d1 =Dog()
d1.eat()
d1.bark()

class Person(Employee):
    Sex ="Male"

    def getcompltedata(self):
        return self.annual_salary()



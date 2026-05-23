'''constructor is just like special method/function that run automatically
on object creation'''

'''Constructor kyu use karte hain?
Object banate time:
1.data initialize karne ke liye
2.variables set karne ke liye'''

#self keyword is mandatory for calling variable name into method.
# Self is mandatory all the time when we declare method inside the class.

#constructor name should be __init__


class Student:

    def __init__(self,name,age):
        self.name = name
        self.age =age
s1 =Student("Rahul" , 22)
s2 =Student("Prakash" , 21)

print(s1.age)

class Device:

    def __init__(self,firstnumber,secondnumber):
        self.firstnumber = firstnumber
        self.secondnumbr = secondnumber

    def addition(self):
        return self.firstnumber+self.secondnumbr

obj= Device(4,5)
print(obj.addition())

class Employee:
    def __init__(self, name , salary):
        self.name =name
        self.salary = salary

    def annual_salary(self):
        return (self.salary)*12

e1 = Employee("Aman Aswal", 80000)
print(e1.annual_salary())
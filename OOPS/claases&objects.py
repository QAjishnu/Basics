#classes are user defined blueprint or prototype.
#objects are the instances of the class.
#class is blueprint and object us blueprint se bani hui cheej.

class calculator:
    num =100

    def getData(self):  #method
        print("I am now executing as a method under class")

#to call the method  we need to create object for the class.
obj = calculator() #syntax to create objects in python.
obj.getData()
print(obj.num)
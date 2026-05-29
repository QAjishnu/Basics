'''
Built in data structure in python:-
1.List   [1,2,3,4]
2.Tuple  (1,2,3,4)
3.Dictonries    {'a':1}
4.Set   (1,2,3,4}
'''

'''Dictonaries'''

#key value pair
#written in curly braces {}
#key and value pair is separated by colon " : "
#after every pair, comma is inserted.
#keys must be unique but values may be duplicated.
#List mein hum [0] ya [1] index ka use karte the, lekin dictionary mein hum Key ka naam use karte hain.


student ={
    "name":"jishnu",
    "age":31,
    "Sex":"Male",
    "Course": "QA Automation",
    "passed":"True"
}
print(student)

#Access data
print(student["age"])
print(student.get("passed"))

#Add data.
student["city"] ="Noida"
print(student)

#update data.
student["city"]="Delhi"
print(student)

#delete data.
student.pop("passed")
print(student)

#looping data
for key , value in student.items():
    print(key,value)

'''
data.keys()      # all keys
data.values()    # all values
data.items()     # key-value pairs
data.get("name") # safe access
'''

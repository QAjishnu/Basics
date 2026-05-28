# list of having only integers
#list is a datatype that allows multiple values and can be different data types.
a = [1, 2, 3, 4, 5, 6]
print(a)

# list of having only strings
b = ["hello", "john", "reese"]
print(b)

# list of having both integers and strings
c = ["hey", "you", 1, 2, 3, "go"]
print(c)

# index are 0 based. this will print a single character
print(c[1])  # this will print "you" in list c
print(c[-1]) #  it will print the last value from the list.
print(c[1:4]) # it will print from 1st index to the 4th index.

#to add values in the list
c.insert(3 , 99)
print(c)

#to add value in the last
c.append("last")
print(c)

#to delete values

del c[2]
print(c)
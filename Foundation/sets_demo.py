#set = collection of unique values.
'''
Points to Remember:-
1.No duplicate allowed
2.Unorderd
3.Mutable (being capable of modification)
4.indexing not allowed
5. It is written under curly braces " {} "
6.To create empty set we use " set() ". Curcly braces {} are not used as it creates dictionary.
7. In Automation it can be used in following cases:
    a.Data comparison
    b.Remove duplicate
    c.Find missing/common elements
'''

nums={1,2,3,4}
print(nums)

#adding element
nums.add(6)
print(nums)

#removing element
nums.remove(4)
print(nums)

#creating a set from list and removing duplicated.
my_list =[1,2,2,3,4,5,5,6,7,7,7,8]
my_set =set(my_list)
print(my_set)

'''Mathematical operation on sets.'''

set1={"Apple", "Mango", "Banana", "Lichi","Daal"}
set2={"Roti","Chawal","Daal","Sabzi", "Apple"}

#1. Union
print(set1.union(set2))
print(set1 | set2)

#2.Intersection
print(set1 & set2)
print(set1.intersection(set2))

#3.Difference
print(set1 - set2)
print(set1.difference(set2))

#4. Symmetric diff(jo dono me common nahi hai)
print(set1.symmetric_difference(set2))






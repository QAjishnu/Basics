#find count of failed TC

results =["Pass", "Fail", "Pass", "Pass", "Fail", "Skip"]
fail_count =0
for c in results:
    if c=="Fail":
        fail_count +=1
print (fail_count)

#find index of element
links = ["Home", "About", "Products", "Contact", "Careers"]
for i in range(len(links)):
    if links[i]=="Products":
        print("Index of product is:",i)

#reverse string using list.
numbers = [10, 20, 30, 40]
reversed_list= []
for j in numbers:
    reversed_list.insert(0, j)
print(reversed_list)


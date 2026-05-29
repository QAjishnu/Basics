'''
list is a datatype that allows multiple values and can be different data types.
list are collections of data that are ordered and mutable.
indexing starts form zero(0).
Duplicates are allowed.
'''
# list exqmple
browsers = ["Chrome", "Firefox", "Edge", "Chrome"] 
# Index:      0          1         2         3

#add item in list using append.
tools = ["Selenium", "Playwright"]
tools.append("Appium")
print(tools)

#add item in list using insert at desired index.
tools = ["Selenium", "Playwright"]
tools.insert(1,"Appium")
print(tools)

#adding a whole list
group1=["TC1","TC2","TC3","TC4"]
group2=["TC5","TC6","TC7","TC8"]
group1.extend(group2)
print(group1)

#removing from list
browsers = ["Chrome", "Firefox", "Edge", "Safari"]
removed = browsers.pop(1)
browsers.remove("Safari")
print(browsers)
print(removed)

#clearing the list
browsers = ["Chrome", "Firefox"]
browsers.clear()
print(browsers)

#searchung and counting
results = ["Pass", "Fail", "Pass", "Fail", "Pass"]
print(results.count("Fail"))

#position search of any element
users = ["Amit", "Rahul", "Kiran"]
print(users.index("Rahul"))

#sorting and reversing
prices = [500, 100, 300, 200]
prices.sort()
print(prices)

#reversing.
steps = ["Open Browser", "Enter URL", "Click Login"]
steps.reverse()
print(steps)

tests = ["LoginTest", "PaymentTest", "CartTest"]
tests.append("LogoutTest")
tests.insert(0,"SetupTest")
tests.sort()
print(tests)



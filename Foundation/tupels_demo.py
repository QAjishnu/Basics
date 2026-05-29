'''
it is same as list but immutable hence cannot be changed.
Ordered , indexed and also allows duplicates.
If you want to create a tuple of any element, you must give comma(,) in last. If not so, python will
treat it as a string or integer.
'''

not_a_tuple = ("Chrome")  # Yeh ek String hai
a_tuple = ("Chrome",)     # Yeh ek Tuple hai!

#syntax

# Tuple banana
env_config = ("https://qa.xyz.com", "admin", "Secret@123")
# Index:              0                 1            2
# Data nikalna (Accessing) - Bilkul list ki tarah square brackets se
print(env_config[0])  # Output: https://qa.xyz.com

#pre defined methods of tuple
#cout item
modes = ("headless", "headed", "headless")
print(modes.count("headless"))  # Output: 2

#indexing
print(modes.index("headed"))  # Output: 1
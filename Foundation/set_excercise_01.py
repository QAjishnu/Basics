# remove duplicate numbers.
nums = [1, 2, 2, 3, 3, 4]
unique = set(nums)
print(unique)

# Find Total Unique Values.
nums = [1, 1, 2, 3, 3]
unique = set(nums)
print(len(unique))

#check items exist.
skills = {"Python", "SQL", "API"}
print("Python" in skills)

#Add new skill
skills = {"Python", "SQL"}
skills.add("Playwright")
print(skills)

#find unique words.
text = "python is easy python is powerful"
words = set(text.split())
print(words)

#Duplicate username detection.
users = [ "admin","qa","admin","test"]
seen = set()
for user in users:
    if user in seen:
        print("Duplicate:", user)
    seen.add(user)


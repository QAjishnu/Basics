#Replace Sensitive Data
card ="98735678827434356"
masked = "************" + card[-4:]
print(masked)

#mobile number validation
mob ="98765432100"
if len(mob)==10 and mob.isdigit():
     print("valid mobile number")
else:
     print("invalid mobile number")

#generate username
name ="black panther "
username= name.lower().strip().replace(" ","_")
print(username)

#Find duplicate characters
#Remove duplicate characters
#Character frequency counter
text ="programming"
dict={}
for char in text
#Remove special characters




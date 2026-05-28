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
text_01 ="banana"
result =""
for c in text_01:
     if c not in result:
          result +=c
print(result)

#Character frequency counter
text ="programming"
freq={}
for ch in text:
     if ch in freq:
          freq[ch] +=1
     else:
          freq[ch]=1
print (freq)
#Remove special characters




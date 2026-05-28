#count vowels in string
text="jishnu Mishra"
count =0
for ch in text:
    if ch in "aieou":
        count +=1
print(count)

#email validation.
mail ="jishnu.mishra@aristocrat.com"
if "@" in mail and ".com" in mail:
    print("It is a valid mail ID")
else:
    print("invalid mail")

#Extract OTP from SMS
msg ="your OTP for login is 45734"
otp = msg.split(" ")[5]
print(otp)

#extract username from email
email="blackpanther231@gmail.com"
username=email.split("@")[0]
print(username)

#Domain Extraction
email2="jack.we@hotmail.com"
domain = email2.split("@")[1]
print(domain)

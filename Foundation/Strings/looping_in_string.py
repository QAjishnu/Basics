#Loop through string
text ="Python Automation"
for ch in text:
    print(ch)

#Reverse string
text1="python"
print(text1[::-1])

#Palindrome check
text3="madam"
if text3==text3[::-1]:
    print("It is a palindrome")
else:
    print("Not a palindrome")

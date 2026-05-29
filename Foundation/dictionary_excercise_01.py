
#count frequency of characters
text ="banana"
freq = {}
for ch in text:
    # Pehle check karo: Kya yeh character dictionary mein pehle se hai?
    if ch in freq:
        # Agar haan, toh uski purani value nikaalo aur +1 kar do
        freq[ch] = freq[ch] + 1
    else:
        # Agar naa, toh pehli baar ke liye value 1 set kar do
        freq[ch] = 1
print(freq)


#most frequent character
text ="dictionaries"
fre ={}
for ch in text:
    if ch in fre:
        fre[ch]=fre[ch]+1
    else:
        fre[ch]=1
print(fre)
max_char=""
max_count=0
for ch,count in fre.items():
    if count>max_count:
        max_count=count
        max_char=ch
print("maximum char:" ,max_char)
print("maximum count:" , max_count)

#count vowels
text = "automation"
vowel = {}
for ch in text:
    if ch in "aieou":
        vowel[ch] = vowel.get(ch,0)+1
print(vowel)

#maximum Marks
marks = {
    "Math": 90,
    "English": 85,
    "Science": 95
}
max_marks=0
max_sub=""
for key, value in marks.items():
    if value>max_marks:
        max_marks=value
        max_sub=key
print("maximum marks obtained in " , max_sub)

#slowest response of API
response_times = {
    "Login_API": 0.5,
    "Payment_API": 4.2,   # Sabse slow
    "Logout_API": 0.2
}
# Sabse slow API ka naam nikalna
slowest_api = max(response_times, key=response_times.get)
print(f"Sabse slow chalne wali API hai: {slowest_api}")
# Output: Sabse slow chalne wali API hai: Payment_API

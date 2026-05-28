'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

# Empty list banayi numbers store karne ke liye
result_numbers = []

# range(2000, 3200) liya hai taaki 3001 loop ke andar tightly include ho jaye
for number in range(2000, 3201):

    # Condition: 7 se divide ho (remainder 0) AUR 5 ka multiple na ho (remainder NOT 0)
    if (number % 7 == 0) and (number % 5 != 0):
        # Condition match hote hi string me badal kar list me daal do
        result_numbers.append(str(number))

# Comma se separate karke single line me output print kiya
print(",".join(result_numbers))
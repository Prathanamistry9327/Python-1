#18. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already 
#ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

# Ans:
str1 = input("Enter a string: ")

if len(str1) >= 3:
    if str1[-3:] == "ing":
        sum = str1 + "ly"
    else:
        sum = str1 + "ing"
else:
    sum = str1

print("SUM: ",sum)
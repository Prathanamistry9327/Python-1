#17.  Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) >= 2 and len(str2) >= 2:
    str3 = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
    print("Result:", str3123)
else:
    print(" 2 char for swap")



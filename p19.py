# 19.Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

#Ans:
str1 = input("Enter a string: ")

index_not = str1.find('not')
index_poor = str1.find('poor')

if index_not != -1 and index_poor != -1 and index_not < index_poor:
    add = string_1[:index_not] + 'good' + string_1[index_poor + 4:]
else:
    add = str1

print("sum: " + add)
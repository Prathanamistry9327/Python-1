main_str = input("Enter the main string: ")
str_to_insert = input("Enter the string to insert: ")

middle_index = len(main_str) // 2
ans = main_str[:middle_index] + str_to_insert + main_str[middle_index:]

print("Ans", ans)
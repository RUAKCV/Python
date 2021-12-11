lst = [1, 2, 2, 3, 3, 3, 3, 4]
user_input = int(input("Insert new number = "))

i = 0
for num in lst:
    if user_input >= num:
        i + = 1
lst.insert(i, user_input)
print(lst)



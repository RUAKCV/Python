a = int(input("Print positive natural number"))
max = a % 10
#print(max)
while a>0:
    number = a % 10
    if number > max:
        max = number
    a = a // 10
print(max)


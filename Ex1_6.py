import math

a = float(input("how many km did you run at first day?"))
b = float(input("what is your target distance?"))
n = 1

while a < b:
    a = a * 1.1
    n+=1
print(n)




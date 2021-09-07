list1 = []
cell=0
while True:
    if cell == "stop":
        list1.remove(cell)
        break
    cell = input("insert element")
    list1.append(cell)

print(list1)

i = 0
for i in range(1,len(list1),2):
    list1[i-1],list1[i] = list1 [i], list1[i-1]

print (list1)

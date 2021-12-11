user_string = input("insert a sentence").split()
#user_string.split()
for i, val in enumerate(user_string,1):
    print(f'#{i} {val[:10]}')


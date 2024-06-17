user = int(input("Please enter a number to check if breaks the hypothesis:\n"))
cnt = 0

while(user != 1):
    if(user % 2 == 0):
        user /= 2
    elif(user % 2  != 0 and user != 1):
        user =  (user *3) +1
    cnt += 1
    print(round(user))

print("steps = ", cnt)
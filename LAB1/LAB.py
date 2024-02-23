first = int(input("Enter something: "))
pivotI = 0
pivotJ = first
for i in range((first)):
    for j in range((first*2)):
        if(i + j == first and i ==0 ):
            print("*", end=" ")
            pivotI +=1
            pivotJ += 1
        elif((i + j == first)):
            print("*", end=" ")
        elif(i == pivotI and j == pivotJ):
            print("*", end=" ")
            pivotI +=1
            pivotJ += 1
        else:
            print(" ", end=" ")
    if(i <= first):
        print()
for i in range((first*4)+1):
    print("*",end="")
print()
if(first > 3):
    for i in range(first-1):
        for j in range(first*2):
            if(j >= first-1 and j <= first+1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        if (j > first):
            print()
else:
    temp = first
    if(temp == 1):
        temp =2
    for i in range(temp-1):
        for j in range(first*2):
            if(j == first):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
for i in range((first*4)+1):
    if(i >= (((first*4))/2)-first and i <= (((first*4))/2)+first):
        print("*",end="")
    else:
        print(" ", end="")

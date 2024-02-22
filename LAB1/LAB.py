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
if(first > 2):
    for i in range(first-2):
        for j in range(first*2):
            if(j >= first-1 and j <= first+1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    for i in range(first-2):
        for j in range(first*2):
            if(j == first):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

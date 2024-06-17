
year = int(input("Please enter an year:\n(year)"))

if(year % 4  !=  0):
    print("Common year")
elif(year % 100 != 0):
    print("Leap year")
elif(year % 400 != 0 ):
    print("Common year")
else:
    print("Leap year")

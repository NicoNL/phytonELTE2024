year = int(input("Please enter a year: "))
while (year < 1582):
    year = int(input("Please enter a VALID year: "))
if(year % 4 == 0 and year % 100 != 0) or ( year % 400 == 0 ):
    print("This is a leap year")
else:
    print("This is a common year")

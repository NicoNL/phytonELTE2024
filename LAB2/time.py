print("Please enter a number of time")

hours=int(input("Starting time(hours):\n"))
mins=int(input("Starting minutes(mins):\n"))
duration=int(input("Please enter the duration(duration):\n"))

while(duration > 0):
    if(duration >= 60):
        duration -=  60
        hours += 1
    if(duration + mins >= 60):
        hours += 1
        temp = 60 - mins
        duration -= temp
        mins = 00
    else:
        mins += duration
        duration = 0

print("The event will finished at",hours, ":", mins)


def correctRanger(num, min, max):
    try:
        int(num)
    except ValueError:
        print("Error: The given input is not a number")
        return False
    if int(num) < min or int(num) > max:
        print("Error: The given number is out of the range")
        return False
    else:
        return True


x = input("Please enter a number from 1-10:\n")

while not correctRanger(x, 1, 10):
    x = input("Please enter a number from 1-10:\n")

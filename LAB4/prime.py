def isPrime(num):
    if(num < 2): return False;
    for i in range(2, int(math.sqrt(num)) +1):
        if(num % i == 0):
            return False;
    return True;

x = int(input("Please enter a number:\n"))
print(isPrime(x))

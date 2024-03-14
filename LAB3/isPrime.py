def is_prime(num):
    divisors = set()
    if(num < 2):
        return False
    for i in range(2,round(num/2)+1):
        if(num % i == 0):
            divisors.add(i)
    if(len(divisors) == 0):
        return True
    return False


x = int(input("Enter number: "))
print(is_prime(x))
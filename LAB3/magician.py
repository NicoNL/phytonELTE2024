import random
print(
"""
+================================+
| Welcome to my game, muggle! |
| Enter an integer number |
| and guess what number I've |
| picked for you. |
| So, what is the secret number? |
+================================+
""")

random_number = random.randint(1,10)


while True:
    user = int(input("Please enter a number:\n"))
    if(user == random_number):
        break;
    print("Ha ha! You're stuck in my loop!")



print("Well done, muggle! You are free now.")

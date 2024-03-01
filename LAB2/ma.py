secret_number = 7

print(
"""""
+================================+
| Welcome to my game, muggle! |
| Enter an integer number |
| guess what numumber I've
|  picked ofr you              |
|So, what's the secret number |
+================================+

""")
x = int(input('Enter your number: '))

while( x != secret_number):
    print("Now you're trapped in my loop")
    x = int(input('Enter your number again: '))

print("Damn bro got it, you free now GG")

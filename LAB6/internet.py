# Code cell 7
def findInternet(word):
    return 'internet' in word.lower().split()

f = findInternet('The Internet Engineering Task Force was created in 1986')
print(f)
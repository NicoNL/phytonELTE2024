word = input("Please enter a word to remove its vowels:\n")
vowels = "aeiouAEIOU"

upper_word = ""
for c in  word:
    if  not (c in vowels):
        upper_word += c.upper()

print("New word  ", upper_word)

# ALTERNATIVE SOLUTION

new_word = ''.join([c.upper() for c in word if c not in vowels])

print("New word:", new_word)

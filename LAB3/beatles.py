beatles = []

# Step 1
beatles.extend(["Jonh Lennon","Paul McCartney","George Harrison"])
print("This are the currrent members of The Beatles", beatles)

#Step 2
for i in range (2):
    member = input("Please add two more members to the band\n")
    beatles.append(member)
print("This are the currrent members of The Beatles", beatles)

#Step 3
beatles.pop(-1)
beatles.pop(-1)
# ALTERNATIVE WAY del beatles[-2:]
print("This are the currrent members of The Beatles", beatles)

#Step 4
beatles.insert(0,"Ringo Starr")
print("This are the currrent members of The Beatles", beatles)

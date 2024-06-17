hat = [1,2,3,4,5]

print("This is the content of the hat", hat)

# Change middle number:
new_middle =  int(input("Please enter a middle number:\n"))
hat[round(len(hat)/2)] = new_middle

print(hat)

# Remove last number
hat.remove(len(hat))

print("Hat after delete the last element: ", hat)

# Print length of the hat
print("Number of elements in the hat: ", len(hat))
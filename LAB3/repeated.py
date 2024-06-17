#Found repeated occurrences

my_list = [1,2,4,4,1,4,2,6,2,9]
new = []
my_list.sort()

for n in my_list:
    if not (n in new):
        new.append(n)

print(new)


#another way
new2 = set(my_list)
print(new2)
t1 = ('apple', 3.14, True, 42)
print(t1)

t2 = (10,55)
t3 = (29,45)

print("Tuples: ", t2, " ", t3)

temp = t2

t2 = t3
t3 = temp

print("Tuples after the swap: ", t2,t3)


t4 = (50,36,60,70,36,75,96)
print("Tuple:", t4)

cnt = 0
for e in t4:
    if 36 == e:
        cnt += 1

print("36 is ", cnt," times in the tuple")
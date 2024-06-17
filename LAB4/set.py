s1 = set()
s1.add("hola")
s1.add(1)
s1.add('d')


s2 = {"szia",4,'d'}

print("First two sets:", s1, " ", s2)

fruits = ["apple","banana","cherry"]
s3 = set()
for f in fruits:
    s3.add(f)

print("Set of fruits: ", s3)

s4 = {15,25,80,85,90}
s5 = {25,80,82,85,100}

print("These are the common elements: ", s4.intersection(s5))


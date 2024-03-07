cnt = 1
def newTask():
    global cnt
    print("Task #" + str(cnt))
    cnt = cnt +1

#task1
newTask()
tuple = ('tuple', 1232, [1,2,34])
print(tuple)
print()

#task2
newTask()
tuple1 = (12,21)
tuple2 = (14,41)


print("Before swapping")
print(tuple1)
print(tuple2)

tuple1,tuple2 = tuple2, tuple1

#task 3 count 36 ocurrences in an tuple
newTask()
tuple = (12,34,35,36,46,36).count(36)
print()
print("Ocurrences of 36 is: ",tuple)
print()

#task 4
newTask()
print("Set with diff element")
set1 = {"hola",123,True}
print(set1)
print()

print("Program for a creating a set")
user_Set = set()
length = input("Please enter a lenght: ")
for i in range(0, int(length)):
    x = input("Please enter a element: ")
    user_Set.add(x)
print(user_Set)

print()
set11 = {1,2,3,4}
set22 = {2,4,5,6}

print("The programin intersection is: ",set22.intersection(set11))
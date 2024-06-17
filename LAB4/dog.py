class Dog:
    def __init__(self,name,age):
       self.name = name
       self.age = age
    def __str__(self):
        return f"{self.name},{self.age}yo"
d1 = Dog("Tom",12)

print(d1)
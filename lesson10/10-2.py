class Person:
    def __init__(self, name, age):
        print("Creating a person object")
        self.name = name
        self.age = age

p1 = Person("Kelvin", "30")
p2 = Person("John", "60")

print(p1)
print(p2)
print(type(p1))

p1.name = "Kelvin"
p1.age = "30"

p2.name = "John"
p2.age = "60"

print(p1.name, p1.age)
print(p2.name, p2.age)
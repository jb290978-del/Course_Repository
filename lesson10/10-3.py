class Person:
    def __init__(self, name, age):
        print("Creating a person object")
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello sailor, my name is", self.name, "and I am", self.age)

    def birthday(self):
        self.age = self.age + 1

p1 = Person("Tarquin", 30)
p1.introduce()

p1.birthday()
p1.introduce()
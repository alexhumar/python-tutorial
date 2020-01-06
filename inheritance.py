class Mammal:
    def __init__(self, name: str):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")


# Python doesn't like empty classes, so if we have empty classes (not a good sign) we should use pass to tell
# interpreter don't worry
class Dog(Mammal):
    def bark(self):
        print(f"{self.name} is barking")


class Cat(Mammal):
    def meow(self):
        print(f"{self.name} is saying meow")


dog1 = Dog("Lucky")
dog1.walk()
dog1.bark()
cat1 = Cat("Rex")
cat1.walk()
cat1.meow()

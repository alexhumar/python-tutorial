class Person:
    name: str

    def __init__(self, name: str):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()
bob = Person("Bob Smith")
bob.talk()

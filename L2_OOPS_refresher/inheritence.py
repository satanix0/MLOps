# Base Class

class Animal:
    def __init__(self, name=None):
        self.name = 'Broski'

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class


class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        print(f"{super().name} barks. and is of {self.breed} breed")


# Create an instance of Animal
animal = Animal("Generic Animal")
animal.speak()

# Create an instance of Dog
dog = Dog("Russian")
dog.speak()

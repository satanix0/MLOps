class Animal:
    def __init__(self):
        """
        Initializes a new instance of the class.

        Attributes:
            name (str): The name of the instance, initialized to None.
            age (int): The age of the instance, initialized to None.
        """
        print("Class instantiated")
        self.name = None
        self.age = None

    def speak(self):
        """
        Prints a message indicating that the object is an animal.
        """
        print("I am an animal")


andy = Animal()
andy.name = "Andy"
andy.age = 4

print(andy.name)
print(andy.age)
andy.speak()

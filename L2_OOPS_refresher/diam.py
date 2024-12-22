# This code demonstrates multiple inheritance and the diamond problem in Python.

class BaseClass:
    def __init__(self):
        self.base_attribute = "Base Attribute"

    def the_method(self):
        return "Method from BaseClass"


class LeftDerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        self.left_attribute = "Left Derived Attribute"

    def the_method(self):
        super().the_method()

        return "Method from LeftDerivedClass"


class RightDerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        self.right_attribute = "Right Derived Attribute"

    def the_method(self):
        super().the_method()

        return "Method from RightDerivedClass"


class DiamondClass(LeftDerivedClass, RightDerivedClass):
    def __init__(self):
        super().__init__()
        self.diamond_attribute = "Diamond Attribute"

    def the_method(self):
        super().the_method()
        return "Method from DiamondClass"


# Creating an instance of DiamondClass
diamond_instance = DiamondClass()

# Accessing attributes and methods from all classes
print(diamond_instance.base_attribute)  # From BaseClass
print(diamond_instance.left_attribute)  # From LeftDerivedClass
print(diamond_instance.right_attribute)  # From RightDerivedClass
print(diamond_instance.diamond_attribute)  # From DiamondClass

print(diamond_instance.the_method())  # From BaseClass
print(diamond_instance.the_method())  # From LeftDerivedClass
print(diamond_instance.the_method())  # From RightDerivedClass
print(diamond_instance.the_method())  # From DiamondClass

# The diamond problem occurs because DiamondClass inherits from both LeftDerivedClass and RightDerivedClass,
# which both inherit from BaseClass. This can cause ambiguity in which method or attribute to use from BaseClass.

# Example of polymorphism in Python using method overriding
class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"
    
def make_sound(animal):
    """
    Function to demonstrate polymorphism by calling the sound method of different animal objects.
    
    :param animal: An instance of Animal or its subclasses
    :return: The sound made by the animal
    """
    return animal.sound()

# Example usage
dog = Dog()
cat = Cat()
print("Dog sound:", make_sound(dog))  # Output: Dog sound: Woof 
print("Cat sound:", make_sound(cat))  # Output: Cat sound: Meow
# This demonstrates polymorphism where the same function make_sound can operate on different types of Animal objects
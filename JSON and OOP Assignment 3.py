# Parent class 'Dog'
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")

# Child class 'JackRussellTerrier'
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_ability):
        super().__init__(name, age, coat_color)
        self.hunting_ability = hunting_ability

    def bark(self):
        print(f"{self.name} is barking!")

    def hunting_skill(self):
        print(f"{self.name} has a hunting ability of {self.hunting_ability}.")

# Child class 'Bulldog'
class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def snore(self):
        print(f"{self.name} is snoring loudly!")

    def show_strength(self):
        print(f"{self.name} has a strength level of {self.strength}.")

# Create objects and test functionalities
dog1 = JackRussellTerrier("Rusty", 3, "White with Brown", "Excellent")
dog2 = Bulldog("Spike", 5, "Fawn", "Strong")

dog1.description()  # Output: Rusty is 3 years old.
dog1.get_info()    # Output: Rusty's coat color is White with Brown.
dog1.bark()         # Output: Rusty is barking!
dog1.hunting_skill()  # Output: Rusty has a hunting ability of Excellent.

dog2.description()  # Output: Spike is 5 years old.
dog2.get_info()    # Output: Spike's coat color is Fawn.
dog2.snore()        # Output: Spike is snoring loudly!
dog2.show_strength()  # Output: Spike has a strength level of Strong.

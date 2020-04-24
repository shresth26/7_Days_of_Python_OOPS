class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def animalDetails(self):
        print("Name :", self.name)
        print("Sound :", self.sound)

class Dog(Animal):
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family

    def animalDetails(self):
        super().animalDetails()
        print("Family :", self.family)

class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def animalDetails(self):
        super().animalDetails()
        print("Color :", self.color)

dog = Dog("Pongo", "Woof Woof", "Carnivore")
dog.animalDetails()
print(" ")
sheep = Sheep("Billy", "Baaa Baaa", "White")
sheep.animalDetails()

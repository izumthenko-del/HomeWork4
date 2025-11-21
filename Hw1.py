class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Some generic animal sound")
    def eat(self):
        print(f"{self.name} is eating.")
class Wolf(Animal):
    def __init__(self, name, type):
        super().__init__(name, "Wolf")
        self.type = type
    def make_sound(self):
        print("Howl!")
    def hunt(self):
        print(f"{self.name} is hunting hares.")
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    def make_sound(self):
        print("Mrrp!")
    def purr(self):
        print(f"{self.name} is purring.")
wolf_1 = Wolf("Fenris", "arctic wolf")
cat_1 = Cat("Oreo", "black and white")

print(f"{wolf_1.name} is a {wolf_1.type} and says:")
wolf_1.make_sound()
wolf_1.eat()
wolf_1.hunt()
print(f"\n{cat_1.name} is a {cat_1.color} and says:")
cat_1.make_sound()
cat_1.eat()
cat_1.purr()

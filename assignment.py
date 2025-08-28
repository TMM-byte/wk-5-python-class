# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power       # Encapsulated attribute
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I wield the power of {self._power}!")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

    def get_power(self):          # Getter for encapsulated attribute
        return self._power

    def set_power(self, new_power):  # Setter for encapsulated attribute
        self._power = new_power

# Subclass 1
class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.name} soars through the skies with {self._power}!")

# Subclass 2
class TechHero(Superhero):
    def use_power(self):
        print(f"{self.name} activates high-tech gear powered by {self._power}!")

# Creating instances
skyhawk = FlyingHero("Skyhawk", "aerokinesis", "Cloud City")
cyberknight = TechHero("CyberKnight", "quantum armor", "Neo-Tokyo")

# Demonstrating polymorphism
heroes = [skyhawk, cyberknight]
for hero in heroes:
    hero.introduce()
    hero.use_power()
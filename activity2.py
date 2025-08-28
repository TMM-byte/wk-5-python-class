# Base class
class Entity:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Vehicle classes
class Car(Entity):
    def move(self):
        print("🚗 Driving on the road.")

class Plane(Entity):
    def move(self):
        print("✈️ Flying through the sky.")

class Boat(Entity):
    def move(self):
        print("🚢 Sailing across the water.")

# Animal classes
class Dog(Entity):
    def move(self):
        print("🐕 Running on four legs.")

class Bird(Entity):
    def move(self):
        print("🐦 Flapping wings and flying.")

class Snake(Entity):
    def move(self):
        print("🐍 Slithering silently.")

# Demonstrating polymorphism
entities = [Car(), Plane(), Boat(), Dog(), Bird(), Snake()]

for entity in entities:
    entity.move()
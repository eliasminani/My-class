# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Derived classes
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🛥️ The boat is sailing on the water.")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each object calls its own version of move()

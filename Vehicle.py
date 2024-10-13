from abc import ABC, abstractmethod

# Abstract Vehicle class
class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

# Car class inherits from Vehicle
class Car(Vehicle):
    def drive(self, distance):
        # Car has increased fuel consumption in summer due to AC
        required_fuel = distance * (self.fuel_consumption + 0.9)
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel
            print(f"The car has driven {distance} km. Remaining fuel: {self.fuel_quantity:.2f} liters.")
        else:
            print("The car does not have enough fuel to drive the specified distance.")

    def refuel(self, fuel):
        # Car adds all the given fuel to its tank
        self.fuel_quantity += fuel
        print(f"The car has been refueled with {fuel} liters. Total fuel: {self.fuel_quantity:.2f} liters.")

# Truck class inherits from Vehicle
class Truck(Vehicle):
    def drive(self, distance):
        # Truck has increased fuel consumption in summer due to AC
        required_fuel = distance * (self.fuel_consumption + 1.6)
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel
            print(f"The truck has driven {distance} km. Remaining fuel: {self.fuel_quantity:.2f} liters.")
        else:
            print("The truck does not have enough fuel to drive the specified distance.")

    def refuel(self, fuel):
        # Truck retains only 95% of the fuel due to a hole in the tank
        actual_fuel = fuel * 0.95
        self.fuel_quantity += actual_fuel
        print(f"The truck has been refueled with {fuel} liters. Total fuel after retaining 95%: {self.fuel_quantity:.2f} liters.")

# Example usage
car = Car(fuel_quantity=20, fuel_consumption=5)  # Car starts with 20 liters, consumes 5 liters/km
truck = Truck(fuel_quantity=50, fuel_consumption=8)  # Truck starts with 50 liters, consumes 8 liters/km

# Drive and refuel the car
car.drive(3)  # Attempt to drive 3 km
car.refuel(10)  # Refuel with 10 liters

# Drive and refuel the truck
truck.drive(4)  # Attempt to drive 4 km
truck.refuel(20)  # Refuel with 20 liters

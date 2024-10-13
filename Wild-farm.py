from abc import ABC, abstractmethod

# Food classes
class Food(ABC):
    def __init__(self, quantity: int):
        self.quantity = quantity

class Vegetable(Food):
    pass

class Fruit(Food):
    pass

class Meat(Food):
    pass

class Seed(Food):
    pass

# Animal classes
class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

class Bird(Animal):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

# Bird subclasses
class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"
    
    def feed(self, food):
        if not isinstance(food, Meat):
            return f"Owl does not eat {food.__class__.__name__}!"
        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity

class Hen(Bird):
    def make_sound(self):
        return "Cluck"
    
    def feed(self, food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity

# Mammal subclasses
class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"
    
    def feed(self, food):
        if isinstance(food, (Vegetable, Fruit)):
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Mouse does not eat {food.__class__.__name__}!"

class Dog(Mammal):
    def make_sound(self):
        return "Woof!"
    
    def feed(self, food):
        if not isinstance(food, Meat):
            return f"Dog does not eat {food.__class__.__name__}!"
        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity

class Cat(Mammal):
    def make_sound(self):
        return "Meow"
    
    def feed(self, food):
        if isinstance(food, (Vegetable, Meat)):
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Cat does not eat {food.__class__.__name__}!"

class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"
    
    def feed(self, food):
        if not isinstance(food, Meat):
            return f"Tiger does not eat {food.__class__.__name__}!"
        self.weight += 1.00 * food.quantity
        self.food_eaten += food.quantity

# Test the hierarchy
if __name__ == "__main__":
    hen = Hen("Hen", 1.5, 0.2)
    print(hen)
    print(hen.make_sound())
    print(hen.feed(Vegetable(2)))
    print(hen)
    
    tiger = Tiger("Tiger", 200, "Jungle")
    print(tiger)
    print(tiger.make_sound())
    print(tiger.feed(Fruit(2)))
    print(tiger.feed(Meat(5)))
    print(tiger)

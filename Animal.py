from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}."


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow meow!"


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")  # Gender được tự động thiết lập thành "Female"

    def make_sound(self):
        return "Meow"


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")  # Gender được tự động thiết lập thành "Male"

    def make_sound(self):
        return "Hiss"


# Test các lớp
if __name__ == "__main__":
    dog = Dog("Buddy", 5, "Male")
    print(dog)              # In ra: This is Buddy. Buddy is a 5 year old Male Dog.
    print(dog.make_sound()) # In ra: Woof!

    kitten = Kitten("Luna", 1)
    print(kitten)           # In ra: This is Luna. Luna is a 1 year old Female Kitten.
    print(kitten.make_sound()) # In ra: Meow

    tomcat = Tomcat("Tom", 3)
    print(tomcat)           # In ra: This is Tom. Tom is a 3 year old Male Tomcat.
    print(tomcat.make_sound()) # In ra: Hiss

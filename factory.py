from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

def get_animal_sound(factory):
    animal = factory.create_animal()
    return animal.speak()


if __name__ == "__main__":
    dog_factory = DogFactory()
    print(get_animal_sound(dog_factory))
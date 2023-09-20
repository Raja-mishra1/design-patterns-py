from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a circle !!!"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a rectangle !!"

class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

class Red(Color):
    def fill(self):
        return "Filling Red color !!"

class Blue(Color):
    def fill(self):
        return "Filling Blue Color !!"

class AbstractFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

    @abstractmethod
    def create_color(self):
        pass

class ShapeFactory(AbstractFactory):
    def create_color(self):
        return Red()
    def create_shape(self):
        return Rectangle()

class ColorFactory(AbstractFactory):
    def create_shape(self):
        return Rectangle()
    def create_color(self):
        return Blue()


def draw_and_fill(factory):
    shape = factory.create_shape()
    color = factory.create_color()
    return f'{shape.draw()},{color.fill()}'

if __name__ == "__main__":
    shape_factory = ShapeFactory()
    color_factory = ColorFactory()

    print(draw_and_fill(shape_factory))
    print(draw_and_fill(color_factory))
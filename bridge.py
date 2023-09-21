from abc import ABC , abstractmethod

class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f'API1 , drawing a circle at ({x}, {y}) and radius{radius} ')

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f'API2 , drawing a circle at ({x}, {y}) and radius{radius} ')


class Shape(ABC):
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    @abstractmethod
    def draw(self):
        pass

class CircleShape(Shape):
    def __init__(self, x, y, radius, drawing_api):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)


if __name__ == '__main__':
    circle1 = CircleShape(1, 2, 3, DrawingAPI1())
    circle1.draw()

    circle2 = CircleShape(1, 2, 5, DrawingAPI2())
    circle2.draw()
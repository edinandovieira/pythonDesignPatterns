from copy import deepcopy


class Shape():
    def clone(self):
        pass

    def draw(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def clone(self):
        return deepcopy(self)

    def draw(self):
        print(f"Drawing Rectangle With width {self.width} and height {self.height}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        return deepcopy(self)

    def draw(self):
        print(f"Drawing Circle With radius {self.radius}")


if __name__ == "__main__":
    originalRectangle = Rectangle(10, 5)
    originalCicle = Circle(7)

    clonedRectangle = originalRectangle.clone()
    clonedCircle = originalCicle.clone()

    originalRectangle.draw()
    originalCicle.draw()

    clonedRectangle.draw()
    clonedCircle.draw()

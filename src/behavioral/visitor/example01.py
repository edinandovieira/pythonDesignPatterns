from __future__ import annotations
from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, dot: Dot):
        pass

    @abstractmethod
    def visit_circle(self, circle: Circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle):
        pass

    @abstractmethod
    def visit_compound_shape(self, compound_shape: CompoundShape):
        pass


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class Dot(Shape):
    def accept(self, visitor: Visitor):
        visitor.visit_dot(self)


class Circle(Shape):
    def accept(self, visitor: Visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):
    def accept(self, visitor: Visitor):
        visitor.visit_rectangle(self)


class CompoundShape(Shape):
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def accept(self, visitor: Visitor):
        visitor.visit_compound_shape(self)
        for child in self.children:
            child.accept(visitor)


class XMLExportVisitor(Visitor):
    def visit_dot(self, dot: Dot):
        print('Exportando Dot para XML')

    def visit_circle(self, circle: Circle):
        print('Exportando Circle para XML')

    def visit_rectangle(self, rectangle: Rectangle):
        print('Exportando Rectangle para XML')

    def visit_compound_shape(self, compound_shape: CompoundShape):
        print('Exportando CompoundShape para XML')
        for child in compound_shape.children:
            child.accept(self)


if __name__ == '__main__':
    dot = Dot()
    circle = Circle()
    rectangle = Rectangle()

    compound_shape = CompoundShape()
    compound_shape.add_child(dot)
    compound_shape.add_child(circle)

    xml_exporter = XMLExportVisitor()

    dot.accept(xml_exporter)
    circle.accept(xml_exporter)
    rectangle.accept(xml_exporter)
    compound_shape.accept(xml_exporter)
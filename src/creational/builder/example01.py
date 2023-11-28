from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def build_chassis(self) -> None:
        pass

    @abstractmethod
    def build_engine(self) -> None:
        pass

    @abstractmethod
    def build_body(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass


class Car():
    def __init__(self) -> None:
        self.parts = []

    def add_part(self, part) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Car parts: {', '.join(self.parts)}", end="")


class CarBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Car()

    @property
    def product(self) -> Car:
        car = self._product
        self.reset()
        return car

    def build_chassis(self) -> None:
        self._product.add_part("Chassis")

    def build_engine(self) -> None:
        self._product.add_part("Engine")

    def build_body(self) -> None:
        self._product.add_part("Body")


class Director():
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def makeBasicCar(self) -> None:
        self.builder.build_chassis()
        self.builder.build_engine()

    def makeFullCar(self) -> None:
        self.builder.build_chassis()
        self.builder.build_engine()
        self.builder.build_body()


if __name__ == "__main__":
    director = Director()
    builder = CarBuilder()
    director.builder = builder

    print("Basica Car: ")
    director.makeBasicCar()
    builder.product.list_parts()

    print("\n")

    print("Fully Car: ")
    director.makeFullCar()
    builder.product.list_parts()

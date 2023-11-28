from abc import ABC, abstractmethod


class Car():
    def __init__(self):
        self.reset()

    def reset(self):
        self.seats = 0
        self.engine = ""
        self.trip_computer = False
        self.gps = False

    def __str__(self):
        return f"Carro com {self.seats} assentos, motor {self.engine}, {'com' if self.trip_computer else 'sem'}, {'com' if self.gps else 'sem'} GPS."


class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setSeats(self, number: int):
        pass

    @abstractmethod
    def setEngine(self, engine: str):
        pass

    @abstractmethod
    def setTripComputer(self):
        pass

    @abstractmethod
    def setGPS(self):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def reset(self):
        self.car.reset()

    def setSeats(self, number: int):
        self.car.seats = number

    def setEngine(self, engine: str):
        self.car.engine = engine

    def setTripComputer(self):
        self.car.trip_computer = True

    def setGPS(self):
        self.car.gps = True

    def getCar(self):
        return self.car


class Director():
    def makeSUV(self, builder: Builder):
        builder.reset()
        builder.setSeats(5)
        builder.setEngine("V8")
        builder.setTripComputer()
        builder.setGPS()

    def makeSportsCar(self, builder: Builder):
        builder.reset()
        builder.setSeats(2)
        builder.setEngine("V12")
        builder.setTripComputer()
        builder.setGPS()


if __name__ == "__main__":
    director = Director()

    carBuilder = CarBuilder()
    director.makeSUV(carBuilder)
    car = carBuilder.getCar()
    print('SUV: ')
    print(car)

    director.makeSportsCar(carBuilder)
    car = carBuilder.getCar()
    print('Sports: ')
    print(car)

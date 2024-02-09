from __future__ import annotations
from abc import ABC, abstractmethod

class Move():
    def __init__(self, transport: TransportStrategy) -> None:
        self._transport: TransportStrategy = transport

    @property
    def getInfo(self):
        return f'A viagem de {self._transport.__class__.__name__} custará {self._transport.getPrice()} e levará cerca de {self._transport.getTime()}'


class TransportStrategy(ABC):
    @abstractmethod
    def getPrice(self) -> float:
        pass

    @abstractmethod
    def getTime(self) -> str:
        pass


class Bycicle(TransportStrategy):
    def __init__(self) -> None:
        self._price: float = 0.00
        self._time: str = '60 minutes'

    def getPrice(self) -> float:
        return self._price

    def getTime(self) -> str:
        return self._time


class Bus(TransportStrategy):
    def __init__(self) -> None:
        self._price: float = 2.00
        self._time: str = '30 minutes'

    def getPrice(self) -> float:
        return self._price

    def getTime(self) -> str:
        return self._time


class Taxi(TransportStrategy):
    def __init__(self) -> None:
        self._price: float = 10.00
        self._time: str = '10 minutes'

    def getPrice(self) -> float:
        return self._price

    def getTime(self) -> str:
        return self._time


class Uber(TransportStrategy):
    def __init__(self) -> None:
        self._price: float = 5.00
        self._time: str = '15 minutes'

    def getPrice(self) -> float:
        return self._price

    def getTime(self) -> str:
        return self._time


if __name__ == '__main__':
    bike = Bycicle()
    bus = Bus()
    taxi = Taxi()
    uber = Uber()
    trip01 = Move(bike)
    print(trip01.getInfo)
    trip02 = Move(bus)
    print(trip02.getInfo)
    trip03 = Move(taxi)
    print(trip03.getInfo)
    trip04 = Move(uber)
    print(trip04.getInfo)
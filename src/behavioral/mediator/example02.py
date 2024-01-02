from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Mediator(ABC):
    @abstractmethod
    def register_aircraft(self, aircraft):
        pass

    @abstractmethod
    def communicate(self, sender, message):
        pass


class TowerControl():
    def __init__(self) -> None:
        self.aircrafts: List[Aircraft] = []

    def register_aircraft(self, aircraft: Aircraft) -> None:
        self.aircrafts.append(aircraft)
        aircraft.set_tower(self)

    def communicate(self, sender: Aircraft, message: str) -> None:
        for aircraft in self.aircrafts:
            if aircraft != sender:
                aircraft.receive_message(sender, message)


class Aircraft(ABC):
    def __init__(self, name: str):
        self.name = name
        self.tower: TowerControl

    @abstractmethod
    def set_tower(self, tower: TowerControl) -> None:
        pass

    @abstractmethod
    def send_message(self, message: str) -> None:
        pass

    @abstractmethod
    def receive_message(self, sender: Aircraft, message: str) -> None:
        pass


class Airplane(Aircraft):
    def set_tower(self, tower: TowerControl) -> None:
        self.tower = tower

    def send_message(self, message: str) -> None:
        print(f'{self.name} sends: {message}')
        self.tower.communicate(self, message)

    def receive_message(self, sender: Aircraft, message: str) -> None:
        print(f'Tower transmition message to {self.name}: {sender.name} {message}')


class Helicopter(Aircraft):
    def set_tower(self, tower: TowerControl) -> None:
        self.tower = tower

    def send_message(self, message: str) -> None:
        print(f'{self.name} sends: {message}')
        self.tower.communicate(self, message)

    def receive_message(self, sender: Aircraft, message: str) -> None:
        print(f'Tower transmition message to {self.name}: {sender.name} {message}')


class Jet(Aircraft):
    def set_tower(self, tower: TowerControl) -> None:
        self.tower = tower

    def send_message(self, message: str) -> None:
        print(f'{self.name} sends: {message}')
        self.tower.communicate(self, message)

    def receive_message(self, sender: Aircraft, message: str) -> None:
        print(f'Tower transmition message to {self.name}: {sender.name} {message}')


if __name__ == '__main__':
    tower = TowerControl()

    airplane = Airplane('Airplane 001')
    helicopter = Helicopter('Helicopter 001')
    jet = Jet('Jet 001')

    tower.register_aircraft(airplane)
    tower.register_aircraft(helicopter)
    tower.register_aircraft(jet)

    airplane.send_message('Prepare for landing.')
    helicopter.send_message('Requesting permission to take off.')
    airplane.send_message('Changing altitude')
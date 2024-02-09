from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class EventManager():
    def __init__(self) -> None:
        self._observers: List[EventListeners] = []
        self._listeners: str = ''

    def subscribe(self, observer: EventListeners) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: EventListeners) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, data: str) -> None:
        for observer in self._observers:
            observer.update(data)


class EventListeners(ABC):
    @abstractmethod
    def update(self, filename: str) -> None:
        pass


class EmailAlertsListeners(EventListeners):
    def __init__(self, observable: EventManager)-> None:
        self.observable = observable

    def update(self, filename: str) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'Notificação por e-mail arquivo novo {filename}')


class LoggingListeners(EventListeners):
    def __init__(self, observable: EventManager)-> None:
        self.observable = observable

    def update(self, filename: str) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'Caixa de entrada no sistema arquivo novo {filename}')


if __name__ == '__main__':
    event = EventManager()

    email = EmailAlertsListeners(event)
    logging = LoggingListeners(event)

    event.subscribe(email)
    event.subscribe(logging)

    event.notify('magazine_001.jpg')
    event.notify('magazine_002.jpg')
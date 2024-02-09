from __future__ import annotations
from typing import Dict, List
from copy import deepcopy


class Memento():
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__('_state', state)

    def get_state(self) -> Dict:
        return self._state

    def __setattr__(self, name, value):
        raise AttributeError('Sorry, I am immutable')


class Editor():
    def __init__(self, text: str, currentFont: str) -> None:
        self.text = text
        self.currentFont = currentFont

    def makeSnapshot(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'


class Snapshot():
    def __init__(self, originator: Editor):
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.makeSnapshot())

    def restore(self) -> None:
        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())


if __name__ == '__main__':
    text = Editor('abcd', 'Arial')
    snapshot = Snapshot(text)

    snapshot.backup()

    text.currentFont = 'Roboto'
    snapshot.restore()

    print(text)
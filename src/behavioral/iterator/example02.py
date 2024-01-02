from collections.abc import Iterator, Iterable
from typing import List, Any


class AlphabetIterAsc(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = sorted(collection)
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return str(self._collection)


class AlphabetIterDesc(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = sorted(collection, reverse=True)
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return str(self._collection)


class AlphabetIterVowel(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = [char for char in sorted(collection) if char in 'aeiou']
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return str(self._collection)


class AlphabetIterConsonant(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = [char for char in sorted(collection) if char not in 'aeiou']
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return str(self._collection)


class Alphabetic(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = list('afghbctuvwxdpqreijklmnosyz')

    def __iter__(self):
        pass

    def ascending_iter(self) -> Iterator:
        return AlphabetIterAsc(self._items)

    def descending_iter(self) -> Iterator:
        return AlphabetIterDesc(self._items)

    def vowel_iter(self) -> Iterator:
        return AlphabetIterVowel(self._items)

    def consonant_iter(self) -> Iterator:
        return AlphabetIterConsonant(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'

if __name__ == '__main__':
    mylist = Alphabetic()

    print(mylist.ascending_iter())

    print(mylist.descending_iter())

    print(mylist.vowel_iter())

    print(mylist.consonant_iter())

    for value in mylist.ascending_iter():
        print(value)

    print()

    for value in mylist.descending_iter():
        print(value)

    print()

    for value in mylist.vowel_iter():
        print(value)

    print()

    for value in mylist.consonant_iter():
        print(value)
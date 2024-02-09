from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Union


class FileSystemComponent(ABC):
    """ Component """
    @abstractmethod
    def display(self) -> Union[str, List[str]]:
        pass

    def add(self, child: FileSystemComponent) -> None:
        pass

    def remove(self, child: FileSystemComponent) -> None:
        pass


class Directory(FileSystemComponent):
    """ Composite """
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[FileSystemComponent] = []

    def display(self) -> List[str]:
        return [child.display() for child in self._children]  # type: ignore

    def add(self, child: FileSystemComponent) -> None:
        self._children.append(child)

    def remove(self, child: FileSystemComponent) -> None:
        if child in self._children:
            self._children.remove(child)


class File(FileSystemComponent):
    """ Leaf """
    def __init__(self, name: str) -> None:
        self.name = name

    def display(self) -> str:
        return self.name


if __name__ == '__main__':
    # Leaf
    file1 = File('example.txt')
    file2 = File('document.doc')
    print(file1.display())
    print(file2.display())

    # Composite
    directory = Directory('MyFolder')
    directory.add(file1)
    directory.add(file2)
    print(directory.display())

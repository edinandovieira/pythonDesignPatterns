from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class OrganizationComponent(ABC):
    """ Component """
    @abstractmethod
    def display(self) -> str:
        pass

    def add(self, child: OrganizationComponent) -> None:
        pass

    def remove(self, child: OrganizationComponent) -> None:
        pass


class Department(OrganizationComponent):
    """ Composite """
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[OrganizationComponent] = []

    def display(self) -> str:
        return f"""{self.__class__.__name__}: {self.name}
    {[child.display() for child in self._children]}"""

    def add(self, child: OrganizationComponent) -> None:
        self._children.append(child)

    def remove(self, child: OrganizationComponent) -> None:
        if child in self._children:
            self._children.remove(child)


class Employee(OrganizationComponent):
    """ Leaf """
    def __init__(self, name: str) -> None:
        self.name = name

    def display(self) -> str:
        return self.name


if __name__ == '__main__':
    # Leaf
    employee1 = Employee('Diego Elias Assunção')
    employee2 = Employee('Lara Marlene Brenda Ramos')
    employee3 = Employee('Danilo Nathan da Rocha')
    employee4 = Employee('Allana Brenda Duarte')
    employee5 = Employee('Débora Isabella Tereza da Paz')
    employee6 = Employee('Antonio Eduardo Melo')
    print(employee1.display())
    print(employee2.display())

    # Composite
    department1 = Department('Accounting')
    department1.add(employee1)
    department1.add(employee2)
    department2 = Department('Technology')
    department2.add(employee3)
    department2.add(employee4)
    department3 = Department('Financial')
    department3.add(employee5)
    department3.add(employee6)
    print(department1.display())
    print(department2.display())
    print(department3.display())

    company = Department('Company')
    company.add(department1)
    company.add(department2)
    company.add(department3)
    print(company.display())

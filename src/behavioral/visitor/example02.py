from __future__ import annotations
from abc import ABC, abstractmethod


class InsuranceVisitor(ABC):
    @abstractmethod
    def visit_building(self, building: Building) -> None:
        pass
    
    @abstractmethod
    def visit_residence(self, residence: Residence) -> None:
        pass

    @abstractmethod
    def visit_bank(self, bank: Bank) -> None:
        pass

    @abstractmethod
    def visit_coffee_make(self, coffee_make: CoffeeMaker) -> None:
        pass


class Property(ABC):
    @abstractmethod
    def accept_insurance_visitor(self, visitor: InsuranceVisitor) -> None:
        pass


class Building(Property):
    def accept_insurance_visitor(self, visitor: InsuranceVisitor) -> None:
        visitor.visit_building(self)


class Residence(Property):
    def accept_insurance_visitor(self, visitor: InsuranceVisitor) -> None:
        visitor.visit_residence(self)


class Bank(Property):
    def accept_insurance_visitor(self, visitor: InsuranceVisitor) -> None:
        visitor.visit_bank(self)


class CoffeeMaker(Property):
    def accept_insurance_visitor(self, visitor: InsuranceVisitor) -> None:
        visitor.visit_coffee_make(self)


class InsuranceAgent(InsuranceVisitor):
    def __init__(self):
        self.insurance_type = None

    def visit_building(self, building: Building) -> None:
        self.insurance_type = "Seguro Médico"

    def visit_residence(self, residence: Residence) -> None:
        self.insurance_type = "Seguro Médico"

    def visit_bank(self, bank: Bank) -> None:
        self.insurance_type = "Seguro contra Roubo"

    def visit_coffee_make(self, coffee_make: CoffeeMaker) -> None:
        self.insurance_type = "Seguro contra Incêndio"


if __name__ == '__main__':
    properties = [Building(), Residence(), Bank(), CoffeeMaker()]

    insurance_agent = InsuranceAgent()

    for property in properties:
        property.accept_insurance_visitor(insurance_agent)
        print(f'Tipo de suro para a {property.__class__.__name__} é {insurance_agent.insurance_type}')
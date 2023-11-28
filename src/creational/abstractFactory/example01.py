from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def hasLegs(self):
        pass

    @abstractmethod
    def sitOn(self):
        pass


class VictorianChair(Chair):
    def hasLegs(self):
        return 'Tem Pernas'

    def sitOn(self):
        return 'Pode sentar na cadeira Vitoriana'


class ModernChair(Chair):
    def hasLegs(self):
        return 'Tem Pernas'

    def sitOn(self):
        return 'Pode sentar na cadeira Moderna'


class FurnitureFactory(ABC):
    @abstractmethod
    def createChair(self) -> Chair:
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    def createChair(self) -> Chair:
        return VictorianChair()


class ModernFurnitureFactory(FurnitureFactory):
    def createChair(self) -> Chair:
        return ModernChair()


def client_code(factory: FurnitureFactory) -> None:
    chair = factory.createChair()
    print(chair.sitOn())


client_code(VictorianFurnitureFactory())
client_code(ModernFurnitureFactory())

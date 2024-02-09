from abc import ABC, abstractmethod


class House(ABC):
    def prepare(self) -> None:
        self.walls()
        self.doors()
        self.windows()
        self.roof()
        self.garage()

    def walls(self) -> None:
        print(f'{self.__class__.__name__}: subindo paredes')

    def doors(self) -> None:
        print(f'{self.__class__.__name__}: colocando portas')

    def windows(self) -> None:
        print(f'{self.__class__.__name__}: colocando janelas')

    @abstractmethod
    def roof(self) -> None:
        pass

    @abstractmethod
    def garage(self) -> None:
        pass


class SimpleHouse(House):
    def roof(self) -> None:
        print(f'{self.__class__.__name__}: colocando telhado simples')

    def garage(self) -> None:
        pass


class SimpleHouseWithGarage(House):
    def roof(self) -> None:
        print(f'{self.__class__.__name__}: colocando telhado simples')

    def garage(self) -> None:
        print(f'{self.__class__.__name__}: colocando portão da garagem')


class HouseWithGarageAndChimney(House):
    def roof(self) -> None:
        print(f'{self.__class__.__name__}: colocando telhado com chaminé')

    def garage(self) -> None:
        print(f'{self.__class__.__name__}: colocando portão da garagem')


if __name__ == '__main__':
    casa01 = SimpleHouse()
    casa01.prepare()

    casa02 = SimpleHouseWithGarage()
    casa02.prepare()

    casa03 = HouseWithGarageAndChimney()
    casa03.prepare()
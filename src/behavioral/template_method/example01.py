from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self) -> None:
        self.hook_before_add_ingredients()
        self.add_ingredients()
        self.hook_after_add_ingredients()
        self.cook()
        self.cut()
        self.serve()

    def hook_before_add_ingredients(self) -> None:
        pass

    def hook_after_add_ingredients(self) -> None:
        pass

    @abstractmethod
    def add_ingredients(self) -> None:
        pass

    @abstractmethod
    def cook(self) -> None:
        pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando pizza.')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Servindo pizza.')


class FourCheese(Pizza):
    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: Mussarela, Parmesão, Provolone e Requeijão')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: cozinhado por 45min no forno a lenha')


class Calabresa(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: Cortar a calabresa em rodelas')

    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: Calabresa e Mussarela')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: cozinhado por 15min no forno comum')


if __name__ == '__main__':
    fourCheese = FourCheese()
    fourCheese.prepare()

    calabresa = Calabresa()
    calabresa.prepare()
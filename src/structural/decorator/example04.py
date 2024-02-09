class Pessoa():
    def vestir(self) -> str:
        return 'Pessoa '


class BaseDecorator(Pessoa):
    def __init__(self, person: Pessoa) -> None:
        self._person = person

    def vestir(self) -> str:
        return self._person.vestir()


class Camisa(BaseDecorator):
    def vestir(self) -> str:
        return f"{super().vestir()} {self.__class__.__name__}"


class Camiseta(BaseDecorator):
    def vestir(self) -> str:
        return f"{super().vestir()} {self.__class__.__name__}"


class Casaco(BaseDecorator):
    def vestir(self) -> str:
        return f"{super().vestir()} {self.__class__.__name__}"


class CapaDeChuva(BaseDecorator):
    def vestir(self) -> str:
        return f"{super().vestir()} {self.__class__.__name__}"


if __name__ == "__main__":
    simple = Pessoa()
    print(simple.vestir())
    print("\n")
    decorator1 = Camisa(simple)
    decorator2 = Casaco(decorator1)
    print(decorator2.vestir())

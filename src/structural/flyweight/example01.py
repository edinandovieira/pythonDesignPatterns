from typing import List, Dict


class Address:
    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            self._street, address_number, self._neighborhood, address_details,
            self._zip_code
        )


class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto')

        return address_flyweight


if __name__ == "__main__":
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='Av Brasil',
        neighborhood='Centro',
        zip_code='00000-000'
    )

    a2 = address_factory.get_address(
        street='Av Brasil',
        neighborhood='Centro',
        zip_code='00000-000'
    )

    luiz = Client('Luiz')
    luiz.address_number = '50'
    luiz.address_details = 'Casa'
    luiz.add_address(a1)
    luiz.list_addresses()

    joana = Client('Joana')
    joana.address_number = '250A'
    joana.address_details = 'AP 555'
    joana.add_address(a2)
    joana.list_addresses()

    print(a1 == a2)

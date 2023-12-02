from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict


class IUser(ABC):
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_all_user_data(self) -> Dict:
        pass


class RealUser(IUser):

    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2) # Simulating requisition
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2) # Simulating requisition
        return [
            {'Rua': 'Av. Brasil', 'Número': 500}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2) # Simulating requisition
        return {'CPF': '111.111.111-11', 'RG': 'MG111222444'}


class UserProxy(IUser):

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        self._real_user: RealUser
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == "__main__":
    luiz = UserProxy('Luiz', 'Otávio')

    print(luiz.firstname)
    print(luiz.lastname)

    print(luiz.get_all_user_data())
    print(luiz.get_addresses())
    
    print('CACHED DATA:')
    for i in range(50):
        print(luiz.get_all_user_data())
        print(luiz.get_addresses())
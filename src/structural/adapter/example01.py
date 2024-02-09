from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None:
        pass

    @abstractmethod
    def right(self) -> None:
        pass

    @abstractmethod
    def down(self) -> None:
        pass

    @abstractmethod
    def left(self) -> None:
        pass


class Control(IControl):
    def top(self) -> None:
        print('movendo para cima')

    def right(self) -> None:
        print('movendo para direita')

    def down(self) -> None:
        print('movendo para baixo')

    def left(self) -> None:
        print('movendo para esquerda')


class NewControl:
    def move_top(self) -> None:
        print('movendo para cima')

    def move_right(self) -> None:
        print('movendo para direita')

    def move_down(self) -> None:
        print('movendo para baixo')

    def move_left(self) -> None:
        print('movendo para esquerda')


#Aqui entra o Adapter de NewControl para Control
class ControlAdapter():
    def __init__(self, newControl: NewControl) -> None:
        self.newControl = newControl

    def top(self) -> None:
        self.newControl.move_top()

    def right(self) -> None:
        self.newControl.move_right()

    def down(self) -> None:
        self.newControl.move_down()

    def left(self) -> None:
        self.newControl.move_left()


if __name__ == '__main__':
    newControl = NewControl()
    c1 = ControlAdapter(newControl)

    c1.top()
    c1.right()
    c1.down()
    c1.left()

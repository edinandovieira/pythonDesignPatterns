class Notifier():
    def __init__(self, message: str):
        self._message = message

    def send(self) -> str:
        return self._message


class BaseDecorator(Notifier):
    def __init__(self, Notifier: Notifier) -> None:
        self._Notifier = Notifier

    @property
    def Notifier(self) -> Notifier:
        return self._Notifier

    def send(self) -> str:
        return self._Notifier.send()


class SMSDecorator(BaseDecorator):
    def send(self) -> str:
        return f"SMSDecorator({self.Notifier.send()})"


class FacebookDecorator(BaseDecorator):
    def send(self) -> str:
        return f"FacebookDecorator({self.Notifier.send()})"


class SlackDecorator(BaseDecorator):
    def send(self) -> str:
        return f"SlackDecorator({self.Notifier.send()})"


def client_code(Notifier: Notifier) -> None:
    print(f"RESULT: {Notifier.send()}", end="")


if __name__ == "__main__":
    simple = Notifier('Alerta de mensagem')
    print("Client: Notificação Simples:")
    client_code(simple)
    print("\n")
    decorator1 = SMSDecorator(simple)
    decorator2 = FacebookDecorator(decorator1)
    print("Client: Notificação por decorador")
    client_code(decorator2)

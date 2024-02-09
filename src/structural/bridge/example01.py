from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def isEnabled(self) -> None:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def getVolume(self) -> None:
        pass

    @abstractmethod
    def setVolume(self, percent: int) -> None:
        pass

    @abstractmethod
    def getChannel(self) -> None:
        pass

    @abstractmethod
    def setChannel(self, channel: int) -> None:
        pass


class TV(Device):
    def __init__(self) -> None:
        self._volume = 10
        self._power = False
        self._channel = 1

    def isEnabled(self) -> None:
        if self._power:
            return True
        else:
            return False

    def enable(self) -> None:
        self._power = True

    def disable(self) -> None:
        self._power = False

    def getVolume(self) -> None:
        return self._volume

    def setVolume(self, percent: int) -> None:
        self._volume = percent

    def getChannel(self) -> None:
        return self._channel

    def setChannel(self, channel: int) -> None:
        self._channel = channel


class Radio(Device):
    def __init__(self) -> None:
        self._volume = 10
        self._power = False
        self._channel = 1

    def isEnabled(self) -> None:
        if self._power:
            return True
        else:
            return False

    def enable(self) -> None:
        self._power = True

    def disable(self) -> None:
        self._power = False

    def getVolume(self) -> None:
        return self._volume

    def setVolume(self, percent: int) -> None:
        self._volume = percent

    def getChannel(self) -> None:
        return self._channel

    def setChannel(self, channel: int) -> None:
        self._channel = channel

# Meu Bridge
class RemoteControl():
    def __init__(self, device: Device) -> None:
        self._device = device

    def togglePower(self):
        if self._device.isEnabled():
            self._device.disable()
        else:
            self._device.enable()

    def volumeDown(self):
        self._device.setVolume(self._device.getVolume() - 10)

    def volumeUp(self):
        self._device.setVolume(self._device.getVolume() + 10)

    def channelDown(self):
        self._device.setChannel(self._device.getChannel() - 1)

    def channelUp(self):
        self._device.setChannel(self._device.getChannel() + 1)


class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self._device.setVolume(0)


if __name__ == '__main__':
    tv = TV()
    remoteTV = RemoteControl(tv)
    remoteTV.togglePower()

    radio = Radio()
    remoteRadio = AdvancedRemoteControl(radio)
    print(radio.isEnabled())
    remoteRadio.togglePower()
    print(radio.isEnabled())
    print(radio.getVolume())
    remoteRadio.volumeUp()
    print(radio.getVolume())

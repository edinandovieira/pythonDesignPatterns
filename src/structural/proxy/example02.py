from abc import ABC, abstractmethod
from time import sleep

# Interface of real object
class Image(ABC):
    @abstractmethod
    def display(self):
        pass


# Real Object
class RealImage(Image):
    def __init__(self, filename: str) -> None:
        self._filename: str = filename
        self._load_image()

    def _load_image(self) -> None:
        sleep(2)
        print(f"Loading image from file: {self._filename}")

    def display(self) -> str:
        sleep(2)
        print(f"Displaying image First: {self._filename}")
        return f"Displaying image: {self._filename}"


# Proxy
class ImageProxy(Image):
    def __init__(self, filename: str) -> None:
        self._filename: str = filename
        self._real_image: RealImage
        
        self._real_image_display: str

    def display(self) -> str:
        if not hasattr(self, '_real_image'):
            self._real_image = RealImage(self._filename)
            self._real_image_display = self._real_image.display()

        return self._real_image_display


if __name__ == "__main__":
    image_proxy = ImageProxy("example.jpg")

    print(image_proxy.display())
    print(image_proxy.display())
    print(image_proxy.display())
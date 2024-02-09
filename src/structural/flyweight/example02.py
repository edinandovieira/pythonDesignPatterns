from typing import Dict


class Font():
    def __init__(self, name: str, size: int, color: str) -> None:
        self._name = name
        self._size = size
        self._color = color

    def render(self, content: str) -> None:
        print(f"""Rendering '{content}' with Font: {self._name},
              Size: {self._size}, Color: {self._color}""")


class FontFactory():
    _fonts: Dict = {}

    def get_font(self, name: str, size: int, color: str) -> Font:
        key = (name, size, color)
        if key not in self._fonts:
            self._fonts[key] = Font(name, size, color)
        return self._fonts[key]


font_factory = FontFactory()

font1 = font_factory.get_font('Arial', 12, 'Black')
font1.render('Hellow, World!')

font2 = font_factory.get_font('Arial', 12, 'Black')
font2.render('Flyweight Example')

font3 = font_factory.get_font('Times New Roman', 14, 'Red')
font3.render('Another Text')

print(font1 == font2)
print(font1 == font3)
print(font2 == font3)

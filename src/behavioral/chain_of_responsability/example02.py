from __future__ import annotations
from abc import ABC, abstractmethod


class ComponentWithContextHelp(ABC):
    @abstractmethod
    def showHelp(self):
        pass


class Component(ComponentWithContextHelp):
    def __init__(self, container: Container):
        self.container = container
        self.tooltipText = ""

    def showHelp(self):
        if self.tooltipText:
            return f"Help: {self.tooltipText}"
        elif self.container:
            self.container.showHelp()


class Button(Component):
    pass


class Container(Component):
    def __init__(self, container: Container):
        super().__init__(container)
        self.children = []

    def add(self, child):
        self.children.append(child)


class Panel(Container):
    def __init__(self, container: Container):
        super().__init__(container)
        self.modalHelpText = "This is a Panel."

    def showHelp(self):
        return f"Help: Visit {self.modalHelpText}"


class Dialog(Container):
    def __init__(self, container: Container):
        super().__init__(container)
        self.wikiPageUrl = "This is a Page."

    def showHelp(self):
        return f"Help: Visit {self.wikiPageUrl}"


if __name__ == "__main__":
    dialog = Dialog("Budget Reports")
    pannel = Panel("Panel")
    button1 = Button("Butao OK")
    button2 = Button("Butao Cancel")

    pannel.add(button1)
    pannel.add(button2)
    dialog.add(pannel)

    button1.tooltipText = "Click me!"
    button2.tooltipText = "Cancel"

    print(button1.showHelp())
    print(button2.showHelp())
    print(pannel.showHelp())
    print(dialog.showHelp())

    print(pannel.children)

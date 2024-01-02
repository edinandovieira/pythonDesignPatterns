from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


class Editor:
    def cut(self):
        print('Texto cortado')

    def copy(self):
        print('Texto copiado')

    def paste(self):
        print('Texto colado')


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class CutCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.cut()


class CopyCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver
        self.execution_history = []

    def execute(self):
        self.receiver.copy()


class PasteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.paste()


class Application:
    def __init__(self):
        self.command = None
        self.execution_history = []

    def set_command(self, command: Command):
        self.command = command

    def run(self):
        if self.command:
            self.command.execute()
            self.execution_history.append(self.command.__class__.__name__)

    def undo(self):
        if self.execution_history:
            last_execution = self.execution_history.pop()
            print(f'Desfazendo {last_execution}')


if __name__ == '__main__':
    editor = Editor()

    copy_command = CopyCommand(editor)
    cut_command = CutCommand(editor)
    paste_command = PasteCommand(editor)

    application = Application()

    application.set_command(copy_command)
    application.run()

    application.set_command(cut_command)
    application.run()

    application.set_command(paste_command)
    application.run()
    
    application.undo()
    application.undo()
    application.undo()
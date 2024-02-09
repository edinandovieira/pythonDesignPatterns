from abc import ABC, abstractmethod


class Expense():
    def __init__(self, expense: str, amount: float) -> None:
        self.expense = expense
        self.amount = amount


class Approver(ABC):
    def __init__(self) -> None:
        self.sucessor: Approver

    @abstractmethod
    def processRequest(self, expense: Expense) -> str:
        pass


class Manager(Approver):
    def __init__(self, sucessor: Approver) -> None:
        self.sucessor = sucessor

    def processRequest(self, expense: Expense) -> str:
        if expense.amount <= 1000:
            return f"Manager approved the expense of ${expense.amount}"
        else:
            return self.sucessor.processRequest(expense)


class Director(Approver):
    def __init__(self, sucessor: Approver) -> None:
        self.sucessor = sucessor

    def processRequest(self, expense: Expense) -> str:
        if expense.amount <= 5000:
            return f"Director approved the expense of ${expense.amount}"
        else:
            return self.sucessor.processRequest(expense)


class VicePresident(Approver):
    def __init__(self, sucessor: Approver) -> None:
        self.sucessor = sucessor

    def processRequest(self, expense: Expense) -> str:
        if expense.amount <= 10000:
            return f"Vice President approved the expense of ${expense.amount}"
        else:
            return self.sucessor.processRequest(expense)


class CEO(Approver):
    def processRequest(self, expense: Expense) -> str:
        return f"CEO approved the expense of ${expense.amount}"


class ExpenseClient():
    def __init__(self):
        self.approvalChain = Manager(Director(VicePresident(CEO())))

    def submitExpense(self, expense: Expense):
        return self.approvalChain.processRequest(expense)

if __name__ == "__main__":
    expenseCliente = ExpenseClient()
    expense1 = Expense('Folha A4', 950)
    expense2 = Expense('Folha A4', 3700)
    expense3 = Expense('Folha A4', 5500)
    expense4 = Expense('Folha A4', 17000)
    print(expenseCliente.submitExpense(expense1))
    print(expenseCliente.submitExpense(expense2))
    print(expenseCliente.submitExpense(expense3))
    print(expenseCliente.submitExpense(expense4))
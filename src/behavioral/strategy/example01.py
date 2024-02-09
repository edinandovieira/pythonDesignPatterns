from __future__ import annotations
from abc import ABC, abstractmethod

class Order():
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self._total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: int) -> None:
        self._discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self._discount)


if __name__ == '__main__':
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    custom_discount = CustomDiscount(25)
    order = Order(100, twenty_percent)
    print(order.total, order.total_with_discount)
    order2 = Order(100, fifty_percent)
    print(order2.total, order2.total_with_discount)
    order3 = Order(100, no_discount)
    print(order3.total, order3.total_with_discount)
    order4 = Order(100, custom_discount)
    print(order4.total, order4.total_with_discount)
    
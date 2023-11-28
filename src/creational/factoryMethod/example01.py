from abc import ABC, abstractmethod

# IProduct
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass
    
# Concrete Product 1
class Truck(Transport):
    def deliver(self):
        return "Entrega por caminhão"
    
# Concrete Product 2
class Ship(Transport):
    def deliver(self):
        return "Entrega por navio"
    
# Creator Interface - IFactoryMethod
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass
    
    def plan_delivery(self):
        transport = self.create_transport()
        return f"Preparando a entrega: {transport.deliver()}"
    
# Concrete Creator 1
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()
    
# Concrete Creator 1
class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()
    
if __name__ == '__main__':
    road_logistics = RoadLogistics()
    print(road_logistics.plan_delivery())
    
    sea_logistics = SeaLogistics()
    print(sea_logistics.plan_delivery())

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
    
# Concrete Product 3
class Car(Transport):
    def deliver(self):
        return "Entrega por carro"
    
# Creator Interface - IFactoryMethod
class Logistics(ABC):
    @abstractmethod
    def create_transport(self, transport_type: str) -> Transport:
        pass
    
    def plan_delivery(self, transport_type: str):
        transport = self.create_transport(transport_type)
        return f"Preparando a entrega: {transport.deliver()}"
    
# Concrete Creator 1
class RoadLogistics(Logistics):
    TRANSPORT_TYPES = {
        "truck": Truck,
        "car": Car,
    }
    
    def create_transport(self, transport_type: str) -> Transport:
        transport_class = self.TRANSPORT_TYPES.get(transport_type.lower())
        
        if transport_class:
            return transport_class()
        else: raise ValueError("Tipo de transporte inválido")
    
# Concrete Creator 1
class SeaLogistics(Logistics):
    TRANSPORT_TYPES = {
        "ship": Ship
    }
    
    def create_transport(self, transport_type: str) -> Transport:
        transport_class = self.TRANSPORT_TYPES.get(transport_type.lower())
        
        if transport_class:
            return transport_class()
        else: raise ValueError("Tipo de transporte inválido")
    
if __name__ == '__main__':
    road_logistics = RoadLogistics()
    print(road_logistics.plan_delivery('truck'))
    print(road_logistics.plan_delivery('car'))
    print(road_logistics.plan_delivery('ship'))
    
    sea_logistics = SeaLogistics()
    print(sea_logistics.plan_delivery('ship'))
    print(sea_logistics.plan_delivery('car'))

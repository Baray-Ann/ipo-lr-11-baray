from .vehicle import Vehicle
from .client import Client

class Ship(Vehicle):
    def __init__(self, vehicle_id, capacity, name):
        super().__init__(vehicle_id, capacity)
        self.name = name
    
    def __str__(self):
        return super().__str__() + f"; Название судна: {self.name}"
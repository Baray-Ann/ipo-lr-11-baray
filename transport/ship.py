from .vehicle import Vehicle
from .client import Client

class Ship(Vehicle):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    def load_cargo(self, client):
        super(Ship, self).load_cargo(client)

    def __str__(self):
        return super().__str__() + f"; Название судна: {self.name}"
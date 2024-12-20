from .vehicle import Vehicle
from .client import Client

class Van(Vehicle):
    def __init__(self, vehicle_id, capacity, is_refrigerated):
        super().__init__(vehicle_id, capacity)
        self.is_refrigerated = is_refrigerated
    
    def __str__(self): 
        return super().__str__() + f"; Наличие холодильника: {self.is_refrigerated}"
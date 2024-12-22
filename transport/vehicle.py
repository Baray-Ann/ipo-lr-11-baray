from .client import Client
import uuid

class Vehicle:

    unique_id = uuid.uuid4()

    def __init__(self, ):
        self.vehicle_id = Vehicle.unique_id
        self.capacity = 0
        self.current_load = 0
        self.clients_list = []
    
    def load_cargo(self, client):
        if not isinstance(client, Client): 
            raise ValueError("Информация о клиенте должна быть объектом класса Client.")
        if (self.current_load + client.cargo_weight) > self.capacity:
            raise ValueError("Грузоподъемность транспортного средства превышена.")
        self.current_load += client.cargo_weight
        self.clients_list.append(client)
        print(f"Загружен груз весом {client.cargo_weight} т. на транспортное средство ID {self.vehicle_id}. Текущая загрузка: {self.current_load} т")

    
    def __str__(self):
        return f"ID Транспорта: {self.vehicle_id}; Грузоподъемность: {self.capacity} т.; Текущая загрузка: {self.current_load} т."
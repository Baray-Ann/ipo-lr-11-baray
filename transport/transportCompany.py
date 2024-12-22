from .vehicle import Vehicle
from .client import Client
from .van import Van
from .ship import Ship

class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []
    
    def add_vehicle(self, vehicle):
        if not isinstance(vehicle,(Ship, Van)):
            raise ValueError("Информация о транспорте должна быть объектом класса Vehicle")
        self.vehicles.append(vehicle)
        print("Транспортное средство добавлено")
    
    def list_vehicles(self):
        vehicles_list = []
        for vehicle in self.vehicles:
            vehicles_list.append(str(vehicle))
        return vehicles_list
    
    def add_client(self, client):
        if not isinstance(client, Client):
            raise ValueError("Информация о клиенте должна быть объектом класса Client.")
        self.clients.append(client)
    
    def optimize_cargo_distribution(self):
        vip_clients = [client for client in self.clients if client.is_vip]
        ordinary_clients = [client for client in self.clients if not client.is_vip]
        sorted_clients = vip_clients + ordinary_clients

        for client in sorted_clients:
            for vehicle in self.vehicles:
                if vehicle.current_load + client.cargo_weight <= vehicle.capacity:
                    vehicle.load_cargo(client)
                    break
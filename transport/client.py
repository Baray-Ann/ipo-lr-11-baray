class Client:
    def __init__(self, name, cargo_weight, is_vip = False):
        self.name = name #Имя клиента
        self.cargo_weight = cargo_weight #Вес груза
        self.is_vip = is_vip #Статус VIP
    
    def __str__(self):
        return f"Имя клиента: {self.name}; Вес груза: {self.cargo_weight}; Статус VIP: {self.is_vip}"

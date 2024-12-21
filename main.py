from transport import Client, Vehicle, Van, Ship, TransportCompany

def main():
    name = input("Введите имя компании: ")
    company = TransportCompany(name)

    def menu():
        print('''
               Меню:
1. Вывести список клиентов
2. Добавить клиента
3. Вывести список транспортных средств
4. Добавить транспортное средство
5. Распределить груз
6. Выход из программы\n''')

    def all_clients():
        print("Список клиентов: \n")
        for client in company.clients:
            print(client)
    
    def add_client():
        name = str(input("Введите имя клиента: "))
        
        while True:
            cargo_weight = input("Введите вес груза: ")
            if cargo_weight.replace('.', '', 1) and float(cargo_weight) > 0:
                cargo_weight = float(cargo_weight)
                break
            else:
                print("Вес груза введен некорректно.")
            
        while True:
            is_vip = input("Есть ли VIP-статус?: ").lower()
            if is_vip == 'да':
                is_vip = 'True'
                break
            elif is_vip == 'нет':
                is_vip = 'False'
                break
            else:
                print("Наличие VIP-статуса введено некорректно.")

        company.add_client(Client(name, cargo_weight, is_vip))
    
    def all_vehicles():
        print("Список транспортных средств: \n")
        for vehicle in company.vehicles:
            print(vehicle)
    
    def add_vehicle():
        vehicle_type = input("Введите вид транспорта: ")

        while True:
            vehicle_id = input("Введите уникальный ID транспорта: ")
            if vehicle_id.isdigit():
                break
            else:
                print("ID транспорта введен некорректною")

        while True:
            capacity = input("Введите грузоподъёмность транспорта(в тоннах): ")
            if capacity.replace('.', '', 1) and float(capacity) > 0:
                capacity = float(capacity)
                break
            else:
                print("Грузоподъёмность транспорта введена некорректно.")
        
        if vehicle_type in ["van", "фургон", "Фургон", "Van"]:
            while True:
                is_refrigerated = input("Есть ли холодильник? ").lower()
                if is_refrigerated == 'да':
                    is_refrigerated = 'True'
                    break
                elif is_refrigerated == 'нет':
                    is_refrigerated = 'False'
                    break
                else:
                    print("Наличие холодильника введено некорректно")
            
            company.add_vehicle(Van(vehicle_id, capacity, is_refrigerated))

        elif vehicle_type in ["ship", "судно", "Ship", "Судно"]:
            name = input("Введите название судна: ")
            company.add_vehicle(Ship(vehicle_id, capacity, name))
        else:
            print("Тип транспорта введен некорректно.")

    def optimization():
        print("Распределение груза.\n")
        company.optimize_cargo_distribution()
        print("Груз распределен.")
    
    def exitProgram():
        print("Выход из программы")
        exit()

    while True:
        menu()
        operationSelect = int(input("Введите номер операции для выполнения: "))

        if operationSelect > 0 and operationSelect <= 6:
            if operationSelect == 1:
                all_clients()

            elif operationSelect == 2:
                add_client()
            
            elif operationSelect == 3:
                all_vehicles()
            
            elif operationSelect == 4:
                add_vehicle()
            
            elif operationSelect == 5:
                optimization()
            
            elif operationSelect == 6:
                exitProgram()
            
        else:
            print("Ввод операции неверен.")


if __name__ == "__main__":
    main()

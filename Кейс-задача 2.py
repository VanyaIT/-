class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        return f"The {self.make} {self.model} is starting."

    def stop(self):
        return f"The {self.make} {self.model} is stopping."

    def __str__(self):
        return f"Vehicle(make={self.make}, model={self.model})"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def start(self):
        return f"The car {self.make} {self.model} with {self.fuel_type} fuel is starting."

    def __str__(self):
        return f"Car(make={self.make}, model={self.model}, fuel_type={self.fuel_type})"

class Bicycle(Vehicle):
    def __init__(self, make, model, type_of_bike):
        super().__init__(make, model)
        self.type_of_bike = type_of_bike

    def start(self):
        return f"The bicycle {self.make} {self.model} is ready to ride."

    def __str__(self):
        return f"Bicycle(make={self.make}, model={self.model}, type_of_bike={self.type_of_bike})"

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model, fuel_type="electric")
        self.battery_capacity = battery_capacity

    def start(self):
        return f"The electric car {self.make} {self.model} with a battery capacity of {self.battery_capacity}kWh is starting silently."

    def __str__(self):
        return f"ElectricCar(make={self.make}, model={self.model}, battery_capacity={self.battery_capacity}kWh)"

if __name__ == "__main__":
    # Создаем экземпляры классов
    car = Car(make="Toyota", model="Corolla", fuel_type="gasoline")
    bicycle = Bicycle(make="Giant", model="Escape 3", type_of_bike="road")
    electric_car = ElectricCar(make="Tesla", model="Model S", battery_capacity=100)

    # Список объектов
    vehicles = [car, bicycle, electric_car]

    # Демонстрация работы методов
    for vehicle in vehicles:
        print(vehicle)
        print(vehicle.start())
        print(vehicle.stop())
        print()



# ここにコードを書いてください
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_vehicle_details(Vehicle):
    # ここにコードを書いてください
        return f"Car: {year} {make} {model}"

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def get_details(self):
        return f"Car: {self.year} {self.make} {self.model}"

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_details(self):
        return f"Truck: {self.year} {self.make} {self.model}, Towing Capacity: {self.towing_capacity}"


def display_vehicle_details(vehicle):
    print(vehicle.get_details())

if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 2021)
    truck = Truck("Ford ", "f-150", 2020, 5000)

    display_vehicle_details(car)
    display_vehicle_details(truck)

import re
from vehicle import Vehicle


class Inventory:
    def __init__(self):
        self.vehicles = []

    def retrieve_vehicles(self):
        return self.vehicles

    def add_vehicle(self, obj):
        self.vehicles.append(Vehicle(**obj))

    def apply_discount(self, func, discount):
        for vehicle in self.vehicles:
            if func(vehicle):
                vehicle.set_discount(discount)

    def search_vehicles(self, pattern):
        return [
            vehicle
            for vehicle in self.vehicles
            if re.search(pattern, vehicle.model) is not None
        ]

    def generator(self):
        for vehicle in self.vehicles:
            yield vehicle


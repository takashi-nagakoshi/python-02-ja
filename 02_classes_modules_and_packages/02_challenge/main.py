from inventory import Inventory
from data_parser import parse_vehicle_data

vehicles = parse_vehicle_data("vehicles.txt")
inventory = Inventory()
for vehicle in vehicles:
    inventory.add_vehicle(vehicle)

print(inventory.vehicles[0].get_model())  # Corolla
print(inventory.vehicles[0].get_make())  # Toyota
print(inventory.vehicles[0].get_year())  # 2020
print(inventory.vehicles[0].get_price())  # 20000
print(inventory.vehicles[0].get_discount())  # 0

inventory.apply_discount(lambda v: v.make == "Toyota", 5)
toyotas = inventory.search_vehicles("Corolla")

for toyota in toyotas:
    toyota.display()

for vehicle in inventory.retrieve_vehicles():
    vehicle.display()
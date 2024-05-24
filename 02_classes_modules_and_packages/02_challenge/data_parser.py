def parse_vehicle_data(file_name):
    with open(file_name) as fd:
        vehicles = [item.rstrip().split(",") for item in fd.readlines()]
        return [
            {
                "model": vehicle[0],
                "make": vehicle[1],
                "year": vehicle[2],
                "price": vehicle[3],
                "discount": vehicle[4] if len(vehicle) == 5 else None,
            }
            for vehicle in vehicles
        ]
# here we have made a class that formats the vehicle object into JSON format
# which was earlier a method inside Vehicle class violating single responsibility principle.
# So we have refactored the code to follow single responsibility principle.

import json
from vehicle import Vehicle

class ObjectFormator:
    def vehicle_to_json(self, vehicle: Vehicle):
        return json.dumps({
            "VehicleMake": vehicle.make,
            "VehicleModel": vehicle.model,
            "VehicleYear": vehicle.year
        })
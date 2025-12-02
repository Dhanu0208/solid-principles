from maintenance_tool import MaintenanceTool
from vehicle import Vehicle

class BreakInspectionTool(MaintenanceTool):
    def perform_maintenance(self, vehicle: Vehicle):
        print("Performing break inspection on {vehicle.make} {vehicle.model}.".format(vehicle=vehicle))
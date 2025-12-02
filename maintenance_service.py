from maintenance_tool import MaintenanceTool
from vehicle import Vehicle

class MaintenanceService:
    def __init__(self, tool: MaintenanceTool):
        self.tool = tool
        
    def service_vehicle(self, vehicle: Vehicle):
        self.tool.perform_maintenance(vehicle)
        
    



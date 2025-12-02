from abc import ABC, abstractmethod
from vehicle import Vehicle

class MaintenanceTool:
    @abstractmethod
    def perform_maintenance(self, vehicle: Vehicle):
        pass
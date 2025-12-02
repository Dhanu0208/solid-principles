# here we have the main file that uses the Vehicle, InsuranceCalculator, and ObjectFormator classes
# to demonstrate the single responsibility principle.

# here we import the necessary classes
from vehicle import Vehicle
from insurance_calculator import InsuranceCalculator
from object_formator import ObjectFormator
from car import Car
from truck import Truck
from electric_car import ElectricCar
from break_inspection_tool import BreakInspectionTool
from maintenance_service import MaintenanceService

def main():
    # here we create an instance of Vehicle, InsuranceCalculator, and ObjectFormator
    
    car = Car("Toyota", "Camry", 2018)
    truck = Truck("Ford", "F-150", 2015)
    electric_car = ElectricCar("Tesla", "Model 3", 2020)
    
    car.refuel()
    truck.refuel()
    electric_car.recharge()
    
    # electric_car.refuel()


    insurance_calculator = InsuranceCalculator()
    object_formator = ObjectFormator()
    
    
    # here we calculate insurance cost and format vehicle details to JSON
    print(f"Insurance Cost: ${insurance_calculator.calculate_insurance_cost(car)}")
    print(f"Insurance Cost: ${insurance_calculator.calculate_insurance_cost(truck)}")

    print(f"Car Details in JSON: {object_formator.vehicle_to_json(car)}")
    print(f"Truck Details in JSON: {object_formator.vehicle_to_json(truck)}")
    
    
    service = MaintenanceService(BreakInspectionTool())
    service.service_vehicle(car)
    
    
if __name__ == "__main__":
    main()


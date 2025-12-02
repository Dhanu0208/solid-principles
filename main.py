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
    print("\n------ Vehicle Management System (SRP Example) ------")
    
    
    
    # here we create an instance of Vehicle, InsuranceCalculator, and ObjectFormator
    insurance_calculator = InsuranceCalculator()
    object_formator = ObjectFormator()
    service = MaintenanceService(BreakInspectionTool())
    
    while True:
        print("\n--- Create a New Vehicle ---")
        vehicle = get_vehicle_from_user()
        
        if vehicle is None:
            print("Exiting program...")
            break
        
        while True:
            print("\nWhat do you want to do for this vehicle?")
            print("1. Calculate Insurance")
            print("2. Service Vehicle")
            print("3. Show Vehicle Details (JSON)")
            print("4. Refuel / Recharge")
            print("5. Go Back to Vehicle Selection")

            option = input("Choose option (1-5): ")

            if option == "1":
                print(f"Insurance Cost: ${insurance_calculator.calculate_insurance_cost(vehicle)}")

            elif option == "2":
                service.service_vehicle(vehicle)

            elif option == "3":
                print("Vehicle Details in JSON:")
                print(object_formator.vehicle_to_json(vehicle))

            elif option == "4":
                if isinstance(vehicle, ElectricCar):
                    vehicle.recharge()
                else:
                    vehicle.refuel()

            elif option == "5":
                print("Returning to main menu...")
                break

            else:
                print("Invalid option! Try again.")


def get_vehicle_from_user():
    print("\nSelect Vehicle Type:")
    print("1. Car")
    print("2. Truck")
    print("3. Electric Car")
    print("4. Exit Program")

    choice = input("Enter choice: ")

    if choice.lower() == "4":
        return None

    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    year = int(input("Enter manufacturing year: "))

    if choice == "1":
        return Car(brand, model, year)
    elif choice == "2":
        return Truck(brand, model, year)
    elif choice == "3":
        return ElectricCar(brand, model, year)
    else:
        print("Invalid choice! Defaulting to Car.")
        return Car(brand, model, year)
    
    
if __name__ == "__main__":
    main()


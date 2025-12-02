from vehicle import Vehicle 

# from car import Car
# from truck import Truck


# here we have a class that calculates insurance cost for a vehicle
# which was earlier a method inside Vehicle class violating single responsibility principle.
class InsuranceCalculator: 
    def calculate_insurance_cost(self, vehicle: Vehicle):
        return vehicle.calculate_insurance_cost() 



        # by doing this we are voilating open closed principle as every time we add a new vehicle type
        # we have to modify this method. 
        # car = Car("Toyota", "Camry", 2018)
        # truck = Truck("Ford", "F-150", 2015)
        # if isinstance(vehicle, car):
        #     return 1000 if age > 5 else 500
        # elif isinstance(vehicle, truck):
        #     return 1500 if age > 8 else 700
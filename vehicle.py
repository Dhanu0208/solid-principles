
from abc import ABC, abstractmethod

#here we have a Vehicle class that has been initialized with make, model and year attributes.
class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def calculate_insurance_cost(self):
        pass 
    
    # Interface segregation principle
    # here if we add refuel and recharge methods inside this class then it will violate single responsibility principle.
    # So we will create separate interfaces for each responsibility.
    # def refuel(self):
    #     pass
    # def recharge(self):
    #     pass



# here as you see we have added all the methods inside this one class which is 
# violating single responsibility principle. 

# So we will refactor the code to follow single responsibility principle 
# by creating separate classes for each responsibility.

# import json
# class Vehicle:
#     def _init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
        
#     def calculate_insurance_cost(self):
#         age = 2024 - self.year  
#         if age > 5:
#             return 1000
#         return 500
    
#     def to_json(self):
#         return json.dumps({
#             "VehicleMake": self.make,
#             "VehicleModel": self.model,
#             "VehicleYear": self.year
#         }) 
        
# def main():
#     vehicle = Vehicle ("Toyota", "Camry", 2018)
#     print(f"Insurance Cost: ${vehicle.calculate_insurance_cost()}")
#     print(f"Vehicle Details in JSON: {vehicle.to_json()}")
    
# if __name__ == "__main__":
#     main()

        
        
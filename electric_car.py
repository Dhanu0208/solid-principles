from vehicle import Vehicle
from rechargeable import Rechargeable

# here we have a ElectricCar class that inherits from Vehicle
class ElectricCar(Vehicle, Rechargeable):
    def calculate_insurance_cost(self):
        age = 2024 - self.year
        return 2000 if age > 5 else 1000
    
    def recharge(self):
        print("Recharging the electric car's battery.")


    # if we are importing the Rechargeable interface then we dont have to implement this method here.
    # def refuel(self):
    #     raise NotImplementedError("Electric cars do not support refueling.")
from vehicle import Vehicle
from fuleable import Fuleable

# here we have a Truck class that inherits from Vehicle
class Truck(Vehicle, Fuleable):
    def calculate_insurance_cost(self):
        age = 2024 - self.year
        return 1500 if age > 8 else 700
    
    def refuel(self):
        print("Refueling the truck with diesel.")


    # if we are importing the Rechargeable interface then we dont have to implement this method here.
    # def recharge(self):
    #     raise NotImplementedError("Trucks do not support recharging.")
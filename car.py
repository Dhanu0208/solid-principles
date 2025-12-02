from vehicle import Vehicle
from fuleable import Fuleable

# here we have a Car class that inherits from Vehicle
class Car(Vehicle, Fuleable):
    def calculate_insurance_cost(self):
        age = 2024 - self.year
        return 1000 if age > 5 else 500
    
    def refuel(self):
        print("Refueling the car with petrol.")       

    # if we are importing the Rechargeable interface then we dont have to implement this method here.
    # def recharge(self):
    #     raise NotImplementedError("Cars do not support recharging.")
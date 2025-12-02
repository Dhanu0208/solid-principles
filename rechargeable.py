from abc import ABC, abstractmethod

# here we have created a separate interface for refuel method to follow ISP 
# we can create separate interfaces for each responsibility like Fuleable interface for refuel method
# and Rechargeable interface for recharge method
class Rechargeable(ABC):
    @abstractmethod
    def recharge(self):
        pass
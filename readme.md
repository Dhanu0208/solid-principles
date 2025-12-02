Single Responsibility Principle (SRP)
The Single Responsibility Principle states that a class should have only one reason to change,
meaning it should have only one job or responsibility.

what would be consequences if we dont follow up single responsibility principle?
    1. finding where to make changes would be difficult,
        in our early example if we wanted to change the insurance calculation logic,
        we would have to search where the function is defined in a large repository,
        or we would have to modify the Vehicle class, which could inadvertently affect other parts of the code
        this would lead to increased chances of bugs and errors,
        making the codebase harder to maintain and understand over time.
    
    2. we have to write repeated code,
        in our early example, we had the printing logic inside the Vehicle class,
        if we had multiple classes that needed to format objects to JSON,
        and if the formatting logic was inside the Vehicle class,
        we would have to duplicate that logic in each class
    
things to remember while following single responsibility principle:
    1. Add methods according to the class name.
        for example, if we have a class named Vehicle,
        we should only add methods that are directly related to the vehicle's properties and behaviors,

    2. thing yourself that will this method would be used by other classes?
        if yes, then make sure to make a separate class for that functionality.




Open-Closed Principle (OCP)
The Open-Closed Principle states that software entities (classes, modules, functions, etc.)
should be open for extension but closed for modification.
This means that you should be able to add new functionality to a class without changing its existing code.

what would be consequences if we dont follow up open-closed principle?
    1. if we have to add new features or functionalities,
    we would have to modify the existing code,
    for example, in our insurance calculator example,
    if we wanted to add a new vehicle type like Motorcycle,
    we would have to modify the calculate_insurance_cost method by adding extra conditions for Motorcycle,
    
    2. Modifying existing code increases the risk of introducing bugs.
    
things to remember while following open-closed principle:
    1. we should avoid using conditional statements for example here we are checking for instance of vehicle type
    inside the calculate_insurance_cost method, so we have to make a base class Vehicle and multiple derived classes like Car, Truck, Motorcycle etc.
    each derived class should implement its own version of calculate_insurance_cost method.





Liskov Substitution Principle (LSP)
The Liskov Substitution Principle states that objects of a superclass should be replaceable
with objects of a subclass without affecting the correctness of the program.

what would be consequences if we dont follow up liskov substitution principle?
    1. if we dont follow LSP and create subclasses for example, electric vehicles that do not implement certain methods from the base class,
    it can lead to runtime errors when those methods are called on instances of the subclass,

things to remember while following liskov substitution principle:
    whenever you create a new class make sure to implement all methods from the base class
    where you are creating a subclass make sure to check its consistency with the base class especially the return value





Interface Segregation Principle (ISP)
Instead of creating one large, all-purpose interface, break it into smaller, more specific interfaces so that 
each class only has methods relevant to it. A class should only have to implement methods it actually uses.

    for example, if we have a Vehicle class, and it had multiple methods like refuel, recharge etc. 
    but not all vehicles need to implement all these methods, but its necessaary to implement all methods from the Vehicle class.
    so to follow ISP we can create separate interfaces for each responsibility like Fuleable interface for refuel method
    and Rechargeable interface for recharge method.

what would be consequences if we dont follow up interface segregation principle?
    1. Classes may be forced to implement methods they don't need, leading to irrelevant code or Not ImplementedError placeholders. 
    This then leads to unexpected runtime errors.

    2. Adding new features or modifying functionality becomes harder, 
    as you have to change large interfaces and all classes that implement them, increasing the risk of introducing bugs.
        for example, if we want to add a new method to the Vehicle class, load_cargo,
        all vehicle types would have to implement this method, even if it doesn't make sense for some of them,
        like cars or motorcycles, leading to unnecessary code and potential errors.  
    
things to remember while following interface segregation principle:
    1. create separate interfaces for each responsibility.
        if we see the situation where a class is forced to implement NotImplementedError methods it doesn't need,
        we should refactor the code to create separate interfaces for each responsibility.
    2. make sure to implement only those interfaces which are necessary for that class.




Dependency Inversion Principle (DIP)
The Dependency Inversion Principle states that high-level modules should not depend on low-level modules.
all classes should depend on abstractions (e.g., interfaces or abstract classes) rather than concrete implementations.

    for example if we wan to implement the break inspection tool for vehicles,
    so we will make another class maintenance service that will have a method of break inspection

    but here the MaintenanceService class is directly dependent on the BreakInspectionTool class,
    and if we want to change the break inspection tool implementation to another tool lets say tire inspection tool,
    we would have to modify the MaintenanceService class, which violates the DIP and OCP principles.

    so we will create an abstraction which is maintenance_tool -> perform_maintenance method
    and break_inspection tool will use the method of maintenance_service 


what would be consequences if we dont follow up dependency inversion principle?
    1. We will break Open Closed Principle i.e. we will need to modify existing classes methods. 
    There is a high chance you might introduce bugs when modifying existing classes.

things to remember while following dependency inversion principle:
    1 Always have abstract classes/interfaces as dependencies. Try not to have dependencies on concrete classes.
    2. Always try to pass dependencies into classes when initializing


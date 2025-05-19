# Define the parent class Vehicle
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def display_details(self):
        # Display the vehicle's details
        print("Vehicle Details:")
        print(f"Vehicle Name: {self.name}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Mileage: {self.mileage} km/l")
# Define the child class Bus that inherits from Vehicla
class Bus(Vehicle):
    pass # Inherits all properties and methods from Vehicle
# Take input from the user
name = input("Enter the name of the Bus: ")
max_speed = input("Enter the maximum speed of the vehicle (in km/h): ")
mileage = input("Enter the mileage of the vehicle (in km/l): ")
# Create an instance of the Bus using user inpur
school_bus =  Bus(name, max_speed, mileage)
# Call the methods to display bus details
school_bus.display_details()

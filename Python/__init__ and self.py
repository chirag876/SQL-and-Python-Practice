class Aviation:
    def __init__(self, fuelcapacity, aircraftype):
        self.fuelcapacity = fuelcapacity
        self.aircraftype = aircraftype


# create an instance of the Aviation class
# This is an example of how to use the __init__ method to initialize attributes of a class.
Airplane = Aviation(1000, "Boeing 747")
print("Airplane Details:")
print(
    f"Fuel Capacity: {Airplane.fuelcapacity}, Aircraft Type: {Airplane.aircraftype}")

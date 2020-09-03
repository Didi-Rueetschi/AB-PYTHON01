# Definition of the class vehicle
class vehicle:
    def __init__(self, bez, ge):
        self.description = bez
        self.speed = ge

    def acceleration(self, value):
        self.speed += value

    def __str__(self):
        return self.description + " " \
               + str(self.speed) + " km/h"


# Definition of the class passenger_vehicles
class passenger(vehicle):
    def __init__(self, bez, ge, ins):
        vehicle.__init__(self, bez, ge)
        self.passengers = ins

    def __str__(self):
        return vehicle.__str__(self) + " " \
               + str(self.passengers) + " Passengers"

    def get_on(self, quantity):
        self.passengers += quantity

    def get_off(self, quantity):
        self.passengers -= quantity


# Create objects for the inheritance class passenger_vehicles
fiat = passenger("Fiat Marea", 50, 0)

# Employ specific method
fiat.get_on(3)
fiat.get_off(1)

# Apply inherited method
fiat.acceleration(10)

# Apply over-written method
print(fiat)

# Execute destructor
del fiat

# Called function not allowed
fiat.output()

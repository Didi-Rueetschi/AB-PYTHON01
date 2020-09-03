# Definition of the class vehicle
class vehicle:
    speed = 0               # attribute
    def acceleration(self, value):    # method
        self.speed += value
    def output(self):                # method
        print("speed:", self.speed)

# Create objects for the class vehicle
opel = vehicle()
volvo = vehicle()

# Object methods
volvo.output()
volvo.acceleration(20)
volvo.output()

# Object output
opel.output()



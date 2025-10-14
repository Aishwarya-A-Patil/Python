class Vehicle:
    def __init__(self, millage, cost):
        self.millage = millage
        self.cost = cost

    def showVehicleDetails(self):
        print("Millage: ", self.millage)
        print("Cost: ", self.cost)
        print("I am Vehicle")

class Car(Vehicle):
    def showCarDetails(self):
        print("I am Car")

#vehicle = Vehicle(30, 20000)
#vehicle.showVehicleDetails()

#init/ constructor is defined in Parent class / Vehicle class so we can pass parameters in child class initilization
car = Car(50, 50000)
#car.showCarDetails()
car.showVehicleDetails()  # inherited from Vehicle class
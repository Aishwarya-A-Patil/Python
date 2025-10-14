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


#Example 2
class Math1:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.addResult = self.n1 + self.n2
        
class Math2(Math1):
    def showResult(self):
        print("Addition Result: ", self.addResult)


m2 = Math2(1, 3)
m2.showResult()
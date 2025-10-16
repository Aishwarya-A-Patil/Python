class Test1:
    def __init__(self, milage, cost):
        self.m = milage
        self.c = cost

    def showVehicleDetails(self):
        print("\n Milage: ", self.m, "\n Cost: ", self.c)
        print("I am a vehicle")

#method overriding --> Used to acess methods of parent class in child without initialization
class Test2(Test1):
    def __init__(self, milage, cost, tyre, hp):
        super().__init__(milage, cost) #refers to constructor of parent class
        #super(). ---> used to call method in parent class
        self.tyre = tyre
        self.hp = hp

    def carDetails(self):
        print("No. of tyres: ", self.tyre, "\n HorsePower: ", self.hp)
        print("I am a car")
        
t2 = Test2(50, 200000, 4, 100)
t2.showVehicleDetails()
t2.carDetails()
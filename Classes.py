
#class
class Phone:                                        # class defination
    def makeCall(self):
        print("Making Call")                        #method/ function/ object

    def playingGame(self):
        print("Playing Games.")


p1 = Phone();                                      # class initialization
p1.makeCall()
p1.playingGame()


#Attributes
class Phone1 :
    def set_color(self,color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        print("The color is ", self.color)
        print("The cost is ", self.cost)

    def show_cost(self):
        print("The color is : ", self.color)
        print("The cost is : ", self.cost)


p2 = Phone1()
p2.set_color("Black")
p2.set_cost(10000)
p2.show_color()
p2.show_cost()


class Operation:
    def firstValue(self, value1):
        self.val1 = value1
       #print("val3 = ",val3) -----> This will throw error as val3 is not accessible

    def secondValue(self, value2, value3):
        self.val2 = value2
        val3  = 123
       #print(val3)
        

    def additionOP(self):
        addResult = self.val1 + self.val2 
        #only self.something is accessible all over the class
        #the valiable addResult is only available accessible inside additionOP
        print("The result of addition operation is: ", addResult)


p3 = Operation()
p3.firstValue(1)
p3.secondValue(2,3)
p3.additionOP()




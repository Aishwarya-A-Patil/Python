#Multiple Level inheritance
class Parent1:
    def p1(self, v1):
        self.v1= v1
        print("this is p1 method of Parent1: v1= ", self.v1)

class Child1(Parent1):
    def c1(self):
        self.v1 = 5
        print("this is c1 method of Child1, v1= ", self.v1)

class Child2(Child1):
    def c2(self):
        self.v1 = 6
        print("this is c2 method of Child2, v1= ", self.v1)
        #super().p1(0) ----> accessed method of Parent1 ---> method overriding

temp1 = Child2()
temp1.c2()
temp1.c1()
temp1.p1(0)
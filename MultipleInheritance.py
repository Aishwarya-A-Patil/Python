#Multiple Inheritance
#Example 1
class Parent1:
    def method1(self, var1):
        self.v1 = var1

    def showMethod1(self):
        self.v1 = 4
        print("This is method1 V1: ", self.v1)

class Parent2:
    def method2(self, var2):
        self.v2 = var2

    def showMethod2(self):
        self.v2 = 5
        print("This is method1 V1: ", self.v2)

class Derived(Parent1, Parent2):
    def method3(self):
        print("This is derived class")

temp = Derived()
temp.showMethod1()
temp.showMethod2()
temp.method3()
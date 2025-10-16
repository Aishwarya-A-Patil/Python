class P1:
    def method1(self, x1):
        print("method1 -->\t x1 =", x1, "\t type: ", type(x1))

class P2:
    def method2(self, x1):
        print("method2 -->\t x1 =", x1, "\t type: ", type(x1))

class P3:
    def method3(self, x1):
        print("method3 -->\t x1 =", x1, "\t type: ", type(x1))

class P4(P1, P2, P3):
    def method4(self):
        pass

p4 = P4()
p4.method1(5)
p4.method2("ABC")
p4.method3(10.0)
p4.method4()
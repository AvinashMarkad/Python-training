class Grandfather:
    def show1(self):
        print("Grandfather class")

class Father(Grandfather):
    def show2(self):
        print("Father class")

class Child(Father):
    def show3(self):
        print("Child class")

c = Child()
c.show1()
c.show2()
c.show3()
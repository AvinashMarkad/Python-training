class A:
    def a(self):
        print('A')

class B(A):
    def b(self):
        print('B')

class C:
    def c(self):
        print('C')

class D(B, C):
    def d(self):
        print('D')

d = D()
d.a()
d.b()
d.c()
d.d()
class A :
    def do(self):
        print(A)

class B (A) :
    def do(self):
        print("B")
        super().do()

class C(A) :
    def do(self):
        print("C")
        super().do()

class D(B,C) :
    def do(self):
        print("D")
        super().do()
print(D.mro())
class A:
    def __init__(self):
        self.calc(10)
    def calc(self, i):
        self.i = 3 * i
 
 
class B(A):
    def __init__(self):
        super().__init__()
        print('i from B is', self.i)
 
    def calc(self, i):
        self.i = 2 * i
 
 
b = B()


##############

def o(p):
    def q():
        return '*' * p
    return q
 
 
r = o(1)
s = o(2)
print(r() + s())


#################

def foo(x, y):
    return y(x) + (x + 1)
 
print(foo(1, lambda x: x * x))
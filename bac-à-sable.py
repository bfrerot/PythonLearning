class Demo:
    def __init__(self, value):
        self.instance_var = value
d1 = Demo(100)
print('contents of d1:', d1.__dict__)
d2 = Demo(200)
d1.another_var = 'another variable in the object'
print('contents of d1:', d1.__dict__)
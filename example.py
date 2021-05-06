import mo_module2 as mm2

class Example(mm2.Gradient):
    x0 = [0,0]

    @staticmethod
    def f(x1,x2):
        pass
    print(type(f))

    @staticmethod
    def f_der(x1,x2):
        pass

Example.solve()
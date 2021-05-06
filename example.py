import mo_module2 as mm2
from numpy import sqrt, array

class Example(mm2.Gradient):
    x0 = [-2,-2]
    e = 0.000001
    @staticmethod
    def f(x1,x2):
        return sqrt(x1**2+x2**2+1)+0.5*x1-0.5*x2

    @staticmethod
    def f_der(x1,x2):
        return array([
            x1/sqrt((x1**2+x2**2+1)) + 0.5,
            x2/sqrt((x1**2+x2**2+1)) - 0.5
        ])

res = Example.solve()
print(res)
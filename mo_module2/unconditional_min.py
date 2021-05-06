from inspect import signature

class Base:
    n = 0
    def __init__(self):
        pass

    def _prelength(foo):
        def dummie(self, *args, **kwargs):
            sig = signature(self.f)
            params = sig.parameters 
            self.n = len(params)
            foo(self, *args, **kwargs)
        return dummie

    @classmethod
    @_prelength
    def solve(self,):
        print(self.n)

class Gradient(Base):
    pass

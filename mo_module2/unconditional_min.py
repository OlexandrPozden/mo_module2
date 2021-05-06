from inspect import signature
from numpy.linalg import norm
from numpy import array, inf

class Base:
    n = 0
    e = 0.0001
    x0 = [0,0]
    
    def __init__(self):
        pass

    def f(self):
        pass

    def f_der(self):
        pass

    def _get_length_params(self):
        sig = signature(self.f)
        params = sig.parameters 
        return len(params)

    def _prelength(foo):
        def dummie(self, *args, **kwargs):
            self.n = self._get_length_params(self)
            return foo(self, *args, **kwargs)
        return dummie

class Gradient(Base):
    
    @classmethod
    @Base._prelength
    def solve(self, m=100):

        # consts
        x = self.x0
        f = self.f
        f_der = self.f_der
        e = self.e

        dfx = f_der(*x)
        if norm(dfx)<e:
            return x
        
        alpha = 1
        
        x = array(x)
        x_ = x - alpha*dfx ## dfx = f'(x) = f'(xk) = f'(x0)
        
        while norm(f_der(*x_))>norm(dfx):
            alpha/=2
            x_ = x - alpha*dfx
            
        i = 0
        while  norm(dfx)>e and i<m:
            x = x_
            dfx = f_der(*x)
            
            x_ = x - alpha*dfx
            
            while norm(f_der(*x_))>norm(dfx):
                alpha/=2
                x_ = x - alpha*dfx
                
            i += 1

        print("iterations: ",i)
        print(x_)
        return x_

    

from inspect import signature
from numpy.linalg import norm, solve
from numpy import array, inf, eye, transpose

class _Base:
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

class Gradient(_Base):
    
    @classmethod
    @_Base._prelength
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

class NewtonRizn(_Base):

    def solve(self, limit = 100):

        f_der = self.f_der
        f = self.f
        h = self.h
        n = self.n
        ebasis = eye(n)
        x_prev = self.x0
        
        i = 0
        while "not found":
            a = 1
            A = []
            for eb in ebasis:
                A.append((f_der(*(x_prev+eb*h))-f_der(*x_prev))/h)
            
            A = array(A)
            transpose(A)
            
            s = solve(A,f_der(*x_prev))
            x = x_prev - s
            
            while f(*x)>f(*x_prev):
                a = a/2
                x = x_prev - a*s
                
            i+=1
            if norm(x-x_prev)<e or norm(f_der(*x))<e or i>limit:
                print("iteration: %i"%(i))
                break
            else:
                x_prev = x
        return 

    

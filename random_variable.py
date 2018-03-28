# created my Massimo Di Pierro @ 2018
# license: BSDv3
from __future__ import print_function
import math

class RandomVariable(object):
    def __init__(self, S, p=None, func=None):
        self.S = S
        self.p = p or (lambda x, S=S: 1.0/len(S))
        self.func = func or (lambda x: x)
    def __call__(self, x):
        return self.func(x)
    def apply(self, g):
        func = lambda x, s=self, g=g: g(s.func(x))
        return RandomVariable(self.S, self.p, func)
    def __neg__(self):
        return self.apply(lambda x: -x)
    def __add__(self, z):
        if isinstance(z, RandomVariable):
            if not z.S == self.S:
                raise NotImplementedError
            func = lambda x, s=self, o=z: s.func(x)+o.func(x)
            return RandomVariable(self.S, self.p, func)
        return self.apply(lambda x, z=z: x+z)
    def __sub__(self, z):        
        if isinstance(z, RandomVariable):
            if not z.S == self.S:
                raise NotImplementedError
            func = lambda x, s=self, o=z: s.func(x)-o.func(x)
            return RandomVariable(self.S, self.p, func)
        return self.apply(lambda x, z=z: x-z)
    def __rsub__(self, z):        
        return -self.__sub__(z)
    def __mul__(self, z):        
        if isinstance(z, RandomVariable):
            if not z.S == self.S:
                raise NotImplementedError
            func = lambda x, s=self, o=z: s.func(x)*o.func(x)
            return RandomVariable(self.S, self.p, func)
        return self.apply(lambda x, z=z: x*z)            
    def __rmul__(self, z):        
        return self.__mul__(z)
    def __div__(self, z):        
        if isinstance(z, RandomVariable):
            if not z.S == self.S:
                raise NotImplementedError
            func = lambda x, s=self, o=z: s.func(x)/o.func(x)
            return RandomVariable(self.S, self.p, func)
        return self.apply(lambda x, z=z: x/z)
    def __rdiv__(self, z):
        return self.apply(lambda x, z=z: z/x)
    def __pow__(self, z):
        return self.apply(lambda x, z=z: x**z)

def pow(self, z): return self.apply(lambda x, z=z: x**z)
def sin(self): return self.apply(lambda x: math.sin(x))
def cos(self): return self.apply(lambda x: math.cos(x))
def tan(self): return self.apply(lambda x: math.tan(x))

class Eo(object):
    def __getitem__(self, f):
        return sum(f(x)*f.p(x) for x in f.S)
E = Eo()

#### example of usage
def examples():
    dice = [1, 2, 3, 4, 5, 6]
    X = RandomVariable(dice)
    print('mean:', E[X])
    print('1-mean:', E[1-X])
    print('twice the mean:', E[X*2])
    print('variance:', E[(X-E[X])**2])
    print('variance again:', E[X**2]-E[X]**2)
    print('standard deviation:', (E[X**2]-E[X]**2)**0.5)
    print('skewness:', E[(X-E[X])**3]/E[(X-E[X])**2]**1.5)
    print('kurtosis:', E[(X-E[X])**4]/E[(X-E[X])**2]**2)
    print('some other complex expectation value:', E[sin(2*X)*cos(X+1)])

if __name__ == '__main__':
    examples()

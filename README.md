## What?

Implements the standard math syntax for expectation values of random variables on finite sets

## How?

This is best explained with an example:

```
# import the objects
from random_variable import RandomVariable, E
         
# define a universe for example the possible outcomes of a dice
dice = [1, 2, 3, 4, 5, 6]

# define one random variable
X = RandomVariable(dice)

# compute and print expectation values
print('mean:', E[X])
print('one minus mean:', E[1-X])
print('twice the mean:', E[X*2])
print('variance:', E[(X-E[X])**2])
print('variance again:', E[X**2]-E[X]**2)
print('standard deviation:', (E[X**2]-E[X]**2)**0.5)
print('skewness:', E[(X-E[X])**3]/E[(X-E[X])**2]**1.5)
print('kurtosis:', E[(X-E[X])**4]/E[(X-E[X])**2]**2)
print('some other complex expectation value:', E[sin(2*X)*cos(X+1)])
```

(works in both python 2 and python 3)

## License

BSD v3 - Created by Prof. Massimo Di Pierro (DePaul Universty) 2018


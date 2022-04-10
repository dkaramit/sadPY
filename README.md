# sadPY
Simple Automatic Differentiation in Python

![](https://img.shields.io/badge/language-Python-black.svg)  ![](https://tokei.rs/b1/github/dkaramit/sadPY)

![](https://img.shields.io/github/repo-size/dkaramit/sadPY?color=blue)

It works as expected for the moment. I only have implemented basic operators, but I expect to continue working on this. 

## Usage:
just import the module, define variables, and take derivatives of expressions.

### Example:
```
from SAD import Variable,derivative,evaluate 
   
x=Variable(2,'x')
y=Variable(1,'y')

z=1/(x*2) * y + 1
print(*z.showExpr())
print(z)
print(derivative(z,x))
print(derivative(z,x,y))
print(derivative(z,x,x,x))
```

The good thing about it is that it will be able to output code for [sadET](https://github.com/dkaramit/sadET) (using the ```showExpr``` method of an ```Expression```)!
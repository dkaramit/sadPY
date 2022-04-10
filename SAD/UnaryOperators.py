from .Expression import Expression

def __Neg__(x):
    if isinstance(x,Expression): 
        return Expression('sadET::Negation< {} >'.format(x.exprType),'- {}'.format(x.expr))

    if not isinstance(x,Expression): 
        return Expression('numericType'.format(x.exprType),'- {}'.format(x))

class Negation(Expression):
    def __init__(self,LH,exprType,expr):
        super(Negation, self).__init__(exprType,expr)
        self.LH=LH

    def evaluate(self):
        return -evaluate(self.LH) 
    
    def derivative(self,wrt):
        return -derivative(self.LH,wrt)

from .BinaryOperators import Multiplication
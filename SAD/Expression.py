def evaluate(Expr):
    if isinstance(Expr,Expression):
        return  Expr.evaluate()
    else:
        return Expr
                
def derivative(Expr,*wrt):
    if len(wrt)==1:
        if isinstance(Expr,Expression):
            if wrt[0] is Expr:
                return Constant(1)
            return  Expr.derivative(wrt[0])
        else:
            return 0
    else:
        return derivative(Expr.derivative(wrt[0]),*wrt[1:])

class Expression:
    def __init__(self,exprType,expr):
        self.exprType=exprType
        self.expr=expr

    def evaluate():
        self.evaluate()
    def __str__(self):
        return str(self.evaluate())
    def showExpr(self):
        return self.exprType,self.expr

    def __neg__(self):
        ex=__Neg__(self)
        return Negation(self,ex.exprType,ex.expr)
    def __add__(self,other):
        ex=__Add__(self,other)
        return Addition(self,other,ex.exprType,ex.expr)
    def __radd__(self,other):
        return self.__add__(other)
    def __sub__(self,other):
        ex=__Sub__(self,other)
        return Subtraction(self,other,ex.exprType,ex.expr)
    def __rsub__(self,other):
        return -1*self.__sub__(other)
    def __mul__(self,other):
        ex=__Mul__(self,other)
        return Multiplication(self,other,ex.exprType,ex.expr)
    def __rmul__(self,other):
        return self.__mul__(other)
    def __truediv__(self,other):
        ex=__Div__(self,other)
        return Division(self,other,ex.exprType,ex.expr)
    def __rtruediv__(self,other):
        ex=__Div__(other,self)
        return Division(other,self,ex.exprType,ex.expr)


class Constant(Expression):
    def __init__(self,value):
        super(Constant, self).__init__('sadET::Constant<numericType>',str(value))
        self.value=value

    def evaluate(self):
        return self.value
    
    def derivative(self,wrt):
        return Constant(0)    


class Variable(Expression):
    def __init__(self,value,wrt):
        super(Variable, self).__init__('sadET::Variable<numericType>',wrt)
        self.value=value
        self.id=id

    def evaluate(self):
        return self.value
    
    def derivative(self,wrt):
        if wrt is self:
            return Constant(1)
        else:
            return Constant(0)
            


from .BinaryOperators import Addition,Multiplication,Subtraction,Division
from .BinaryOperators import __Add__,__Mul__,__Div__,__Sub__
from .UnaryOperators import Negation
from .UnaryOperators import __Neg__
from .Expression import Expression,evaluate,derivative

def __Add__(x,y):
    if isinstance(x,Expression) and isinstance(y,Expression): 
        return Expression('sadET::Addition< {} , {} >'.format(x.exprType,y.exprType),'({} + {})'.format(x.expr,y.expr))
    if isinstance(x,Expression) and not isinstance(y,Expression): 
        return Expression('sadET::Addition< {} , {} >'.format(x.exprType,'numericType'),'({} + {})'.format(x.expr,y))

def __Sub__(x,y):
    if isinstance(x,Expression) and isinstance(y,Expression): 
        return Expression('sadET::Subtraction< {} , {} >'.format(x.exprType,y.exprType),'({} - {})'.format(x.expr,y.expr))
    if isinstance(x,Expression) and not isinstance(y,Expression): 
        return Expression('sadET::Subtraction< {} , {} >'.format(x.exprType,'numericType'),'({} - {})'.format(x.expr,y))
    
def __Mul__(x,y):
    if isinstance(x,Expression) and isinstance(y,Expression): 
        return Expression('sadET::Multiplication< {} , {} >'.format(x.exprType,y.exprType),'({} * {})'.format(x.expr,y.expr))
    if isinstance(x,Expression) and not isinstance(y,Expression): 
        return Expression('sadET::Multiplication< {} , {} >'.format(x.exprType,'numericType'),'({} * {})'.format(x.expr,y))

def __Div__(x,y):
    if isinstance(x,Expression) and isinstance(y,Expression): 
        return Expression('sadET::Division< {} , {} >'.format(x.exprType,y.exprType),'({} / {})'.format(x.expr,y.expr))
    if isinstance(x,Expression) and not isinstance(y,Expression): 
        return Expression('sadET::Division< {} , {} >'.format(x.exprType,'numericType'),'({} / {})'.format(x.expr,y))
    if not isinstance(x,Expression) and isinstance(y,Expression): 
        return Expression('sadET::Division< {} , {} >'.format('numericType',y.exprType),'({} / {})'.format(x,y.expr))



class Addition(Expression):
    def __init__(self,LH,RH,exprType,expr):
        super(Addition, self).__init__(exprType,expr)
        self.LH=LH
        self.RH=RH

    def evaluate(self):
        return evaluate(self.LH) + evaluate(self.RH) 
    
    def derivative(self,wrt):
        return derivative(self.LH,wrt) + derivative(self.RH,wrt)

class Multiplication(Expression):
    def __init__(self,LH,RH,exprType,expr):
        super(Multiplication, self).__init__(exprType,expr)
        self.LH=LH
        self.RH=RH

    def evaluate(self):
        return evaluate(self.LH) * evaluate(self.RH) 
    
    def derivative(self,wrt):
        return derivative(self.LH,wrt) * self.RH + self.LH * derivative(self.RH,wrt)

class Division(Expression):
    def __init__(self,LH,RH,exprType,expr):
        super(Division, self).__init__(exprType,expr)
        self.LH=LH
        self.RH=RH

    def evaluate(self):
        return evaluate(self.LH) / evaluate(self.RH) 
    
    def derivative(self,wrt):
        return derivative(self.LH,wrt) / self.RH - self.LH*derivative(self.RH,wrt)/(self.RH*self.RH)

class Subtraction(Expression):
    def __init__(self,LH,RH,exprType,expr):
        super(Subtraction, self).__init__(exprType,expr)
        self.LH=LH
        self.RH=RH

    def evaluate(self):
        return evaluate(self.LH) - evaluate(self.RH) 
    
    def derivative(self,wrt):
        return derivative(self.LH,wrt) - derivative(self.RH,wrt)
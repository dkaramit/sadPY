from SAD import Variable,derivative,evaluate 

def main():
    x=Variable(2,'x')
    y=Variable(1,'y')

    z=1/(x*2) * y + 1
    print(*z.showExpr())
    print(z)
    print(derivative(z,x))
    print(derivative(z,x,y))
    print(derivative(z,x,x,x))


if __name__=='__main__':
    main()

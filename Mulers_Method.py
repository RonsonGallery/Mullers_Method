import math

epsilon = 0.0001
MAX = 100

def function(x):
    return (1 * pow(x,3) - pow(x,2) - x - 1 )

#def p(x,a,b,c):
#   return (c +b(x+))

def Muller(x0 ,x1, x2):
    def p(x):
        return (c + (b * (x-x2)) + (a * pow(x-x2,2)))
    d1 = function(x0) - function(x2)
    d2 = function(x1) - function(x2)
    h1 = x0 - x2
    h2 = x1 - x2
    c = function(x0)
    b = (d2*pow(h1,2)-d1*pow(h2,2)/h1*h2 *(h1 -h2))
    a = ((d1*h2 - d2*h1) / (h1*h2 * (h1 - h2)))
    denom = max(b + math.sqrt(b**2 -4*a*c),b - math.sqrt(b**2 -4*a*c))
    x3 = (-2 * c / denom) + x2
    #z = -2 * c / (b + abs(math.sqrt(b**2 - 4 * a* c))) + x2
    #y = -2 * c / (b - abs(math.sqrt(b**2 - 4 * a * c))) + x2
    #myList = [z,y]
    #x3 = min(myList , key = lambda x:abs(x-x2))
    if x3 - x2 < epsilon:
        return x3
    else:
        return Muller(x1,x2,x3)

print("The root of the function is")
print(Muller(0,1,2))
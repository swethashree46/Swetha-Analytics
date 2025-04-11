#USER DEFINED FUNCTION MODULE 2
#COMPLEX FUNCTIONS

#FIBONACCI SERIES
def fib(n):
    a,b = 0,1
    series = []
    for x in range(n):
        series.append(a)
        a,b = b,a+b
    return series


#MULTIPLES OF 11
def multiples(n):
    a,b = 11,22
    product = []
    for x in range(n):
        product.append(a)
        a,b = b, b+11
    return product


#ODD NUMBER OR EVEN NUMBER
def odd(n):
    num=n%2
    if(num==0):
        print("Even number")
    else:
        print("Odd number")
    return num


#(a+b)^2
def plus(a,b):
    form=(a*a)+(b*b)+2*a*b
    return form

#(a-b)^2
def minus(a,b):
    sol=(a*a)+(b*b)-2*a*b
    return sol

def tables(number,times):
    result = []
    for i in range(1, times + 1):
        result.append(number * i)
    return result


def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

x=0
while x>=0 and x<=15:
    result=x*x+x+17
    if(IsPrime(result)):
        print("x=",x,"res=",result,"- Число простое")
    else:
        print("x=", x, "res=", result, "- Число не простое")
    x += 1





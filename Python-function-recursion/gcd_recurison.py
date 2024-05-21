#begin
def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        return gcd(b,a%b)
#end

a,b=map(int,input('enter the 2 number:-').split())
result=gcd(a,b)
print(f'GCD of {a} and {b} is :- ',result)    
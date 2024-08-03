#check whether a give number is prime or not
#prime number can not be negative
#begin
def check_prime(n):
    flag=False
    if n==1:
        return "1 is not a prime number"
    elif n < 0:
        return "Negative number can to be prime number"
    elif n >1 :
        for i in range(2,n):
            if n % i == 0:
               flag=True
               break   
        if flag :
            return "Not a prime number"
        else:
             return "Prime number"
    
#end

num=int(input("Enter a number "))
print(check_prime(num))
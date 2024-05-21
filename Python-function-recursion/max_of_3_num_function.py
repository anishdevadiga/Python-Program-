#max of 3 numbers using function

#begin
def fun_max(num1,num2,num3):
    if num1>num2 and num1>num3:
       return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
         return num3
#end 

num1,num2,num3=map(int,input('Ente the number:-').split())
result=fun_max(num1,num2,num3)
print(f'{result} is largest amomg {num1} {num2} {num3}')

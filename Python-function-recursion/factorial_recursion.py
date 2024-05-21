
#begin
def fact_num(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num*fact_num(num-1)
#end

num=int(input("enter the number "))
result=fact_num(num)
print(f'factorial of {num} is:-',result)



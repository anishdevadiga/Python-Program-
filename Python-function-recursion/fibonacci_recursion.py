#begin
def fibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)
#end

#begin
def fibo_series(num,count=0,result=[]):
    if count<num:
       result.append(fibo(count))
       return fibo_series(num,count+1,result)
    else:
        return result
#end



n=int(input("Enter thee no of terms:-"))
if n<0:
    print("Invalid input,enter postitve number only")
else:
    print(f"Fibonacci series up to {n} terms :-")
    list_fibo=fibo_series(n)
    print(list_fibo)



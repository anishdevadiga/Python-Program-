def armstrongnumber(n):
    sum =0 
    if n <= 0:
        return "Armstrong number cannot be negative or zero"
    else:
        temp = n
        while temp > 0:
            digit = temp % 10
            sum+=digit ** 3
            temp//=10
        if n == sum:
            return "Armstrong number"
        else :
            return "not a armstrng number"
print(armstrongnumber(13))


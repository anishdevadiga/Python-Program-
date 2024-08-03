#print n prime numbers

#begin
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

#end

#begin
def print_n_prime(n):
    count =0 
    num =2
    while count< n:
        if is_prime(num):
            print(f'{num}\t')
            count+=1
        num+=1
        
#end

n=10
print_n_prime(n)
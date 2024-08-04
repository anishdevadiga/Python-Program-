#begin
def small_string(str):
    list_str=list(str)
    stack_str=[]
    for c in list_str:
        if stack_str and stack_str[-1] == '1' and c == '0':
            stack_str.pop()
        else:
            stack_str.append(c)
    return ''.join(stack_str)
#end


binaryString = input("Enter a binary String : ")
print(small_string(binaryString))
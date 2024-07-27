def checkInput(xlist,y):
    if len(xlist) < 4:
        print("Error!,number of list elements must than greater than 4")
        return False
    if y<0 :
         print("n value cannot be negative")
         return False
    return True

def removeElements(x,y):
    sortedList=sorted(x)
    outlierList=sortedList[y:-y]
    print("Original List :",x)
    print("Sorted List :",sortedList)
    print("Outlier removed list:",outlierList),

def main_block():
    try:
        userInput=list(map(float,input("Enter the list of number seperated by comma : ").split(',')))
        n=int(input("Enter a value for n : "))
        if checkInput(userInput,n):
            removeElements(userInput,n)
    except ValueError:
        print("Invalid input error,enter only numeric values")

main_block()
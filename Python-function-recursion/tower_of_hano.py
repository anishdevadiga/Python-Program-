#begin
def tower(num,source,destination,auxilary):
    if num==1:
        print(f"Moving disk {num} from {source} to {destination}\n")
    else:
        tower(num-1,source,auxilary,destination)
        print(f"Moving disk {num} from {source} to {destination}\n")
        tower(num-1,auxilary,destination,source)
#end

num=int(input("Enter number of disks:-"))
s,d,a=input("Enter source destination auxilary:-").split()
tower(num,s,d,a)

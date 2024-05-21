list1= [1,2,3,4]
print(list1)
print(list1[1])

#string list
list_str=["anish","mca"]
print(list_str[1])

#negative indexing
list_int=[1,2,3,4,5,6,7,8]
print(list_int[-1])

#slicing
print("\nSlicing")
print(list_int[1:3])
print(list_int[3:])
print(list_int[:5])
print(list_int[-3:-1])

#modify
list_str[1]="devadiga"
print(list_str)
#methods
print("\nAppend")
list_int.append(9)
print(list_int)

print("\ninsert")
list_str.insert(1,"mca")
print(list_str)

#extend
list_str.extend(list_int)
print(list_str)

#pop
print(list_str.pop())

#pop with index
print(list_str.pop(2))

#remove
list_str.remove(1) #if printed then returns None

#delete list
list_del=[1,2,3]
del list_del
#print(list_del)

#clear
list_clr=[1,2,3,4]
list.clear(list_clr)
print(list_clr)

#sort and reverse
list_sort=[9,6,4,3,6,1,2]
list_sort.sort()
print(list_sort)
list_sort.sort(reverse=True)
#list.sort(list_str) error bcz tha tlist has different data typr
print(list_sort)
list_sort.reverse()
print(list_sort)

#copy
list_copy=list_sort.copy()
print(list_copy)

#count
print(list_copy.count(6))

#length
print(len(list_copy))
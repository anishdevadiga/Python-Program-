import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
print("array length",len(arr))

#slicing arrname[start:end:step]
#end is exclusive
#default step count is 1

print(arr[1:4])

print(arr[:4:]) #if start is not specified then default value is zero

print(arr[1::]) #if end is not specified goes till array length

print(arr[1:5:3]) #step means increment

print(arr[::2]) #takes default start and end value

print(arr[::]) #prints entire array

#negative step

print(arr[7:1:-2]) #here start must be from last index of the array

print(arr[::-2])#prints array in reverse order with step two

print(arr[::-1])#prints entire array in reverse order


import numpy as np
arr=np.array([1,1,0,3,2,5,6,7,4,4,9,8,7])

#here sort and append method makes changes on the original array
print("Before sroting array",arr)
arr.sort()
print("After sorting ",arr)

arr1= [1, 2, 3, 4, 5]
print("Before appending ",arr1)
arr1.append(100)
print("After appending ",arr1)

arr1.append("100")
print("After string appending",arr1)
#since arr1 is a list not a array 
#if we want a homogenous array the nus e numpy

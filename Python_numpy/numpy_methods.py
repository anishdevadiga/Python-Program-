import numpy as np

arr=np.array([1,1,0,3,2,5,6,7,4,4,9,8,7])
arr2=np.array([0,1,2,3,4,5,6,7,8,9])

#sort  delete insert creaets a copy of the  array as an output 
#but doesnot affect the oiginal array

#sorting
print("Sorted array",np.sort(arr))

 #inserting
 #np.insert(arranme,index,element)
 #eleemt must of same type
new_arr=np.insert(arr2,5,10)
print("Array after insertion",new_arr)

#deleteing
#numpy.delete(arrname,index)
new_arr2=np.delete(arr2,5)
print("Array after deletion",new_arr2)

#fliping -reversing the entire array
print("Flipped (reversed) array",np.flip(arr2))
print("original array",arr)

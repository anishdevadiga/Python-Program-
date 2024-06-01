import numpy as np

#array creation
arr=np.array([1,2,3,4])

print(arr)

#dimension
print(arr.ndim)

#creatina arr by specifying dim

adim=np.array([1,"2",3.4],ndmin=2)
print(adim)
print(adim.ndim)

#creation of array by specfying data type
ad_type=np.array([1,'A','C',1.5],dtype=str)
#ad_type=np.array([1,'A','C',1.5],dtype=int) error
#ValueError: invalid literal for int() with base 10: 'A'
print(ad_type)

#2d array
twod=np.array([[1,2,3],[1,2,3]])
print(twod)
print(twod.ndim)

#3d array
threed=np.array([
                [[1,2,3],[10,20,30]],
                [[100,200,300],[1000,2000,3000]]
                ])
print(threed)

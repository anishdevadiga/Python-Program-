import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])

x=np.where(arr==2)
print(x)
#output
#(array([1], dtype=int64),)

y=np.where(arr==0)
print(y)
#output (array([], dtype=int64),)

y1=np.where(arr=="str")
print(y1)
#output (array([], dtype=int64),)
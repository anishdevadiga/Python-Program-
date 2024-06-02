import pandas as pd
import numpy as np

#coverting series to dataframe
val={"rollno":[11,21,31],"name":["a","b","c"]}
#rollno and name are the two series
#dataframecan be considered as a collection of series
data_frm=pd.DataFrame(val)
print(data_frm)

#data frame with random valuewithin arange
df = pd.DataFrame(data=np.random.randint(1, 100, size=(100, 5)), columns=['a', 'b', 'c', 'd', 'e'])
print("Dataframe with random values\n",df)

new_data=pd.DataFrame(val,index=["d1","d2","d3"])
print(new_data)
'''
    rollno name
d1      11    a
d2      21    b
d3      31    c

'''
print("Element at d1\n",new_data.loc['d1':'d2'])
#or
print("Element at d1\n",new_data.loc[['d1','d2']])
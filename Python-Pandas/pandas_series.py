import pandas as pd

d=[1,2,3,4]
s1=pd.Series(d)
print(s1)

val=[11,21,31,41]
s2=pd.Series(data=val,index=['a','b','c','d'])
print(s2) 

#indexing
print("First value of s1",s1[0])
print("First value of s2",s2['a'])

#series using dictionary
cal={"d1":420,"d2":380,"d3":500}
dict_series=pd.Series(cal)
print("Dictoinary series\n",dict_series)
print("Accesing d1",dict_series['d1'])
#accesing storing values 
new__dict_series=pd.Series(dict_series,index=['d1','d2'])
print("New dict \n",new__dict_series)
#specifying own imdexing
index_dict= pd.Series(cal,index=['1','2','3'])
'''
output
#1   NaN
2   NaN
3   NaN

we canot change the key values of a dictionary defined as series
'''
print(index_dict)


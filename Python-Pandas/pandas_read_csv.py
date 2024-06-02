import pandas as pd
# Load the dataset
data = pd.read_csv('/Research data set/diabetics data set/diabetes2.csv')
data.info()

#head(count)
print(data.head(10))
print(data.tail(10))

#accesing
print("Accesing elements at index 50\n",data.loc[50])
print("Accesing elements from 50 to 60\n",data.loc[50:60])

#printing 2 rows
print("Accesing elements at index 0 1\n",data.loc[[0,1]])

#to_string()
#print(data.to_string()) #prints entire csv file

#max_rows
print("MAX rows", pd.options.display.max_rows)

#we can increase the moximum number of rows to display data frame
'''
pd.options.display.max_rows=767
print("MAX rows after applying trick ", pd.options.display.max_rows)
'''

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
     









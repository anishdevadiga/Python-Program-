import numpy as np

data = [16, 9, 14, 11, 13, 6, 18, 15, 10, 12]
#data = list(map(int, input("Enter 10 integers separated by commas: ").split(',')))


#sorted data
sorted_data=sorted(data)
print("Sorted data: ",sorted_data)

#min and max value
min_val=np.min(sorted_data)
max_val=np.max(sorted_data)

#iqr
q1=np.percentile(sorted_data,25)
median=np.median(sorted_data)
q3=np.percentile(sorted_data,75)
iqr=q3-q1
print("InterQuartile Range : ",iqr)

#outliers
lower_bound=q1-(1.5*iqr)
upper_bound=q3+(1.5*iqr)
print(f"Outliers are [{lower_bound},{upper_bound}]")

print("\nFive Number Summary table\n")
print("Min value\t|\tQ1 Value\t|\tMedian\t|\tQ3 value\t|\tMax Value")
print(f"{min_val}\t\t|\t{q1}\t\t|\t{median}\t|\t{q3}\t\t|\t{max_val}")



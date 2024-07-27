import numpy as np
marks =[38, 41, 36, 31, 45, 38, 27, 32, 29, 39]

#mean
print("Mean of the marks",np.mean(marks))

#when marks increased by 2
marks_incr_by_2=[mark + 2 for mark in marks]
print("Mean of marks afrer 2 marks is increased",np.mean(marks_incr_by_2))

#when marks is deducted by 1
marks_decr_by_1=[mark-1 for mark in marks]
print("Mean of marks afrer 1 marks is decremented",np.mean(marks_decr_by_1))

#when mark is halfed
marks_half = [ mark * 0.5 for mark in marks]
print("Mean of marks afrer  marks is halfed",np.mean(marks_half))
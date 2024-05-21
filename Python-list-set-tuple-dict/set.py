set_var={1,2,1,1,1,1}
print(set_var)

#creation using set method
set_new=set({1,2,3,3,3})
print(set_new)

#check for element
print(1 in set_var)
print(3 not in set_new)

#add emthod
set_new.add(4)
print(set_new)

set_new.add(0)
print(set_new)

#remove
set_new.remove(4)
print(set_new)

#pop
set_var.pop()
print(set_var)

#update
x={1,2,3,4}
y={5,6,7,8}
x|=y
print(x)

#update method
y.update(x)
print(y)

#issubset method
print(set_new<=x) #false
print(set_var<=x)
print(set_var.issubset(x))

#superset
print(x>=set_var)
print(x.issuperset(set_var))

#union,interesection
s1={1}
s2={True}
print('union')
print(s1.union(s2)) #ans 1
print(s2.union(s1)) # ans True

#the value of the calling set will be displayed
print(s1.intersection(s2)) #ans True
print(s2.intersection(s1)) #ans 1
#the value of the set inside the function as parameter will be displayed

#disjoint
s3={0}
s4={1}
print(s3.isdisjoint(s4))
print(s4.isdisjoint(s2))

#clear
s3.clear()
print(s3)

#copy
s3=s4.copy()
print(s3)

#intersection update 
a={1}
b={1,2}
c={1,2,3}
b.intersection_update(c)
print(b)

#difference and difference update 
d={1,2,3,4}
e={1,2}
print(d.difference(e))
d.difference_update(e)
print(d)

#del
del e

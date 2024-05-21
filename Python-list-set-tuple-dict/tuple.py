tuple_var=(1,2,3,4,5,6)
print(tuple_var)

tuple_str=("anish")
print(type(tuple_str))#type is str not tuple

tuple_str1=("anish",)
print(type(tuple_str1))#type is tuple

#indexing
print(tuple_var[0])

#conversion of tuple to list
tuplelist=tuple_str1
print(type(tuplelist))

tuplelist=tuplelist+tuple_str1;
print(tuplelist)

del tuplelist

tuple_new=tuple((1,2,3,4,5))
print(tuple_new)

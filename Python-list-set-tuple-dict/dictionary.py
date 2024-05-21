dict_var={"rollo":1,"age":20}
print(dict_var)

dict_new=dict(anish=230977,cass='mca')
print(dict_new)

#add 
dict_new['sectio']='a'
print(dict_new)

#modfiy
dict_new['sectio']='b'
print(dict_new)

#key
print(dict_new.keys())

#values
print(dict_new.values())

#update or modfiy uisng update method
dict_new.update({'job':'data'})
print(dict_new)

#pop
dict_new.pop('job')
print(dict_new)

dict_new.popitem()
print(dict_new)

del dict_var['rollo']
print(dict_var)
del dict_var
#print(dict_var)
dict_ = {'name':'Ranjith','age':23,3:'m'}
print(dict_.keys())
print(dict_.values())
print(dict_.items())
for i,j in dict_.items():
    print(str(i)+": "+str(j))
print(dict_[3])
print(dict_.get(3))
print(dict_.get(30))
del dict_[3]
print(dict_, type(dict_))
a = 100
b = 100
print(a is b)
print(id(a),id(b))
b = 90
print(a is b)
print(id(a),id(b))
s = {8,9,9,5,6,7,8,8,9,5,9}
print(s,type(s))
s.update([7,8,8,0,9999])
print(s)
s.remove(9)
print(s)
s.add(69)
print(s)
s1 ={6,7,8,9}
s2 ={1,2,3,4,5,6,7}
print(s1.intersection(s2))
print(s1&s2)
print(s1.union(s2))
print(s1|s2)
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)
f = frozenset(s1)
f.update([7,8]) # Gives Error
lst = [20,30,40,50]
b = bytes(lst)
print(b)
print(type(b))

b1 = bytearray(lst)
print(b1)
print(type(b1))
b1[0]=90
print(b1)
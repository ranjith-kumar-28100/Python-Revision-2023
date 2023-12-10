lst = [56, 45, 45, 78, 45, 65, 45, 69, 78]
l = [i for i in lst if lst.count(i) == 1]
print(l)

l = [i ** 3 for i in lst]
print(l)

l = [i for i in range(1, 21) if i % 2 == 0]
print(l)

lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 4, 3, 2, 1]
prod = [i * j for i, j in zip(lst1, lst2)]
print(prod)
prod = [lst1[i] * lst2[i] for i in range(len(lst1))]
print(prod)

lst1 = [5, 6, 7, 9, 0, 77, 5]
lst2 = [56, 58, 54, 56, 9, 7, 6]

common = [lst1[i] for i in range(len(lst1)) if lst1[i] in lst2]
print(common)

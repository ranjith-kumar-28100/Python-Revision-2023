from functools import  reduce
lst = [5, 6, 8, 9, 11, 10, 2, -6, 0]
filtered_lst = list(filter(lambda x: x % 2 == 0 and x != 0, lst))
print(filtered_lst)

mapped_lst = list(map(lambda x: x * 2, lst))
print(mapped_lst)

inp_list = list(map(int, input('Enter Space Separated Integers').split(' ')))
print(inp_list)
print(len(inp_list))
print(type(inp_list[0]))

reduced_sum = reduce(lambda x,y:x+y,lst)
print(reduced_sum)

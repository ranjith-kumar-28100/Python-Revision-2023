def custom_range(x, y):
    while x <= y:
        if y % x == 0:
            yield x
        x += 1


lst = custom_range(3, 21)
for i in lst:
    print(i)

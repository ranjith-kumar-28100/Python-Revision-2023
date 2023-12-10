def average(a=10, b=10):
    print(f"a = {a},b = {b}")
    return (a + b) / 2


print(average(78, 89))
print(average(b=78, a=89))
print(average(a=78, b=89))
print(average())
print(average(a=45))
print(average(b=56))

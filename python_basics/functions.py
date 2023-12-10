def average(a, b):
    return (a + b) / 2


def calc(a, b):
    sum = a + b
    diff = a - b
    prod = a * b
    quo = a / b
    return sum, diff, prod, quo


avg = average(8, 9)
print(f"Average of 8 and 7 is {avg}")
sum, diff, prod, quo = calc(8,9)
print(sum,diff,prod,quo)
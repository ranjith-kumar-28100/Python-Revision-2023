n = int(input("enter an even number: "))
try:
    assert n % 2 == 0, "You have entered odd number, please enter even number"
except AssertionError as obj:
    print(obj)
print("The value of n is ", n)

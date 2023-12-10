age = int(input("enter your age: "))
if age >= 18:
    print("You are a major.")
else:
    print("You are a minor.")

n = int(input("enter a number: "))
if n == 0:
    print(f"{n} is neither odd nor even")
elif n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

a, b, c = input("enter 3 no.s with space").split(" ")
a, b, c = int(a), int(b), int(c)
if a > b and a > c:
    print(f"{a} is greater")
elif b > c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")

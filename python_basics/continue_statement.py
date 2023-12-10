x = 0
while x < 20:
    x += 1
    if (x % 3 == 0):
        print(f" multiple of 3 found, skipping.")
        continue
    print(x)

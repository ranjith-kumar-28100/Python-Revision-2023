x = 123 #Global

def say_hi():
    x = 10
    if x>0:
        print("Hi")
    else:
        print("Hello")
    print(x)
    print(globals()['x'])

say_hi()
print(x)
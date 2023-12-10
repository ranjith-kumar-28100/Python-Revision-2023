def disp():
    print("Hai, Hello, Vanakkam")


x = disp
x()


def add(a, b):
    return a + b


y = add
print(y(10, 11))

print(type(y))


def greet(name):
    def message():
        return "Hello, Have a nice day "

    return message() + name


print(greet("RKG"))


def do_something(something):
    return "doing something: " + something


def say_hello():
    return "Saying Hello"


print(do_something(say_hello()))


def display():
    def message():
        return "You're a badass"

    return message()


print(display())


def fun(lst):
    for i in lst:
        print(i)


fun([7, 8, 65, 4, 56, 7])

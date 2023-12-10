def cube(func):
    def inner():
        n = func()
        return n ** 3

    return inner


def half(func):
    def inner():
        n = func()
        return n // 2

    return inner


@cube
@half
def num():
    return 10


print(num())

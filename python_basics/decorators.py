def decor_func(inp_fun):
    def inner_fun():
        res = inp_fun()
        return res * 2

    return inner_fun


@decor_func
def get_inp():
    return 5


def new_inp():
    return 10


new_func = decor_func(new_inp)
print(new_func())
print(get_inp())


def decor_func2(inp_func):
    def inner_func(name,age):
        res = inp_func(name,age)
        return res + " How are you"

    return inner_func


@decor_func2
def hello(name,age):
    return "hello " + name+" you are "+str(age)+" years old"


print(hello("Ranjith",23))

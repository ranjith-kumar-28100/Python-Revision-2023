def my_fun(x, *args, **kwargs):
    print(x)
    print(args, len(args))
    for i in args:
        print(i)
    print(kwargs, len(kwargs))
    for k, v in kwargs.items():
        print(k, v)


my_fun(10, 56, 89, 789, 564, name="Ranjith", age=21)
my_fun(50, name="Ranjith", age=23)
my_fun(50, 98, 78, 90)

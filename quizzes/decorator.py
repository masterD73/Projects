def ensure(typ):
    def checker(f):
        def checked_func(arg):
            if isinstance(arg, typ):
                return f(arg)
            else:
                raise TypeError("Type should be int only.")

        return checked_func

    return checker


@ensure(int)
def foo(n):
    print(n)

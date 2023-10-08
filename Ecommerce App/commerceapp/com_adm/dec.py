


def dec_div(func):
    def wrapper(a,b):
        if b>a:
            a,b = b,a
        return func(a,b)
    return wrapper


@dec_div
def div(a,b):
    print(a/b)


div(5,10)
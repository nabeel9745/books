
def decorator_divide(func):
    def wrap(a,b):
        if b>a:
            b,a=a,b
        return func(a,b)
    return wrap        

@decorator_divide
def divide(a,b):
    print(a/b)
divide(5,10)
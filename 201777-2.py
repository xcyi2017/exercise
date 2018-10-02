from functools import wraps
def outer(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print('{:*^20}'.format('begin'))
        results = func(*args, **kwargs)
        print('{:*^20}'.format('end'))
        return results  
    return wrap

@outer
def func1(x,y=1):
    return x+y


print(func1(2))
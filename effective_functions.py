

def uppercase(func):
        def wrapper():
            res = func()
            upper_res = res.upper()
            return upper_res
        return wrapper

@uppercase
def greet():
    return 'hi'

greet()

# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage

# class BlueCar(Car):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.color = 'Blue'


# print(BlueCar('green', 78007).color)
import functools
from dis import dis
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__, args,kwargs)
        res = func(*args, **kwargs)
        print(res)
    return wrapper

@trace
def greet(name, message):
    return 'Hi {}, {} '.format(name, message)

print(greet('Kwezi', 'How are you ?'))   

# dis(greet)
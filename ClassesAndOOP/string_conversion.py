class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __repr_(self):
        return '__repr__ for Car'
        
    def __str__(self):
        return '__str__ for Car'

my_green_car = Car('green', 789078)

print(my_green_car)
my_green_car
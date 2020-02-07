# from collections import namedtuple

# # Car = namedtuple('Car', 'color mileage')

# # my_car = Car('green', 97090)

# # print(my_car.color)
# # print(my_car[0])
# # print(tuple(my_car))
# # print(*my_car)
# # print(my_car)

# #subclassing namedtuples
# Car = namedtuple('Car', 'color mileage')

# class MyCar(Car):
#     def hexcolor(self):
#         if self.color == 'red':
#             return 'yay'
#         else:
#             return 'nay'

# new_car = MyCar('red', 6658678)
# print(new_car.hexcolor())

# ElecCar = namedtuple('ElecCar', Car._fields + ('charge',))
# eCar = ElecCar('red', 324234,5436)
# print(eCar)


class Animal:
    def __init__(self, animal_type):
        self.animal_type = animal_type
    def __repr__(self):
        return 'Animal(animal_type=\'{}\')'.format(self.animal_type)
    
new_animal = Animal('Dog')
print(new_animal)
print(new_animal.animal_type)
        

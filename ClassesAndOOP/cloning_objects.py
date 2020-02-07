# xs = [[1,2,3],[4,5,6,]]
# ys = list(xs)
# xs.append(['Yes I\'m different'])
# xs[1][0] = 'X'
# print('shallow - ', xs)
# print('shallow - ',ys)
# print(xs[1][0] is ys[1][0])


# from copy import deepcopy

# xs = [[1,2,3],[4,5,6,]]
# zs = deepcopy(xs)
# xs[0][0] = 'Changed'

# print('Deep - ',xs)
# print('Deep - ',zs)



#copy arbitrary objects
import copy
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point ({},{})'.format(self.x, self.y)

a = Point(2,3)
b = copy.copy(a)

print(a)
print(b)
print(a is b)




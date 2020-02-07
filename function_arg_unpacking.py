def print_vector(x,y,z):
    print('<{},{},{}>'.format(x,y,z))
#tuples
tuple_vec = (1,0,1)

print_vector(*tuple_vec)
list_vec = [1,0,1]
print_vector(*list_vec)

genexpr = (x * x for x in range(3))
print_vector(*genexpr)

#collections/dictionaries
dict_vec = {'y':1,'x':0,'z': 1}
print_vector(**dict_vec)
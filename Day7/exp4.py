# Empty tuple
init_tuple = ()
print("Length of init_tuple:", len(init_tuple))

# Compare tuples
init_tuple_a = ('a', 'b')
init_tuple_b = ('a', 'b')
print("Are init_tuple_a and init_tuple_b equal?", init_tuple_a == init_tuple_b)

# Concatenate tuples
init_tuple_a = ('1', '2')
init_tuple_b = ('3', '4')
result = init_tuple_a + init_tuple_b
print("Concatenated tuple:", result)

# Tuple multiplication producing empty tuple
l = [1, 2, 3]
init_tuple = ('Python',) * (len(l) - l[0] - l[1])
print("Tuple multiplication result:", init_tuple)

# Proper tuple multiplication
init_tuple = ('Python',) * 3
print(init_tuple)
print(type(init_tuple))

# Immutable tuples: correct way to modify
init_tuple = (1,) * 3
init_tuple = (2,) + init_tuple[1:]
print(init_tuple)

# Slicing a repeated tuple
init_tuple = ((1,2),) * 7
print(len(init_tuple[3:8]))

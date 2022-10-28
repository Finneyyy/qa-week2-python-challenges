'''
Tuples: ordered, immutable
Basically read-only lists

They are more memory-efficient due to not needing to change
Main advantage: Having a list of constants that you won't need to change
'''

tuple_a = [1,2,3],[4,5,6],[7,8,9]

# if a tuple contains mutable objects, they don't become immutable when 
# they are in a tuple
tuple_a[1][1]=0
print(tuple_a)
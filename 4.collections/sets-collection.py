# Sets -> unordered, mutable
# You can't have a set of mutable objects, they have to be immutable
# this is due to the way sets handle objects (via hashing)

set_a={1,2,3}

# to make an empty set, use the set constructor
empty_set=set()

# remove entry in a set if it's there
set_a.discard(4)
print(set_a)
'''
Definitions:
# Collections -> Data type that holds several values
# Mutable -> Able to be changed
# Ordered -> Retains order of elements, accessible via indices (index)

Lists: ordered, mutable

'''

fruits=["Apple","Cherry","Banana","Apricot","Orange"]

# forward indexing
print(fruits[1])

# negative indexing
print(fruits[-2])

# slicing
# Goes from index 1 up to but not including the last index
print(fruits[1:-1])

# slicing
# prints everything up to last index
print(fruits[:-1])

# slicing
# prints entire array
print(fruits[:])

# slicing
# reverse the array by step (::-1 reverses the list by each step)
print(fruits[::-1]) # result: ['Orange', 'Apricot', 'Banana', 'Cherry', 'Apple']

# adding things to the list
fruits.append("Strawberry")

# add something to a specific point in the array/list
fruits.insert(2, "Raspberry")

# add objects to the end of the list
fruits.extend("Pineapple", "Pear", "Plum")

# does the same as extend, adds list to the end of the list
fruits = fruits + ["Mango","Blackberry", "Cranberry"]

# removes first occurence of object
fruits.remove("Mango")

# removes the object at an index
fruits.pop(1)

# print the object that pop removes
print(fruits.pop(1))

# deletes the object at index 3
del fruits[3]

# replaces an element in the array
fruits[2] = "Grapefruit"

# sort by alphabetical/numerical order
fruits.sort()
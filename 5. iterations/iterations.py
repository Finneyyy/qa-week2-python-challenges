#import num2words
# Iterations -> repeatedly execute same code till stop condition

'''
Loops:

# While
# For
'''

# While loop
i=0
while i<10:
	print(i)
	i+=1

print(" ")

# for loop
fruits= ["apple","pear","banana","cherry"]
for index, fruit in enumerate(fruits):
#	data[index]=data.apply(num2words)
	print("The",f"{index}'th fruit is", fruit.capitalize())

print(" ")

# a for loop to print a range (0->10 incrementing by 1 each time)
for i in range(0,11,1):
	print(i)

print(" ")

cap_cities = {"Ireland":"Dublin", "France":"Paris", "England":"London"}
for country, capital in cap_cities.items():
	print("Capital of",country, "is",capital)

print(" ")

# comprehensions

# checks the length of the elements ->
# if the element has 6 characters, capitalise those objects
cap_fruits=[fruit.capitalize() if len(fruit)==6 else fruit for fruit in fruits]
print(cap_fruits)

print(" ")

# invert dictitionary
new_cap_cities={capital:country for country, capital in cap_cities.items()}
print(new_cap_cities) 
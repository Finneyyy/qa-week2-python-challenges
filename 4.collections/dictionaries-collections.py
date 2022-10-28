# Dictionaries -> ordered(ish), mutable

cap_cities = {"Ireland":"Dublin", "France":"Paris", "England":"London"} # dict(key=value, ...)
print(cap_cities["France"])

# KeyError thrown if key isn't in dict
#print(cap_cities["Geramy"])

# Returns the key if it's there, otherwise gives default value
print(cap_cities.get("Germany","Doesn't exist"))
print(cap_cities)

# add something to dict
cap_cities.update(Italy="Rome")

# print and remove an entry
print(cap_cities.pop("France"))

# remove an entry in the list entirely
del cap_cities["England"]
print(cap_cities)
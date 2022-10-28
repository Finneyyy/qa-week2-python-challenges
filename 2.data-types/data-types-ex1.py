# take in a whole number (10) and a float (2.3)
# and round the float to its nearest whole
# then print them out

number1=input("Enter whole number: ")
number2=input("Enter decimal number: ")

integer_number=int(number1)
float_number=float(number2)
round_number=int(round(float_number))

print(number1)
print(number2)
print(round_number)
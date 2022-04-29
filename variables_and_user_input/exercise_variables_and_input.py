# Q1
number1 = input('Enter a number: ')
number2 = input('Enter another number: ')
print(float(number1) + float(number2))

# Q2
number1_q2 = input('Enter a number: ')
number2_q2 = input('Enter another number: ')
print(float(number1_q2) * float(number2_q2))

# Q3
distance_km_input = input('How many kilometres? ')
distance_km = float(distance_km_input)
distance_m = int(distance_km * 1000)
distance_cm = int(distance_km * 100000)
print_m = f"{distance_km}km = {distance_m}m"
print_cm = f"{distance_km}km = {distance_cm}cm"
print(print_m)
print(print_cm)

# Q4
name = input('What is your name? ')
height = input('How tall are you (cms)? ')
output = f"{name} is {height}cms tall."
print(output)
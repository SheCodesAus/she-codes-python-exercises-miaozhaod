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

# Q5
name_q5 = input('What is your name? ')
age_q5 = input('How old are you? ')
age_to_90 = 90 - int(age_q5)
output_q5 = f"{name_q5} has {age_to_90} years to turn 90"
print(output_q5)

# Q6
number1_q6 = input('Enter a float: ')
number2_q6 = input('Enter another float:')
output_q6 = int(float(number1_q6) * float(number2_q6))
print(output_q6)

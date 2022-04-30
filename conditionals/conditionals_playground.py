# Data Types - strings, int, floats, boolean (case-sensitive, must capitalised)
# boolean1 = True
# boolean2 = False 
# print(type(boolean1))

knows_password = False
knows_username = False
# boolean operators - NOT, AND, OR
login = knows_password and knows_username
recover = knows_password or knows_username

# print(type(login))
# print(login)
# print(not knows_password)

is_raining = False
is_cold = True
# print(type(is_raining))
type(is_cold)

number1 = 3
number2 = 3.0
print(number1 == number2)
print(number1 is number2)

name = 'Camila'
if name == 'Asli': 
    print('hello')
elif name == "Camila":
    print(f"Hello {name}, what are we doing today?")
else:
    print('wow hello i missed you')

# is_raining = False
# temperature = 16
# wind_chill = 3
# if is_raining: 
#     print('Take an umbrella!')
# else: 
#     print('Do not take an umbrella')

# if temperature - wind_chill < 16:
#     print('Take a jumper')
# elif temperature - wind_chill > 30:
#     print("Euck, it's hot today, stay home")
# else: 
#     print('wow, what a lovely day!')
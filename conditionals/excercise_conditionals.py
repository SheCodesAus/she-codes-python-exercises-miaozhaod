# Q1
moths_in_house = True
if moths_in_house == True:
    print('Get the moth')
else: 
    print('No threats detected')

# Q2
moths_in_house = False
mitch_is_home = False
if moths_in_house: 
    if mitch_is_home:
        print("Hoooman! Help me get the moths!")
    else: 
        print("Meooooooooooooow! Hissssss!")
else: 
    if mitch_is_home:
        print("Climb on Mitch.")
    else:
        print("No threats detected.")

# Q3
light_color = "Red"
car_detected = True
if light_color == "Red":
    if car_detected:
        print('flash')
    else: print('Do nothing')
elif light_color == "Green":
    print('Do nothing')
else:
    print('Do nothing')

# Q4
height = input('What is your height(cms)? ')
height_int = int(height)
if height_int < 120:
    print("Sorry, not today :(")
else: print("Hop on!")

# Q5
username = input('Enter your username: ')
password = input('Enter your password ')  
result = ""
output = f"Username: {username} \nPassword: {password} \n"
if username == "fleur" and password =="password123":
    result = "Correct!"
    output += result 
    print(output)
else: 
    result = "Incorrect!"
    output += result
    print(output)

# Q6
email = input('Enter your email: ')
if "@" in email and "." in email:
    print('Valid email')
else: print('invalid email')





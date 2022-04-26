from email import message


weather = 'rainy'

# print(weather)
# Data types - 
# string is a text data - quotes
# integer is a numerical data (whole number) - just give number
# Float numerical (with decimals)
height = 165
weight = 55.8
# print(type(weather))
# print(type(height))
# print(type(weight))

day = "Saturday"
# print(type(day))
message = f"Today is {day}!"
message2 = "Today is " + day
# print(message)
# print(message2)

run1_dist = 1400

# total_dist = run1_dist + run2_dist
# print(total_dist)

run4_dist = 1.35
# total_dist = run3_dist + run4_dist
# print(total_dist)

# division and mutiplication
# print(run1_dist / 1000)
# print(run3_dist * 1000) 
# division  is always produce float
# other calculation depens on the data type
# as long as there's one float, will produce float

name = 'Miao'
run2_dist = 1000
run3_dist = 1.7
# print(name + run2_dist) - error
# print(name * run2_dist) - multiple times of name
# print(name * name) - err
# print(name * run3_dist) - err

# typecast to change the data type
print(name * int(run3_dist))
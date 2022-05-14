import csv
from posixpath import split;

# Q4
with open('colours_213.csv') as csv_file:
    reader = csv.reader(csv_file)
    red = []
    green = []
    blue = []
    yellow = []
    for line in reader:
        if 'red' in line[4].lower():
            red.append(line[4])
        if 'green' in line[4].lower():
            green.append(line[4])
        if 'blue' in line[4].lower():
            blue.append(line[4])
        if 'yellow' in line[4].lower():
            yellow.append(line[4])

    red_length = len(red)
    green_length = len(green)
    blue_length = len(blue)
    yellow_length = len(yellow)

    print(f"Red: {red_length}")
    print(f"Green: {green_length}")
    print(f"Blue: {blue_length}")
    print(f"Yellow: {yellow_length}")

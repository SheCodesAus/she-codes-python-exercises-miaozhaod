import csv

# import os
# cwd = os.getcwd() // get current directory
# print(cwd)

# cats = ["meow", "hmmm"]
# with open("cats.txt", mode="w") as file:
#     writer = csv.writer(file, delimiter="\n")
#     writer.writerow(cats)

with open("2016_pilbara.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)

population = []

with open("2016_pilbara.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        population.append(line)
print(population)

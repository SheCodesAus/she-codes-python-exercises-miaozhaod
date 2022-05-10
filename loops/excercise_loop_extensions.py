# Q1
# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08],
# ]

# baby_spinach = input("Number of Baby Spinach: ")
# hot_chocolate = input("Number of Hot Chocolate: ")
# crackers = input("Number of Crackers: ")
# bacon = input("Number of Bacon: ")
# carrots = input("Number of carrots: ")
# ornages = input("Number of oranges: ")
# all_ammounts = [int(baby_spinach), int(hot_chocolate), int(crackers), int(bacon), int(carrots), int(ornages)]

# index_list = list(range(0, len(groceries)))
# for index in index_list:
#     groceries[index].append(all_ammounts[index])

# all_price = []
# for grocery in groceries:
#     item = grocery[0]
#     price = float("{:.2f}".format(grocery[1] * grocery[2]))
#     all_price.append(price)
#     print(f"{item}: {price}")

# print(float("{:.2f}".format(sum(all_price))))

# Q2
# letters = [
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
# ]
# word = input("Enter a word: ")
# word_arr = list(word)
# for item in word_arr:
#     for letter in letters:
#         if letter == item:
#             myletter = letter
#             myletter_position_in_alphabet_list = letters.index(letter)
#             myletter_position_in_word_list = word_arr.index(item)
#             print(f"{myletter_position_in_word_list} {myletter}")

# Q3
# input = int(input("Enter a number: "))
# for i in range(1, input + 1):
#     print("*" * i)

# Q4
input = int(input("Enter a number: "))
for i in range(0, input):
    stars_number = i + i + 1  # to get how many stars in each row
    total_space = input * 2 - 1  # to get how many spaces each row is taken
    blanks_number = int((total_space - stars_number) / 2)  # to get the number of spaces before the stars
    space_print = " " * blanks_number
    star_print = "*" * stars_number
    print(f"{space_print}{star_print}")

# Q1
number = "0"
arr = []
while number != "":
    number = input("Enter a number: ")
    if number != "":
        arr.append(int(number))
while number == "":
    print("Empty")
    break
print(sum(arr))

# Q2
number = int(input("Enter a number: "))
arr = []
for num in range(0, number + 1):
    arr.append(num)
for num in arr:
    if num % 2 != 0:
        print(num)

# Q3
number = 30
guess = ""
while guess == "":
    guess = int(input("Guess a number: "))
while guess < number:
    print("Too low")
    guess = int(input("Guess a number: "))
while guess > number:
    print("Too high")
    guess = int(input("Guess a number: "))
while guess == number:
    print("Correct")
    break

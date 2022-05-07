# Q1
input = int(input("Enter a number: "))
for i in range(1, (input + 1)):
    result = input * i
    print(f"{input} * {i} = {result}")

# Q2
input = int(input("Enter a number: "))
arr = list(range(0, input + 1))
sum = 0
# print(sum(arr))
for i in range(0, len(arr)):
    sum = sum + arr[i]
print(sum)

# Q3
random_numbers = [3, 5, 9, 1]
random_numbers = [-3, -5, 9, 1]
random_numbers = []
sum = 0
for index in range(0, len(random_numbers)):
    sum = sum + random_numbers[index]
print(sum)

# Q4
mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldenreamers.xyz"],
]
for mail in mailing_list:
    print(f"{mail[0]}: {mail[1]}")

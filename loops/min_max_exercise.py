# find minimun
numbers = [4, 7, 10, 1, 2];

min = 0;
my_index = 0;
for index in range(0, len(numbers)-1):
    if(numbers[index] < numbers[index + 1]):
        min = numbers[index]
        my_index = index
    else:
        min = numbers[index+1]
        my_index = index + 1
    
print(min)
print(my_index)

# Q1
def temprature(temp_in_f):
    temp_in_c = (temp_in_f - 32) * 5 / 9
    return temp_in_c


# print(temprature(0))

# Q2
def isOdd(num):
    if (num % 2) == 0:
        return "False"
    else:
        return "True"


# print(isOdd(-1))

# Q3
def numbers(num):
    total = sum(num)
    length = len(num)
    mean = total / length
    return mean


# print(numbers([10, 5, 6]))

# Q4
def total_cost(price_per_unit, num_units):
    total = price_per_unit * num_units
    result = f"${total}"
    return result


print(total_cost(4.25, 3))

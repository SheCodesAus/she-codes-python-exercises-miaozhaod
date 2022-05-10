# definition
def hello():
    print("hello world")
    return "what's up"


# result = hello()
# print(result)


def add(number1, number2):  # formal parameters
    result = number1 + number2
    return result


# print(add(2, 2))


def create_greeting(name):
    greeting = f"hello {name}"
    return greeting


# print(create_greeting("chilli"))


def tripple(number):
    result = number * 3
    return result


# print(tripple(3))


def convert_cm_to_in(length_cm):
    length_in = length_cm / 2.54
    return length_in


# print(convert_cm_to_in(10))


def calculate_meam(a, b):
    total = a + b
    mean = total / 2
    return mean


print(calculate_meam(3, 4))


def camila():
    pass

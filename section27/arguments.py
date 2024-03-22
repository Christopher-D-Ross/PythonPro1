# Keyword Arguments
# def my_function(a, b, c):
#     # Perform action on a
#     # Perform action on b
#     # Perform action on c
#
# my_function(1, 2, 3)
# my_function(c=3, a=1, b=2)
#
#
#
# # Arguments with Default Values
# def my_function_dv(a=1, b=2, c=3):
#     # Perform action on a
#     # Perform action on b
#     # Perform action on c
#
# my_function_dv()
# my_function_dv(b=2)


def my_function_quiz(a, b=2, c=3):
    print(a, b, c)


# my_function_quiz(1)


# Unlimited Arguments
def print_numbers(*args):
    for n in args:
        print(n)


# print_numbers(1, 2, 3, 4, 5, 6)


def add_numbers(*args):
    sum_of_args = 0
    for n in args:
        sum_of_args += n
    return sum_of_args


# print(add_numbers(2, 2, 2, 2))


def print_an_arg(*args, arg):
    print(args[arg])


# print_an_arg(1, 2, 3, 4, 5, 6, arg=2)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=10, multiply=6)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Dodge")
print(my_car.model)
print(my_car.make)

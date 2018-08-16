def print_something():
    print("this came from the {} module".format(__name__))

def a_function(some_string):
    print(some_string)

def add_two(number):
    return number + 2
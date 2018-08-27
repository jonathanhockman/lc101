def example_one():
    number = input("Enter an integer: ")

    try:
        # attempt to execute this code
        number = int(number)
        number = 10 / number
    except ValueError:
        # execute int() fails
        print("Invalid integer entered")
    except ZeroDivisionError:
        # execute number entered is 0
        print("Tried to divide by zero")
    else:
        # only executes if no exception is thrown
        print("Converted and divided 10:", number)

def example_two():
    number = input("Enter a float: ")

    try:
        # attempt to execute this code
        if "." in number:
            number = float(number)
            if number == 0:
                print("raise ZeroDivisionError ourselves")
                raise ZeroDivisionError
            else:
                number = 10 / number
        else:
            print("raise ValueError ourselves")
            raise ValueError
    except ValueError:
        # execute int() fails
        print("Invalid float entered")
    except ZeroDivisionError:
        # execute number entered is 0
        print("Tried to divide by zero")
    else:
        # only executes if no exception is thrown
        print("Converted and divided 10:", number)

def example_three():
    number = input("Enter a number from 1 to 10: ")

    try:
        number = int(number)
        if number < 1 or number > 10:
            raise ValueError
    except ValueError:
        print("Not a number or out of range.")

def example_four():
    number = input("Enter a number from 1 to 10: ")

    try:
        number = int(number)
        if number < 1 or number > 10:
            raise ValueError("Value out of range")
    except ValueError as ve:
        print(ve.args[0])

example_four()
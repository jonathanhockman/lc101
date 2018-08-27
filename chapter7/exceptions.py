import menu

def try_except():
    number = input("Enter an integer: ")

    try:
        number = int(number)
        return "Successfully converted string to integer: {}".format(number)
    except ValueError:
        print("handled a ValueError")

def try_except_else():
    number = input("Enter an integer: ")

    try:
        number = int(number)
    except ValueError:
        print("handled a ValueError")
    else:
        return "Else was called because no exception was thrown"

    return "only executed because 'else' was not called due to exception"

def try_except_except():
    number = input("Enter an integer: ")

    try:
        if "." in number:
            number = float(number)
        else:
            number = int(number)

        repeat_string = number * "repeat"
        return repeat_string
    except ValueError:
        print("handled a ValueError")
    except:
        print("Something other than a ValueError happened")

def try_except_try_except():
    number = input("Enter a number: ")

    try:
        number = int(number)
        return "Successfully converted string to integer: {}".format(number)
    except ValueError:
        try:
            number = float(number)
            return "Successfully converted string to float: {}".format(number)
        except ValueError:
            print("handle ValueError")

def try_except_finally():
    number = input("Enter an integer: ")

    try:
        number = int(number)
    except ValueError:
        print("handled a ValueError")
    finally:
        print("This will always print no matter what")

    return "Made it here just fine"

if __name__ == '__main__':
    # Bad Options
    # options = {
    #     "try/except": try_except,
    #     "try/except/else": "this is not a function",
    #     "try/except/except": try_except_except,
    #     "try/except/finally": 1
    # }

    # Good options
    options = {
        "try/except": try_except,
        "try/except/else": try_except_else,
        "try/except/except": try_except_except,
        "try/except/try/except": try_except_try_except,
        "try/except/finally": try_except_finally
        }

    menu = menu.Menu(options)
    menu.startMenu()
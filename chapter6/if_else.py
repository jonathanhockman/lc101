from msvcrt import getch

# binary
def run_binary(x):
    if x > 10:
        return "greater than 10"
    else:
        return "not greater than 10"

# nested
def run_nested(x):
    if x > 10:
        if x > 20:
            return "greater than 20"
        else:
            return "greater than 10 not greater than 20"
    else:
        return "not greater than 10"

# chained
def run_chained(x):
    if x > 10:
        return "greater than 10"
    elif x < 5:
        return "less than 5"
    else:
        return "not greater than 10 not less than 5"

# ternary
def ternary(x):
    return "greater than 10" if x > 10 else "not greater than 10"

def ternary_tuple(x):
    return ("not greater than 10", "greater than 10")[x > 10] # not recommended

def main():
    functions = (run_binary, run_nested, run_chained, ternary, ternary_tuple)

    menu_message = """
Select one:
0. binary
1. nested
2. chained
3. ternary
4. ternary(tuple)
q. Quit
Enter selection: """

    while True:
        selection = input(menu_message)

        if selection == 'q':
            break

        try:
            selection = int(selection)
            if selection < len(functions):
                val_for_x = int(input("Enter integer to compare: "))
                message = functions[selection](val_for_x)
                print(f"\nResult: '{message}'")
        except:
            print("\nInvalid input.")
        finally:
            print("--press a key to continue--")
            getch()

if __name__ == '__main__':
    main()
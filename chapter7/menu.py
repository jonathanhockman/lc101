class Menu():
    def __init__(self, options):
        self.menu_message = ""
        self.functions = []
        index = 1
        for label in options:
            try:
                fun = options[label]
                if callable(fun):
                    self.functions.append(fun)
                else:
                    raise Exception()
            except Exception:
                self.menu_message = "{}\n{}: {} -- invalid function".format(self.menu_message, index, label)
                self.functions.append(lambda : None)
            else:
                self.menu_message = "{}\n{}: {}".format(self.menu_message, index, label)
            finally:
                index += 1

        self.menu_message = "\n\nChoose One\n--------------{}\nq: Quit\n-> ".format(self.menu_message)

    def startMenu(self):
        while True:
            selection = input(self.menu_message)

            if selection == 'q':
                break

            try:
                selection = int(selection) - 1
                message = self.functions[selection]()
                print(f"\nResult: '{message}'")
            except:
                print("\nInvalid input.")
            finally:
                input("--press enter to continue--")

def run_example():
    def first_function():
        return "first function executed"

    def second_function():
        return "second function executed"

    options = {"first function": first_function, "second function": second_function}
    menu = Menu(options)
    menu.startMenu()

if __name__ == '__main__':
    run_example()
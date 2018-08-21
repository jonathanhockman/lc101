import py2

# py1 does not have a check for main so this
# code executes when it's imported
def print_names():
    print("py1's name is:", __name__)
    print("py2's name is:", py2.__name__)

def main():
    print_names()

if __name__ == '__main__':
    main()
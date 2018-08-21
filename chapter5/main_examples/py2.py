import py1

def print_names():
    print("py2's name is:", __name__)
    print("py1's name is:", py1.__name__)

if __name__ == '__main__':
    print_names()
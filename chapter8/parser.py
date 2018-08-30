import datetime

class custom_data(object):
    def __init__(self, **kargs):
        self.types = kargs

    def __call__(self, arg):
        setattr(arg, "types", self.types)
        return arg


@custom_data(name=str, age=int, birthday=datetime.date.fromisoformat)
class SimpleClass():
    def __init__(self):
        self.name = None
        self.age = None
        self.birthday = None

    def print_hello(self):
        print("Hello, my name is {}. I was born on {} which makes me {} years old".format(self.name, self.birthday, self.age))


class Parser(object):
    @staticmethod
    def parse(json_string, obj):
        key_pairs = {}

        key = None
        value = None

        # *****while loops*****
        str_len = len(json_string)

        index = 0
        while index < str_len:
            c = json_string[index]

            if c == "'" or c == '"':
                index += 1

                if key is None:
                    key = ""
                else:
                    value = ""

                while index < str_len:
                    c = json_string[index]

                    if c == "'" or c == '"':
                        if value is not None:
                            key_pairs[key] = value
                            key = None
                            value = None
                        break

                    if value is not None:
                        value += c
                    else:
                        key += c
                    index += 1
            index += 1

        # *****for loops****
        # found_start = False

        # for c in json_string:
        #     if not found_start and (c == "'" or c == '"'):
        #         found_start = True
        #         if key is None:
        #             key = ""
        #         else:
        #             value = ""
        #         continue

        #     if found_start:
        #         if c == "'" or c == '"':
        #             found_start = False

        #             if value is not None:
        #                 key_pairs[key] = value
        #                 key = None
        #                 value = None

        #             continue

        #         if value is None:
        #             key += c
        #         else:
        #             value += c

        new_obj = obj()
        for key in key_pairs:
            if key in obj.types:
                field_type = obj.types[key]
                value = key_pairs[key]
                try:
                    setattr(new_obj, key, field_type(value))
                except:
                    print("Invalid value ({}) passed for key ({}). Expected type {}".format(value, key, field_type))

        return new_obj

data = "'name' 'Michael Giacchinno' 'age' '50' 'birthday' '1967-10-10' 'other_key' 'some_val'"

o = Parser.parse(data, SimpleClass)
o.print_hello()



x = 0
while x < 5:
    print(x)
    x += 1

original = "this is a string"
index = 0
while original[index] != ' ' and index < len(original):
    index += 1
print("First space occurs at index", index)
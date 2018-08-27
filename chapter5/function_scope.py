def change_value(value):
    if type(value) == int:
        value *= 2
    elif type(value) == list:
        value.append(5)
    else:
        value = str(value)

print("return with int:", change_value(2))
my_int = 2
print("my_int before:", my_int)
change_value(my_int)
print("my_int after:", my_int)

print("return with list:", change_value([1,2,3,4]))
my_list = [1,2,3,4]
print("my_list before:", my_list)
change_value(my_list)
print("my_list after:", my_list)

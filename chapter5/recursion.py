# summation
def acc(times, result = 0):
    if times <= 0:
        return result
    return acc(times - 1, result + times)

print("Summation:", acc(10))

# square
def square(num, iteration = 0, result = 0):
    num = abs(num)

    if iteration == num:
        return result

    return square(num, iteration + 1, \
                  result + num)

print("Square:", square(10))

# exponent
def pwr(num, exp, result = None):
    if result is None:
        result = num if exp > 0 else 1

    if exp <= 1:
        return result

    result *= num
    return pwr(num, exp - 1, result)

print("Exponent:", pwr(4,2))

# lists within lists
def add_items(my_list):
    result = 0
    for item in my_list:
        if type(item) == list:
            result += add_items(item)
        else:
            result += item

    return result

print("Add items:", add_items([1, 2, [3, 4, 5], 6, [7, [8, 9], 10]]))
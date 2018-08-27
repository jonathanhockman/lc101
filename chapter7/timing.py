import random
import time

values = []

counter = 0
percent_invalid = .1
num_values = 10000
total_invalid = percent_invalid * num_values

while counter < num_values:
    # if we still have invalid left to add and random chance says to add
    # or if total values left to add equals total invalid left to add
    if (total_invalid > 0 and random.random() >= .5) or num_values - counter == total_invalid:
        total_invalid -= 1
        values.append("string")
    else:
        values.append(1)

    counter += 1

total_try = 0
for i in values:
    start = time.perf_counter_ns()
    try:
        i + 1
    except:
        i + "1"
    end = time.perf_counter_ns()
    total_try += end - start

total_if = 0
for i in values:
    start = time.perf_counter_ns()
    if i == 1:
    # if type(i) == int:
        i + 1
    else:
        i + "1"
    end = time.perf_counter_ns()
    total_if += end - start

print("\n\nTotal Values: {}\nTotal Invalid: {}%".format(len(values), percent_invalid * 100))
print("Average for Try/Except: {}".format(total_try/num_values))
print("Average for If/Else: {}".format(total_if/num_values))
print("\n")
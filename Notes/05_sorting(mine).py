# Sorting

#swap value

import random
import time

a = 1
b = 2

temp = a
a = b
b = temp

print(a, b)

# pythonic way
a, b = b, a

# make a random list of 100 number with values of 1 to 99
# use list comp
rando_list = [random.randrange(1, 100) for x in range(100)]
rando_list2 = rando_list[:]
print(rando_list)
start_time = 0
total_iterations = 0

for cur_pos in range(len(rando_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(rando_list)):
        if rando_list[scan_pos] < rando_list[min_pos]:
            min_pos = scan_pos
    rando_list[cur_pos], rando_list[min_pos] = rando_list[min_pos], rando_list[cur_pos]

print("Insertion sort time:", time.perf_counter() - start_time)
print(rando_list)
print("Insertion sort iterations:",total_iterations)

# INSERTION SORT
total_iterations = 0
start_time = 0

for key_pos in range(1, len(rando_list2)):
    key_val = rando_list2[key_pos]
    scan_pos = key_pos -1  # look to dancer
    while scan_pos >= 0 and rando_list2[scan_pos] > key_val:
        total_iterations += 1
        rando_list2[scan_pos + 1] = rando_list2[scan_pos]
        scan_pos -= 1
    rando_list2[scan_pos + 1] = key_val


print("Insertion sort time:", time.perf_counter() - start_time)
print(rando_list2)
print("Insertion sort iterations:", total_iterations)


# MORE WITH FUNCTIONS
print("Hello", end=" ") # uses an optional parameter which has a default value of "\n"
print("World", end="!\n")

def hello(name, time_of_day):
    print("Hello", name, "Good", time_of_day)

hello("Owen", "afternoon") # morning is the default value
hello("Wilson", time_of_day="afternoon")

# lambda functions (anonymous function on a single line)
double_me = lambda x: x * 2
# double_me is a function that returns the value x * 2
print(double_me(5))

sum_product = lambda a, b: [a + b, a * b]
print(sum_product(3, 2))

# Real world sorting with Python
my_list = [random.randrange(1, 100) for x in range(100)]

# sort method (change the list in place)
my_list.sort()  # default is to sort alphabetically or numerically small to large
print(my_list)

my_list.sort(reverse=True)
print(my_list)

# use a lambda as the key
my_2dlist = [[random.randrange(1, 100), random.randrange(1, 100)] for x in range (100)]
print(my_2dlist)

my_2dlist.sort()
print(my_2dlist)

my_2dlist.sort(key=lambda x: x[1])  # sorts by second item

my_2dlist.sort(key=lambda x: sum(x))
print(my_2dlist)

my_2dlist.sort(key=lambda x: abs(x[0] - x[1]), reverse = True)  # abs = absolute value
print(my_2dlist)

# sorted function (returns a new list)
new_list = sorted(my_2dlist, key= x: sum(x))
print(new_list)  # sorted by sum
print(my_2dlist)  # sorted still by difference
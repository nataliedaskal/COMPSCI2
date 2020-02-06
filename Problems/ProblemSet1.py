# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
# b) Make a list of even numbers from 20 to 40
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]

# 1 a
my_list = [x for x in range(101)]
print(my_list)

# 1 b
my_list2 = [x for x in range(20, 41) if x % 2 == 0]
print(my_list2)

# 1 c
my_list3 = [x ** 2 for x in range(101)]
print(my_list3)

# 1 d
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
my_positive = [x for x in my_list if x > 0]
print(my_positive)


# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list

from Problems.number_list import *
print(num_list[-5:])

# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
# Find and print the lowest number in num_list (1pt)
# Find and print the average of num_list (2pts)
# Remove the lowest number from num_list (2pt)
# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)

print(max(num_list))

print(min(num_list))

print(sum(num_list) / len(num_list))

num_list.sort()
num_list.pop(0)
print(num_list)

top_ten = num_list[-10:]
print(top_ten)

# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?

my_count = [num_list.count(x) for x in num_list]
print(num_list[my_count.index(max(my_count))])

# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't

for i in range(2, 10000):
    for num in num_list:
        if num % i == 0:
            num_list.remove(num)
prime_numbers = len(num_list)
print(prime_numbers)

# Find the number of palindromes
# Hint: This may be easier to do with strings

palindrome_count = 0
for x in range(len(num_list)):
    n = str(num_list[x])
    if n[0] == n[3] and n[2] == n[1]:
        palindrome_count += 1
print(palindrome_count)
# More on loops

# Basic FOR loop
for i in range(5, 51, 5):
    print(i, end=" ")
print()
# RANGE function (alternative for comprehension)
my_list = [x for x in range(100)]
print(my_list)

my_list = list(range(100)) #iterable
print(my_list)

# BREAK
for number in my_list:
    if number > 10:
        break
    print(number, end="yay")

print("End of loop")

# CONTINUE (skips to the end of the loop for that iteration)
for number in my_list:
    if number % 7 ==0:
        continue
    print(number, end=" ")

# FOR ELSE
for number in my_list:
    print(number, end=" ")
else:
    print("The loop completed naturally")




# Add me as a collaborator in Github
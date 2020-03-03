# Exceptions (use me sparingly please)

# Exception - condition that results in abnormal program
# Exception handling - what we actively do for an exception
# Catch - code that handles abnormal condition
# Throw/Raise - abnormal conditions throw or raise an exception
# Unhandled exceptions - program killers. Thrown... but not caught.


# Divide by zero error (ZeroDivisionError)
x = 0
y = 2

# print(y / x) DOESN'T WORK

try:
    print(y / x)
except:
    print("Invalid operation, divide by zero.")

# Conversion error (ValueError)

done = False

while not done:
    try:
        user_input = int(input("Enter a valid integer: "))
        done = True
    except:
        print("Number not valid, enter an integer")

# File opening (IOError, FileNotFoundError)

try:
    file = open("AliceInWonderland.txt")
except:
    print("File not found.")

# Use the built in error types for Python

try:
    my_file = open("myfile.txt")
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Fool! You can't divide by zero")
except ValueError:
    print("Invalid int conversion")
except:
    print("Unknown Error")

# Make an MPG calculator

try:
    miles = float(input("Miles travled: "))
    gallons = float(input("gallons used: "))
except ValueError:
    print("You entered an invalid number,")

try:
    print("MPG is", miles / gallons)
except:
    print("Your MPG is infinite!!!")
finally:
    print("Finally will always run regardless of exception or no exception")
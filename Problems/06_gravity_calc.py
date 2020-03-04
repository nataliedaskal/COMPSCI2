# Universal Gravity Calculator (12pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following
# (3pts) takes the inputs for mass 1, mass 2, and distance between the two objects (m1, m2, and r)
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (2pts) keeps asking for inputs until they are valid (see while loop from notes)
# (3pts) calculates the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.


done = False
while not done:
    G = 6.67e-11
    try:
        mass_1 = float(input("Mass 1: "))
        mass_2 = float(input("Mass 2: "))
        radius = float(input("Radius: "))
        F = G * (mass_1 * mass_2) / radius ** 2
        print("The force of gravity is", "{:.2e}".format(F), "N")
        done = True
    except ValueError:
        print("You entered an invalid number,")
    except ZeroDivisionError:
        print("You entered an invalid number,")
    except:
        print("You entered an invalid number,")




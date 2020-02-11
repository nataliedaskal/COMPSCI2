# Searching

# use forward slashes to go into folders and .. to go "up" a folder
file = open('resources/super_villains.txt', 'r')  # open to read
print(file)

for line in file:
    print(line)

file.close()

# .strip() method removes the extra characters at end of text
print("    Hello ".strip())
print("World\n".strip())
print("!")

# 'w' opens to write and overwrites the file
# 'a' opens to append
# 'r' reads
file = open('resources/super_villains.txt', 'a')
file.write("Lee the Merciless\n")
file.write('Rohan the Destroyer\n')
file.close()

# open to write can create a new file
file = open('resources/heroes.txt', 'w')
file.write('Owen the Valiant\n')
file.close()

# better way to open close a file (syntactic sugar)
# file automatically closes after execution of with
with open('resources/super_villains.txt') as f:
    for line in f:
        print(line.strip())


# .read() method just imports whole file as a string
with open('resources/super_villains.txt') as f:
    read_data = f.read()  # big string

print("\n\nRead method")  # not necessary
print(read_data)

# reading data into an array (list)
with open('resources/super_villains.txt', 'r') as f:
    villains = [x.strip().upper() for x in f]

print(villains)

# linear search (not very efficient but easy)

key = "Vidar the Manic".upper()

i = 0
while i < (len(villains) - 1) and key != villains [i]:
    i += 1

if i < len(villains):
    print("Found it at position", i)
else:
    print(key, "is not in the list")

# try to make this into a function

def linear_search(key, list):
    """
    :param key: what you are looking for
    :param list: where you are looking
    :return: True or false -- bool did you find it?
    """
    i = 0
    while i < (len(my_list) -1) and key.upper() != my_list[i]:
        i += 1

    if i < len(villains) - 1:
        print("Found", key, "at position", i)
        return True
    else:
        print(key, "not found.")
        return False


# binary search

key = "THEODORA THE WICKED"
lower_bound = 0
upper_bound = len(villains)
found = False

while lower_bound <= upper_bound and not found:
    middle_pos = (upper_bound + lower_bound) // 2
    if villains[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villains[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True

if found:
    print(key, "was found at position", middle_pos)
else:
    print(key, "not found.")
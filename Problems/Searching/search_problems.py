'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

my_list = []
with open('Dictionary.txt') as f:
    word_list = [x.strip() for x in f]

for word in word_list:
    my_list.append(len(word))
max_letters = max(my_list)
for i in word_list:
    if len(i) == 28:
        print("The longest word in the dictionary is", i + ", which has", max_letters, "letters.")


# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"

alice_in_wonderland = open("AliceInWonderLand.txt")
word_list = []
for word in alice_in_wonderland:
    words = split_line(word.strip())
    for word in words:
        word_list.append(word)
lens_words = []
for word in word_list:
    lens_words.append(len(word))

print("There are", len(word_list), "words in Alice in Wonderland. The average word is", sum(lens_words)/len(lens_words), "letters.")

# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?

alice_number = 0
for i in range(len(word_list)):
    if word_list[i].upper() == "ALICE":
        alice_number += 1
print("Alice appears", alice_number, "times.")


# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"


# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

cheshire_count = 0
cat_count = 0
cheshirecat_count = 0
for i in range(len(word_list)):
    if word_list[i].upper() == "CHESHIRE":
        cheshire_count += 1
    if word_list[i].upper() == "CAT":
        cat_count += 1
    if word_list[i].upper() == "CHESHIRE" and word_list[i + 1].upper() == "CAT":
        cheshirecat_count += 1

print("Cheshire occurs", cheshire_count, "times.")
print("Cat occurs", cat_count, "times.")
print("Cheshire cat occurs", cheshirecat_count, "times.")

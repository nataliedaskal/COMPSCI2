import random

my_list = ["CALIFORNIA", "IOWA", "MAINE", "COLORADO", "OREGON", "GEORGIA"]

#1
random.shuffle(my_list)
my_word = my_list.pop()
print(my_word, my_list)

#2
my_word = my_list.pop(random.randrange(len(my_list)))
print(my_word, my_list)

used_letters = ["A", "S", "T"]
my_word = "GEORGIA"

# make a list of words
# pick a random word
done = False
while not done:
    # print the gallows
    # print the word with blanks or letters
    guess = input("Pick a letter")
    # check to see if already selected
    # check if in word (if it isn't, you lose a life)
    # check for a win or loss


correct = True
for letter in my_word:
    if letter in used_letters:
        print(letter, end=" ")
    else:
        print("_", end=" ")
        correct = False

print(correct)

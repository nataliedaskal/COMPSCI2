import random

gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]

print(gallows[4])

my_list = ["CALIFORNIA", "IOWA", "MAINE", "COLORADO", "OREGON", "GEORGIA"]
word = my_list[random.randrange(6)]
word_letters = []
guessed_letters = []
wrong_guesses = 0
your_level = 0
done = False
for i in range(len(word)):
    print("__ ", end="")

while not done:
    print(gallows[your_level])
    correct_guesses = 0
    letters_remaining = len(word)
    guess = input("\nPick a letter ")
    if guess.lower() in guessed_letters:
        print('You already guessed that, pick a different letter.')
        if guess.lower() not in guessed_letters:
            guessed_letters.append(guess)
    if guess.lower() in word.lower():
        if guess.lower() not in guessed_letters:
            correct_guesses += 1
        word_letters.append(guess.lower())
    else:
        wrong_guesses += 1
        your_level += 1
    for letter in word.lower():
        if letter in word_letters:
            print(letter + " ", end="")
            letters_remaining -= 1
        else:
            print("__", end=" ")
    if letters_remaining == 0:
        done = True
        print("You won! I challenge you to play again!")
    if wrong_guesses >= 6:
        print("You lost. I challenge you to play again!")
        done = True

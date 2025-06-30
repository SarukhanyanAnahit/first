import random

def game_state(hangman_pics, missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print("\nused letters:", ' '.join(missed_letters))

    blanks = ''
    for letter in secret_word:
        if letter in correct_letters:
            blanks += letter + ' '
        else:
            blanks += '_ '
    print("\nword:", blanks.strip())

def all_letters_found(word, correct_letters):
    for letter in word:
        if letter not in correct_letters:
            return False
    return True

def play_hangman():
    words = ['python', 'program', 'hangman', 'developer', 'keyboard', 'village', 'teacher']
    secret_word = random.choice(words)
    missed_letters = []
    correct_letters = []
    hangman = [
        '''
         +---+
         |   |
             |
             |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
             |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        ========='''
    ]

    max_wrong = len(hangman) - 1
    game_over = False

    while not game_over:
        game_state(hangman, missed_letters, correct_letters, secret_word)
        guess = input("\ninput letter (a-z): ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("input only 1 letter։")
            continue
        if guess in missed_letters or guess in correct_letters:
            print("you used it։")
            continue
        if guess in secret_word:
            correct_letters.append(guess)
            if all_letters_found(secret_word, correct_letters):
                print(f"\nyou win! word was- {secret_word}")
                game_over = True
        else:
            missed_letters.append(guess)
            if len(missed_letters) == max_wrong:
                game_state(hangman, missed_letters, correct_letters, secret_word)
                print(f"\nyou loosed word is {secret_word}")
                game_over = True

if __name__ == "__main__":
    play_hangman()

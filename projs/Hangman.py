import random

def game_state(hangman, missed, correct, guess):
    print(hangman[len(missed)])
    print("\nused letters:", ' '.join(missed))

    blanks = ''
    for letter in guess:
        if letter in correct:
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
    try:
        words = ['someone', 'maybe', 'one', 'forever', 'toshiba', 'anyone']
        in_mind = random.choice(words)
        missed = []
        correct = []
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
            game_state(hangman, missed, correct, in_mind)
            guess = input("\ninput letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                print("input only 1 letter։")
                continue
            if guess in missed or guess in correct:
                print("you used it։")
                continue
            if guess in in_mind:
                correct.append(guess)
                if all_letters_found(in_mind, correct):
                    print(f"\nyou win! word was- {in_mind}")
                    game_over = True
            else:
                missed.append(guess)
                if len(missed) == max_wrong:
                    game_state(hangman, missed, correct, in_mind)
                    print(f"\nyou loosed word is {in_mind}")
                    game_over = True
    except:
        print(f"\n error occurred")

if __name__ == "__main__":
    play_hangman()

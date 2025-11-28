import random
def word_list():
    return ['python', 'java', 'kotlin', 'javascript']


def get_word(words):
    return random.choice(words).upper()

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")







def display_hangman(tries):
    stages = [
        # 0 tries left – full hangman
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        """,
        # 1 try left
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |
        """,
        # 2 tries left
        """
           --------
           |      |
           |      O
           |     /|\\
           |
           |
        """,
        # 3 tries left
        """
           --------
           |      |
           |      O
           |     /|
           |
           |
        """,
        # 4 tries left
        """
           --------
           |      |
           |      O
           |      |
           |
           |
        """,
        # 5 tries left
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        # 6 tries left – empty gallows (start)
        """
           --------
           |      |
           |
           |
           |
           |
        """
    ]
    return stages[tries]



def main():
    words = word_list()          # get list once
    word = get_word(words)       # pick random word
    play(word)

    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word(words)
        play(word)


if __name__ == "__main__":
    main() 
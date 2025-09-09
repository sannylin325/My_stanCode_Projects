"""
File: hangman.py
Name: Sanny Lin
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Hangman game with steps limit
    1. Generate a random word by random_word() = word
    2. Let user input an alphabet "input_ch"
        * if "input_ch" is not alphabet or not single, print "Illegal format."
    3. If "input_ch" is in the word:
       Move the value of "ans" into "old_ans", and add new value into "ans":
        (1) for word[i] is not "input_ch": add the value of the same index of "old_ans" into "ans"
        (2) for word[i] is "input_ch": add "input_ch" into "ans"
    4. If ans == word: the user win the game
    5. If the user is run out of steps before ans == word: the user lose the game
    """
    # set variables
    word = random_word()
    step = N_TURNS
    old_ans = "-" * len(word)
    ans = "-" * len(word)

    # start guessing
    while True:
        # check current answer & remaining steps
        print("The word looks like " + str(ans))
        print("You have " + str(step) + " wrong guesses left.")

        # input guess
        input_ch = (input("Your guess: ")).upper()  # case-insensitive
        # check if input_ch is a single alphabet
        while not input_ch.isalpha() or len(input_ch) != 1:
            print("Illegal format.")
            input_ch = (input("Your guess: ")).upper()

        # check if input_ch is in the word
        if word.find(input_ch) == -1:  # not in the word
            step -= 1
            print("There is no " + input_ch + "'s in the world.")
            # renew hangman image
            hangman(step)
        else:
            old_ans = ans
            ans = ""
            for i in range(len(word)):  # renew "ans"
                if word[i] != input_ch:
                    ans += old_ans[i]
                else:
                    ans += input_ch
            print("You are correct!")

        # check if lose or win
        if step == 0:
            print("You are completely hung :(")
            break
        elif ans == word:
            print("You win!!")
            break
    # print the correct answer at last
    print("The word was: " + word)

def random_word():
    # return a word below in random
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def hangman(step):
    # draw hangman's image by the residual step
    print(" _________")
    print(" |    |")
    if step == 6:
        for i in range(6):
            print(" |")
    elif step == 5:
        print(" |    O")
        for i in range(5):
            print(" |")
    elif step == 4:
        print(" |    O")
        for i in range(2):
            print(" |    |")
        for i in range(3):
            print(" |")
    elif step == 3:
        print(" |    O")
        print(" |   /|")
        print(" |    |")
        for i in range(3):
            print(" |")
    elif step == 2:
        print(" |    O")
        print(" |   /|\\")
        print(" |    |")
        for i in range(3):
            print(" |")
    elif step == 1:
        print(" |    O")
        print(" |   /|\\")
        print(" |    |")
        print(" |   /")
        for i in range(2):
            print(" |")
    elif step == 0:
        print(" |    O")
        print(" |   /|\\")
        print(" |    |")
        print(" |   / \\")
        for i in range(2):
            print(" |")
    print("-----")


if __name__ == '__main__':
    main()

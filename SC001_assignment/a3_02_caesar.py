"""
File: caesar.py
Name: Sanny Lin
------------------------------
(Instructions by stanCode)
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Find the index in "new_alpha" of each character in the inputted sentence,
    add the character with corresponding index in "ALPHABET" to "ans" in order,
    at last, return and print the result "ans".
    """
    print("The deciphered string is: " + decipher())


def decipher():
    """
    District in 2 parts:
    1. Get the new sequence of ALPHABET = "new_alpha":
       the last "n" numbers of ALPHABET will move to the front of ALPHABET
    2. Decipher the inputted sentence
        (1) Find the index in "new_alpha" of each character in the inputted sentence
        (2) Add the character with corresponding index in "ALPHABET" to "ans" in order
    :return ans: str, which is the inputted sentence after deciphered
    """
    # get the new sequence of ALPHABET = new_alpha
    n = int(input("Secret number: "))
    new_alpha = ALPHABET[len(ALPHABET)-n:] + ALPHABET[:len(ALPHABET)-n]

    # decipher the inputted sentence
    s = input("What's the ciphered string? ").upper()  # case-insensitive
    ans = ""
    for i in range(len(s)):
        j = new_alpha.find(s[i])
        if j != -1:  # is alphabet
            ans += ALPHABET[j]
        else:  # j == -1, means not in ALPHABET, maybe exists space or landmark
            ans += s[i]
    return ans


if __name__ == '__main__':
    main()

"""
File: similarity.py (extension)
Name: Sanny Lin
----------------------------
(Instructions by stanCode)
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Compare the short_sequence with the long_sequence,
    find the most match piece in long_sequence.
    """
    print("The best match is " + match())


def match():
    """
    1. Cut the long_sequence into short_digit sizes at the beginning of index[i]
       ("i" is a loop from 0 to (long_digit-short_digit+1))
    2. Compare short_sequence with each cut_sequences
        (1) if short_sequence[j] == cut_sequence[j]: get 1 score
        (2) if score > high_score:
            reassign high_score
            reassign ans = cut_sequence
    :return ans: str, which is the most match cut_sequence from long_sequence
    """
    # input DNA sequences (case-insensitive)
    long_sequence = input("Please give me a DNA sequence to search: ").upper()
    short_sequence = input("What DNA sequence would you like to match? ").upper()

    # digits of the DNA sequences
    long_digit = len(long_sequence)
    short_digit = len(short_sequence)

    # set variables
    score, high_score = 0, 0
    ans = ""

    # cut long_sequence into short_digit sizes at the beginning of index[i]
    # the above "i" is a loop from 0 to (long_digit-short_digit+1)
    for i in range(0, long_digit - short_digit + 1):
        cut_sequence = long_sequence[i:(i + short_digit)]
        score = 0  # clear the old score value before comparing new cut_sequence
        # compare short_sequence with each cut_sequences
        for j in range(short_digit):
            if short_sequence[j] == cut_sequence[j]:
                score += 1
        if score > high_score:
            high_score = score
            ans = cut_sequence
    return ans


if __name__ == '__main__':
    main()

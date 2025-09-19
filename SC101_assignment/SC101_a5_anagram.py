"""
File: anagram.py
Name: Sanny Lin
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    Find the anagrams for the inputted word. Calculate time used for searching.
    """
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')

    while True:
        # check input word
        s = input(f'Find anagrams for: ')
        if s == EXIT:
            break

        # prepare list & set
        anagrams_list = []        # anagrams answer list
        s_list = [True] * len(s)  # the alphabet in s is used or not
        used_set = set()          # all current_s been used in recursion

        # prepare dictionary
        sub_dict = read_dictionary(s)

        # start to search
        print(f'Searching...')
        start = time.time()
        ####################
        find_anagrams(s, s_list, used_set, '', anagrams_list, sub_dict)
        ####################
        end = time.time()
        print(f'{len(anagrams_list)} anagrams: {anagrams_list}')
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')
        print('----------------------------------')


def read_dictionary(s):
    """
    ---helper of read_dictionary()---
    :param s: str, the inputted word
    :return: set, key=word that startswith alphabet in s & len(word) == len(s)
    """
    sub_dict = set()  # use set will be faster than dict, thanks Jerry !!
    with open(FILE, 'r') as f:
        for line in f:
            token = line.split()[0]
            # only pick the tokens that startswith alphabet in s & len(token) == len(s)
            if token[0] in s and len(token) == len(s):  # len(token) == len(s)  >> thanks Yi-Ru <3
                sub_dict.add(token)
    return sub_dict


def find_anagrams(s, s_list, used_set, current_s, anagrams_list, sub_dict):
    """
    ---helper of find_anagrams(s)---
    :param s: str, the inputted word
    :param s_list: list, boolean, if alphabet in s is un-used = True, used = False
    :param used_set: set, all current_s been used in recursion
    :param current_s: str, which is checking now
    :param anagrams_list: list, collecting anagrams
    :param sub_dict: set, return by read_dictionary_helper(s)
    :return: list, the anagrams of s
    """
    if len(current_s) <= len(s):
        if len(current_s) == len(s):
            if current_s in sub_dict:
                anagrams_list.append(current_s)
                print(f'Found: {current_s}')
                print(f'Searching...')
        else:
            for i in range(len(s)):  # alphabet in s may repeat, use index to differ which alphabet
                if s_list[i]:
                    # choose
                    current_s += s[i]
                    # explore
                    if current_s not in used_set:  # early stopping: if current_s appeared before
                        s_list[i] = False  # used
                        used_set.add(current_s)
                        find_anagrams(s, s_list, used_set, current_s, anagrams_list, sub_dict)
                        # un-choose
                        s_list[i] = True  # pop >> un-used
                    current_s = current_s[:-1]


if __name__ == '__main__':
    main()

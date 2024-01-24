"""
File: rocket.py
Name: Sanny Lin
-----------------------
(Instructions by stanCode)
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.
"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    function: print the whole rocket(district in 6 parts)
    """
    head()  # the sharp corner of the rocket
    belt()  # "+" and "=" between head and the main body of rocket
    upper()  # the upper half of the main body
    lower()  # the lower half of the main body
    belt()  # "+" and "=" between head and the main body of rocket
    head()  # the sharp corner of the rocket


def head():
    """
    function: print the sharp corner of the rocket
    method: district in 3 parts
    (1) empty space (2) /  (3) \
    """
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(" ", end="")
        for j in range(i+1):
            print("/", end="")
        for j in range(i+1):
            print("\\", end="")  # show backslash
        print("")


def belt():
    """
    function: print one line between head and the main body of rocket
    method: district in 3 parts
    (1) +  (2) =  (3) +
    """
    print("+", end="")
    for i in range(SIZE*2):
        print("=", end="")
    print("+", end="")
    print("")


def upper():
    """
    function: print upper half of the main body of rocket
    method: district in 6 parts
    (1) |  (2) .  (3) /  (4) \  (5) .  (6) |
    """
    for i in range(SIZE):
        print("|", end="")
        for j in range(SIZE-i-1):
            print(".", end="")
        for j in range(i+1):
            print("/", end="")
            print("\\", end="")  # show backslash
        for j in range(SIZE-i-1):
            print(".", end="")
        print("|", end="")
        print("")


def lower():
    """
    function: print lower half of the main body of rocket
    method: district in 6 parts
    (1) |  (2) .  (3) \  (4) /  (5) .  (6) |
    """
    for i in range(SIZE):
        print("|", end="")
        for j in range(i):
            print(".", end="")
        for j in range(SIZE-i):
            print("\\", end="")  # show backslash
            print("/", end="")
        for j in range(i):
            print(".", end="")
        print("|", end="")
        print("")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()

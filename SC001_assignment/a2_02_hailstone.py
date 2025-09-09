"""
File: hailstone.py
Name: Sanny Lin
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    If input number "n" is odd, make "n" reassign as "3n+1",
    and if "n" is even, halve "n" as "1/2n".
    Repeat above actions until "n" becomes 1.
    Count how many steps it took to reach 1.
    * Premise: The inputted number is not 1.
    """
    print("This program computes Hailstone sequences.")
    print("")
    n = int(input("Enter a number: "))
    step = 0
    while n != 1:
        if n % 2 == 1:
            nn = n * 3 + 1
            print(str(n)+" is odd, so I make 3n+1: " + str(nn))
        else:
            nn = n / 2
            print(str(n) + " is even, so I take half: " + str(nn))
        n = nn
        step += 1
    print("It took " + str(step) + " steps to reach 1.")


if __name__ == "__main__":
    main()

"""
File: extension2_number_checker.py
Name: Sanny Lin
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""


# the number used to leave this program
EXIT = -100


def main():
    """
    Halve the inputted number "n", get the number "nq".
    Divided "n" by all the integers <= "nq",
    only if "n" is divisible that we add the "nq" into the answer.
    Compare the answer and "n":
    (1) if equals, it's a perfect number;
    (2) if bigger, it's an abundant number;
    (3) if smaller, it's a dificient number.
    """
    print("Welcome to the number checker!")
    while True:
        n = int(input("n: "))
        if n == EXIT:
            print("Have a good one!")
            break
        # find and sum all the factor of the integer
        else:
            nq = int(n / 2)
            ans = 0
            while True:
                if nq == 0:
                    break
                elif n % nq == 0:
                    ans += nq
                nq -= 1
        # print result
        if ans == n:
            print(str(n) + " is a perfect number.")
        elif ans > n:
            print(str(n) + " is an abundant number.")
        else:
            print(str(n) + " is a deficient number.")


if __name__ == '__main__':
    main()

"""
File: extension3_triangular_checker.py
Name: Sanny Lin
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""


# the number used to leave this program
EXIT = -100


def main():
    """
    Halve the inputted number "tn" then +1, get the number "n".
    Compare tn and "n*(n+1)/2":
    (1) if equals, it's a triangular number;
    (2) if not equals, it's not a triangular number.
    """
    print("Welcome to the triangular number checker!")
    while True:
        tn = int(input("n: "))
        if tn == EXIT:
            print("Have a good one!")
            break
        # test if "tn" is a triangular number
        else:
            n = int(tn / 2 + 1)
            while True:
                if n != 1:
                    if n * (n + 1) / 2 != tn:
                        n -= 1
                    else:
                        break
                else:
                    break
            if n != 1:
                print(str(tn) + " is a triangular number.")
            else:
                print(str(tn) + " is not a triangular number.")


if __name__ == '__main__':
    main()

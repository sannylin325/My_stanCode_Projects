"""
File: extension4_narcissistic_checker.py
Name: Sanny Lin
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""


# the number used to leave this program
EXIT = -100


def main():
    """
    Divided inputted number "n" by 10, repeat until n<1, then count the digit of "n".
    Repeat divided "n" by 10,
    the extra numbers will be the number of each digit of "n".
    Sum: the raise of each digit number to the power of the number of digits.
    Compare "n" and sum: if equals, it's a narcissistic number, otherwise, not.
    """
    print("Welcome to the narcissistic number checker!")
    while True:
        n = int(input("n: "))
        if n == EXIT:
            print("Have a good one!")
            break
        # test if "n" is a narcissistic number
        else:
            # count the digit of "n"
            dn = n
            d = 0
            while True:
                if dn >= 1:
                    d += 1
                    dn /= 10
                else:
                    break
            # get the number of each digit of "n"
            # raise each digit number to the power of the number of digits
            # sum the numbers above
            sn = n
            n_sum = 0
            while True:
                if sn >= 1:
                    nn = sn % 10
                    n_sum += nn ** d
                    sn //= 10
                else:
                    break
            # print results
            if n_sum == n:
                print(str(n) + " is a narcissistic number.")
            else:
                print(str(n) + " is not a narcissistic number.")


if __name__ == '__main__':
    main()

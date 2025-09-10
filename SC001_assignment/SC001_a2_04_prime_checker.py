"""
File: prime_checker.py
Name: Sanny Lin
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

import math


# the number used to leave this program
EXIT = -100


def main():
	"""
	Root the inputted number "n", get the number "nq".
	Divided "n" by all the integers smaller than "nq", until "n" is divisible.
	If the last "nq" is 1, "n" is a prime number; otherwise, not.
	"""
	print("Welcome to the prime checker!")
	while True:
		n = int(input("n: "))
		if n == EXIT:
			print("Have a good one!")
			break
		else:
			nq = int(math.sqrt(n))
			while n % nq != 0:
				nq -= 1
				if n % nq == 0:
					break
			if nq == 1:
				print(str(n) + " is a prime number.")
			else:
				print(str(n) + " is not a prime number.")


if __name__ == "__main__":
	main()

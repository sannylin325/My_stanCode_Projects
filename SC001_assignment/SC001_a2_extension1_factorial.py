"""
File: extension1_factioral.py
Name: Sanny Lin
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""


# the number used to leave this program
EXIT = -100


def main():
	"""
	Program: Multiply all the integers smaller than the inputted number "n".
	"""
	print("Welcome to stanCode factorial master!")
	while True:
		n = int(input("Give me a number, and I will list the answer of factorial: "))
		ans = 1
		if n == EXIT:
			print("------ See ya! ------")
			break
		while True:
			if n != 1:
				ans *= n
				n -= 1
			else:
				print("Answer: " + str(ans))
				break


if __name__ == '__main__':
	main()

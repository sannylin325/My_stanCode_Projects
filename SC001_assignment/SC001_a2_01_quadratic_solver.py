"""
File: quadratic_solver.py
Name: Sanny Lin
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Equation: a*x^2+b*x+c
	Calculate the roots of the above equation.
	Premise: a != 0
	"""
	# input numbers
	print("stanCode Quadratic Solver!")
	a = int(input("Enter a: "))
	while a == 0:
		print('\"a" should not be 0')
		a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	root = int(b * b - 4 * a * c)

	# list quadratic function & print result
	if root > 0:
		x1 = (-b + math.sqrt(root)) / (2 * a)
		x2 = (-b - math.sqrt(root)) / (2 * a)
		print("Two roots: " + str(x1) + "," + str(x2))
	elif root == 0:
		print("One root: " + str((-b)/(2*a)))
	else:
		print("No real roots")


if __name__ == "__main__":
	main()

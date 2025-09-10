"""
File: coin_flip_runs.py
Name: Sanny Lin
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	1. r.randint(0, 1): 1 -> H, 0 -> T
	2. check: 'True' if consecutive, 'False' if break consecutive.
	3. When run==num, stop and print. (only add new roll to string if run < num)
	# break at second same of last run
	"""
	print("Let's flip a coin!")
	num = int(input('Number of runs: '))

	# set variables
	string = ''
	run = 0
	old = -1
	check = False

	# start flipping5
	while True:
		coin = r.choice(['H', 'T'])
		string += coin
		if old == coin and not check:  # consecutive
			check = True
			run += 1
		if old != coin and check:  # break consecutive
			check = False
		old = coin
		if run == num:
			break
	print(string)


if __name__ == "__main__":
	main()

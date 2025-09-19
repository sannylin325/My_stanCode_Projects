"""
File: interactive.py
Name: Sanny Lin
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
"""

import util
import submission


def main():
	weights = {}
	with open('weights', 'r', encoding='utf-8') as f:
		for line in f:
			key, value = line.strip().split()  # no strip() also work, but should not be split(' ')
			weights[key] = float(value)
	util.interactivePrompt(submission.extractWordFeatures, weights)


if __name__ == '__main__':
	main()

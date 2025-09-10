"""
File: boggle_TrieNode.py
Name: Sanny Lin
----------------------------------------
BOGGLE game
Get ORDER ** 2 inputted letters,
array each letter with the neighboring letters,
and sum how many words was found at the end.
*** use class TrieNode to accelerate
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ORDER = 4


class TrieNode:
	def __init__(self):
		self.children = {}
		self.end = False


class Trie:
	def __init__(self):
		self.start = TrieNode()

	def insert(self, word):
		cur = self.start
		for ch in word:
			if ch not in cur.children:
				cur.children[ch] = TrieNode()
			cur = cur.children[ch]
		cur.end = True


def main():
	"""
	BOGGLE game
	Get ORDER ** 2 inputted letters,
	array each letter with the neighboring letters,
	and sum how many words was found at the end.
	"""
	node = read_dictionary().start
	board = get_board()
	if not board or len(board[0]) != ORDER:  # input with illegal format
		return
	ans = []
	start = time.time()
	####################
	for row in range(len(board)):
		for col in range(len(board[0])):
			find_boggle(node, board, '', row, col, [], ans)
	####################
	end = time.time()
	print(f'There are {len(ans)} words in total.')
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	trie = Trie()
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			trie.insert(line)
	return trie


def get_board():
	"""
	:return: list[list], with letters in legal format
	"""
	board = []
	check = True
	for i in range(ORDER):
		print(f'(Please enter {ORDER} letters separated by space.)')
		letters = input(f'{i+1} row of letters: ').lower().strip().split()
		if len(letters) != ORDER:
			print('Illegal format.')
			break
		for letter in letters:
			if len(letter) != 1 or not letter.isalpha():
				print('Illegal format.')
				check = False
		if not check:
			break
		else:
			board.append(letters)
	return board


def find_boggle(node, board, current_s, row, col, used, ans):
	# conditions for not execute find_boggle()
	if row < 0 or row == len(board) or col < 0 or col == len(board[0]):
		return
	if (row, col) in used or board[row][col] not in node.children:
		return

	# choose
	current_s += board[row][col]
	used.append((row, col))
	node = node.children[board[row][col]]
	# base case
	if len(current_s) >= 4 and node.end and current_s not in ans:
		print(f'Found "{current_s}"')
		ans.append(current_s)
	# explore
	for i in range(-1, 2):
		for j in range(-1, 2):
			find_boggle(node, board, current_s, row+i, col+j, used, ans)
	# un-choose
	used.pop()


if __name__ == '__main__':
	main()

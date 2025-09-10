"""
File: weather_master.py
Name: Sanny Lin
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# the number used to leave this program
EXIT = -100


def main():
	"""
	Let user input temperature datas.
	If the first data is not "EXIT" number:
	Assign need variables, and compare the new data with basic data.
	Calculate the maximum, minimum, average, and cold days of the datas.
	"""
	print('stanCode \"Weather Master 4.0"!')
	# variables about maximum, minimum, average and cold days
	t_max, t_min = -float('inf'), float('inf')
	t_sum, count = 0, 0
	cold = 0
	# input data (or leave)
	while True:
		t = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
		if t == EXIT:
			break
		else:
			# statistics for average
			t_sum += t
			count += 1
			# calculate cold days
			if t < 16:
				cold += 1
			# reassign maximum and minimum
			if t > t_max:
				t_max = t
			if t < t_min:
				t_min = t
	# print results
	if not count:
		print("No temperatures were entered.")
	else:
		print("Highest temperature = " + str(t_max))
		print("Lowest temperature = " + str(t_min))
		print("Average = " + str(t_sum / count))
		print(str(cold) + " cold day(s)")


if __name__ == "__main__":
	main()

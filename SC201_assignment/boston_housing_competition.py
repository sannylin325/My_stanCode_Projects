"""
File: boston_housing_competition.py
Name: Sanny Lin
--------------------------------
This file demonstrates how to analyze boston
housing dataset. Students will upload their 
results to kaggle.com and compete with people
in class!

You are allowed to use pandas, sklearn, or build the
model from scratch! Go data scientists!
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing, linear_model, model_selection, metrics
import numpy as np


def main():
	train_data = pd.read_csv('boston_housing/train.csv')  # check: no missing value and no category(all digital)
	# extract true label
	y = train_data.medv
	# extract features & add constant
	features = ['crim', 'zn', 'chas', 'nox', 'rm', 'dis', 'rad', 'tax', 'black', 'lstat']
	x = pd.DataFrame(train_data[features])
	x['constant'] = [1] * len(y)

	# validation set for testing overvitting
	x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.3, random_state=0)

	# normalize
	normalizer = preprocessing.MinMaxScaler()
	x_train = normalizer.fit_transform(x_train)
	x_test = normalizer.transform(x_test)

	# polynomial
	poly_phi_extractor = preprocessing.PolynomialFeatures(degree=2)
	x_train_poly = poly_phi_extractor.fit_transform(x_train)
	x_test_poly = poly_phi_extractor.transform(x_test)

	# linear regression
	h = linear_model.LinearRegression()
	regressor = h.fit(x_train_poly, y_train)
	predictions = regressor.predict(x_test_poly)
	print(sum(regressor.predict(x_train_poly)) / len(y_train))
	print(sum(regressor.predict(x_test_poly)) / len(y_test))
	# count RMS error
	print(metrics.mean_squared_error(predictions, y_test)**0.5)

	# submit prediction to Kaggle
	test_data = pd.read_csv('boston_housing/test.csv')  # check: no missing value and no category(all digital)
	test_x = pd.DataFrame(test_data[features])
	test_x['constant'] = [1] * len(test_x)
	test_test = normalizer.transform(test_x)
	test_test_poly = poly_phi_extractor.transform(test_test)
	predictions = regressor.predict(test_test_poly)
	# #  count RMS error
	# print(metrics.mean_squared_error(predictions, y)**0.5)
	out_file(predictions, 'boston_housing_ver3.csv')


def out_file(predictions, filename):
	"""
	: param predictions: numpy.array, a list-like data structure that stores 0's and 1's
	: param filename: str, the filename you would like to write the results to
	"""
	print('\n===============================================')
	print(f'Writing predictions to --> {filename}')
	# get ID in test.csv
	test_data = pd.read_csv('boston_housing/test.csv')
	ids = test_data.ID
	# start writing predictions
	with open(filename, 'w') as out:
		out.write('ID,medv\n')
		for i in range(len(ids)):
			out.write(str(ids[i]) + ',' + str(predictions[i]) + '\n')
	print('===============================================')


if __name__ == '__main__':
	main()

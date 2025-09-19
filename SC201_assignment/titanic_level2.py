"""
File: titanic_level2.py
Name: Sanny Lin
----------------------------------
This file builds a machine learning algorithm by pandas and sklearn libraries.
We'll be using pandas to read in dataset, store data into a DataFrame,
standardize the data by sklearn, and finally train the model and
test it on kaggle website. Hyper-parameters tuning are not required due to its
high level of abstraction, which makes it easier to use but less flexible.
You should find a good model that surpasses 77% test accuracy on kaggle.
"""

import math
import pandas as pd
from sklearn import preprocessing, linear_model

TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'

# Global variable
nan_cache = {}  # Cache for test set missing data


def data_preprocess(filename, mode='Train', training_data=None):
	"""
	:param filename: str, the filename to be read into pandas
	:param mode: str, indicating the mode we are using (either Train or Test)
	:param training_data: DataFrame, a 2D data structure that looks like an excel worksheet
						  (You will only use this when mode == 'Test')
	:return: Tuple(data, labels), if the mode is 'Train'; or return data, if the mode is 'Test'
	"""
	data = pd.read_csv(filename)
	labels = None
	################################
	# abandon features ('PassengerId', 'Name', 'Ticket', 'Cabin')
	data.pop('PassengerId')
	data.pop('Name')
	data.pop('Ticket')
	data.pop('Cabin')
	# drop NaN
	if mode == 'Train':
		data.dropna(inplace=True)
	# digital category
	data.Sex.replace(['female', 'male'], [0, 1], inplace=True)
	data.Embarked.replace(['S', 'C', 'Q'], [0, 1, 2], inplace=True)
	# filling missing value
	if mode == 'Train':
		age_average = round(sum(data.Age) / len(data.Age), 3)
		fare_average = round(sum(data.Fare) / len(data.Fare), 3)
		# nan_cache: global variable, cache data for test set (Age and Fare)
		nan_cache['Age'] = age_average
		nan_cache['Fare'] = fare_average
	else:
		data.Age.fillna(nan_cache['Age'], inplace=True)
		data.Fare.fillna(nan_cache['Fare'], inplace=True)
	# extract True labels
	if mode == "Train":
		labels = data.pop('Survived')
	################################
	if mode == 'Train':
		return data, labels
	elif mode == 'Test':
		return data


def one_hot_encoding(data, feature):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param feature: str, the column name of interest
	:return data: DataFrame, remove the feature column and add its one-hot encoding features
	"""
	############################
	# One hot encoding for Sex
	if feature == 'Sex':
		data['Sex_0'] = 0
		data.loc[data.Sex == 0, 'Sex_0'] = 1
		data['Sex_1'] = 0
		data.loc[data.Sex == 1, 'Sex_1'] = 1
	# One hot encoding for Pclass
	if feature == 'Pclass':
		data['Pclass_0'] = 0
		data.loc[data.Pclass == 1, 'Pclass_0'] = 1
		data['Pclass_1'] = 0
		data.loc[data.Pclass == 2, 'Pclass_1'] = 1
		data['Pclass_2'] = 0
		data.loc[data.Pclass == 3, 'Pclass_2'] = 1
	# One hot encoding for Embarked
	if feature == 'Embarked':
		data['Embarked_0'] = 0
		data.loc[data.Embarked == 0, 'Embarked_0'] = 1
		data['Embarked_1'] = 0
		data.loc[data.Embarked == 1, 'Embarked_1'] = 1
		data['Embarked_2'] = 0
		data.loc[data.Embarked == 2, 'Embarked_2'] = 1
	# pop original feature
	data.pop(feature)
	############################
	return data


def standardization(data, mode='Train'):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param mode: str, indicating the mode we are using (either Train or Test)
	:return data: DataFrame, standardized features
	"""
	standardizer = preprocessing.StandardScaler()
	data = standardizer.fit_transform(data)
	return data


def main():
	"""
	You should call data_preprocess(), one_hot_encoding(), and
	standardization() on your training data. You should see ~80% accuracy on degree1;
	~83% on degree2; ~87% on degree3.
	Please write down the accuracy for degree1, 2, and 3 respectively below
	(rounding accuracies to 8 decimal places)
	"""
	# # Train data
	# data cleaning
	train_data = data_preprocess(TRAIN_FILE, mode='Train')
	y = train_data[1]
	train_data = train_data[0]
	# one_hot_encoding
	train_data = one_hot_encoding(train_data, 'Sex')
	train_data = one_hot_encoding(train_data, 'Pclass')
	train_data = one_hot_encoding(train_data, 'Embarked')
	# standardization
	standardizer = preprocessing.StandardScaler()
	train_data = standardizer.fit_transform(train_data)

	# # linear regression with polynomial features
	# Train data
	poly_phi_extractor = preprocessing.PolynomialFeatures(degree=2)
	train_data_poly = poly_phi_extractor.fit_transform(train_data)
	h = linear_model.LogisticRegression(max_iter=10000)
	classifier = h.fit(train_data_poly, y)
	print('Training Acc: ', classifier.score(train_data_poly, y))


if __name__ == '__main__':
	main()

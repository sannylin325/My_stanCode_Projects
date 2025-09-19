"""
File: titanic_deep_nn.py
Name: Sanny Lin
-----------------------------
This file demonstrates how to create a deep
neural network (5 layers NN) to train our
titanic data, using the constants and global variables.
-----------------------------
X.shape = (N0, m)
Y.shape = (1, m)
W1.shape -> (N0, N1)
W2.shape -> (N1, N2)
W3.shape -> (N2, N3)
W4.shape -> (N3, N4)
W5.shape -> (N4, N5)
B1.shape -> (N1, 1)
B2.shape -> (N2, 1)
B3.shape -> (N3, 1)
B4.shape -> (N4, 1)
B5.shape -> (N5, 1)
"""

from collections import defaultdict
import numpy as np

# Constants
TRAIN = 'titanic_data/train.csv'     # This is the filename of interest
NUM_EPOCHS = 40000                   # This constant controls the total number of epochs
ALPHA = 0.01                         # This constant controls the learning rate α
L = 5                                # This number controls the number of layers in NN
NODES = {                            # This Dict[str: int] controls the number of nodes in each layer
    'N0': 6,
    'N1': 5,
    'N2': 4,
    'N3': 3,
    'N4': 2,
    'N5': 1
}


def main():
    """
    Print out the final accuracy of the deep neural network.
    """
    X_train, Y = data_preprocessing()
    _, m = X_train.shape
    # print('Y.shape', Y.shape)
    # print('X.shape', X_train.shape)
    # ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    X = normalize(X_train)
    ####################################
    weights, biases = neural_network(X, Y)
    ####################################
    k = {}
    a = {'A0': X}
    for i in range(1, L+1):
        k[f'K{i}'] = np.dot(weights[f'W{i}'].T, a[f'A{i-1}']) + biases[f'B{i}']
        a[f'A{i}'] = np.maximum(0, k[f'K{i}'])
    predictions = np.where(k[f'K{L}'] > 0, 1, 0)
    acc = np.equal(predictions, Y)
    num_acc = np.sum(acc)
    print('Training Acc: ', num_acc / m)


def normalize(X):
    """
    :param X: numpy_array, the dimension is (num_phi, m)
    :return: numpy_array, the values are normalized, where the dimension is still (num_phi, m)
    """
    min_array = np.min(X, axis=1, keepdims=True)
    max_array = np.max(X, axis=1, keepdims=True)
    return (X - min_array) / (max_array - min_array)


def neural_network(X, Y):
    """
    :param X: numpy_array, the array holding all the training data
    :param Y: numpy_array, the array holding all the ture labels in X
    :return (weights, bias): the tuple of parameters of this deep NN
             weights: Dict[str, float], key is 'W1', 'W2', ...
                                        value is the corresponding float
             bias: Dict[str, float], key is 'B1', 'B2', ...
                                     value is the corresponding float
    """
    np.random.seed(1)
    # Initialize all the weights and biases
    weights = {}
    biases = {}
    #####################################
    for i in range(1, L+1):
        weights[f'W{i}'] = np.random.rand(NODES[f'N{i-1}'], NODES[f'N{i}']) - 0.5
        biases[f'B{i}'] = np.random.rand(NODES[f'N{i}'], 1) - 0.5
    #####################################

    k, a = {}, {'A0': X}
    d_w, d_b, d_k, d_a = {}, {}, {}, {}
    _, m = X.shape
    # training
    for epoch in range(NUM_EPOCHS):
        # # Forward Pass
        # ReLu
        for i in range(1, L):
            k[f'K{i}'] = np.dot(weights[f'W{i}'].T, a[f'A{i-1}']) + biases[f'B{i}']
            a[f'A{i}'] = np.maximum(0, k[f'K{i}'])
        # sigmoid
        k[f'K{L}'] = np.dot(weights[f'W{L}'].T, a[f'A{L-1}']) + biases[f'B{L}']
        H = 1 / (1+np.exp(-k[f'K{L}']))
        J = (1/m) * (np.sum(-(Y*np.log(H)+(1-Y)*np.log(1-H))))

        # # Backward Pass
        d_k[f'dK{L}'] = (1/m) * (np.sum(H-Y, axis=0, keepdims=True))
        d_w[f'dW{L}'] = np.dot(a[f'A{L-1}'], d_k[f'dK{L}'].T)
        d_b[f'dB{L}'] = np.sum(d_k[f'dK{L}'], axis=1, keepdims=True)
        # module
        for i in range(L-1, 0, -1):
            d_a[f'dA{i}'] = np.dot(weights[f'W{i+1}'], d_k[f'dK{i+1}'])
            d_k[f'dK{i}'] = d_a[f'dA{i}'] * np.where(k[f'K{i}'] > 0, 1, 0)
            d_w[f'dW{i}'] = np.dot(a[f'A{i-1}'], d_k[f'dK{i}'].T)
            d_b[f'dB{i}'] = np.sum(d_k[f'dK{i}'], axis=1, keepdims=True)

        # # Updates all the weights and biases
        for i in range(1, L+1):
            weights[f'W{i}'] = weights[f'W{i}'] - ALPHA * d_w[f'dW{i}']
            biases[f'B{i}'] = biases[f'B{i}'] - ALPHA * d_b[f'dB{i}']

    return weights, biases


def data_preprocessing(mode='train'):
    """
    :param mode: str, indicating if it's training mode or testing mode
    :return: Tuple(numpy_array, numpy_array), the first one is X, the other one is Y
    """
    data_lst = []
    label_lst = []
    first_data = True
    if mode == 'train':
        with open(TRAIN, 'r') as f:
            for line in f:
                data = line.split(',')
                # ['0PassengerId', '1Survived', '2Pclass', '3Last Name', '4First Name', '5Sex', '6Age',
                #  '7SibSp', '8Parch', '9Ticket', '10Fare', '11Cabin', '12Embarked']
                if first_data:
                    first_data = False
                    continue
                if not data[6]:
                    continue
                label = [int(data[1])]
                if data[5] == 'male':
                    sex = 1
                else:
                    sex = 0
                # ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
                passenger_lst = [int(data[2]), sex, float(data[6]), int(data[7]), int(data[8]), float(data[10])]
                data_lst.append(passenger_lst)
                label_lst.append(label)
    else:
        pass
    return np.array(data_lst).T, np.array(label_lst).T


if __name__ == '__main__':
    main()

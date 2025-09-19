"""
File: submission.py
Name: Sanny Lin
"""

#!/usr/bin/python

import math
import random
from collections import defaultdict
from util import *
from typing import Any, Dict, Tuple, List, Callable

FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]


############################################################
# Milestone 3a: feature extraction

def extractWordFeatures(x: str) -> FeatureVector:
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    d = defaultdict(int)
    for word in x.split():
        d[word] += 1
    return d

############################################################
# Milestone 4: Sentiment Classification

def learnPredictor(trainExamples: List[Tuple[Any, int]], validationExamples: List[Tuple[Any, int]],
                   featureExtractor: Callable[[str], FeatureVector], numEpochs: int, alpha: float) -> WeightVector:
    """
    Given |trainExamples| and |validationExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of epochs to
    train |numEpochs|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement gradient descent.
    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and validationExamples
    to see how you're doing as you learn after each epoch. Note also that the 
    identity function may be used as the featureExtractor function during testing.
    """
    weights = defaultdict(float)  # the weight vector
    for i in range(numEpochs):
        for j in range(len(trainExamples)):
            x = featureExtractor(trainExamples[j][0])
            y = 0 if trainExamples[j][1] == -1 else trainExamples[j][1]
            h = 1/(1+math.exp(-dotProduct(weights, x)))
            increment(weights, -alpha*(h-y), x)

        def predictor(x):
            ki = dotProduct(weights, featureExtractor(x))
            return 1 if ki >= 0 else -1

        print(f'Training error: ({i} epoch): {evaluatePredictor(trainExamples, predictor)}')
        print(f'Validation error: ({i} epoch): {evaluatePredictor(validationExamples, predictor)}')

    return weights


############################################################
# Milestone 5a: generate test case

def generateDataset(numExamples: int, weights: WeightVector) -> List[Example]:
    """
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    """
    random.seed(42)

    def generateExample() -> Tuple[Dict[str, int], int]:
        """
        Return a single example (phi(x), y).
        phi(x) should be a dict whose keys are a subset of the keys in weights
        and values are their word occurrence.
        y should be 1 or -1 as classified by the weight vector.
        Note that the weight vector can be arbitrary during testing.
        """
        # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
        phi = defaultdict(int)
        for word in random.sample(weights.keys(), random.randint(1, len(weights))):
            phi[word] += 1
        y = 1 if dotProduct(weights, phi) >= 0 else -1
        return phi, y

    return [generateExample() for _ in range(numExamples)]


############################################################
# Milestone 5b: character features

def extractCharacterFeatures(n: int) -> Callable[[str], FeatureVector]:
    """
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces mapped to their n-gram counts.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    """
    def extract(x: str) -> Dict[str, int]:
        d = defaultdict(int)
        x = x.replace(' ', '')
        for i in range(len(x)-n+1):
            d[x[i:i+n]] += 1
        return d

    return extract

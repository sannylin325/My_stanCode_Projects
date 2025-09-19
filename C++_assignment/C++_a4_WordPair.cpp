/**
 * Files: WordPair.cpp
 * Author: Sanny Lin
 * 
 * The WordPair class represents a pair of words.
 * It stores two words: the first word and the second word.
 * The class provides methods to retrieve the first and second words, 
 * as well as a string representation of the WordPair object.
 * 
 * The WordPairList class represents a list of word pairs.
 * It takes an array of words as input and generates all possible pairs of words from the given array.
 * The class provides a method to calculate 
 * the number of matching pairs where the first and second words are the same.
 */

#include<iostream>
#include<list>
using namespace std;

class WordPair{
private:
	string first;
	string second;

public:
	// constructor
	/** Constructs a WordPair object */
	WordPair(string w1, string w2){
		first = w1;
		second = w2;
	}

	// methods
	/** @return: the first word of this WordPair object*/
	string getFirst(){
		return first;
	}

	/** @return: the second word of this WordPair object*/
	string getSecond(){
		return second;
	}
};


class WordPairList{
private:
	list<WordPair> allPairs;  // the list of word pairs, initialized by the constructor

public:
	// constructor
	/** 
	 * Constructs a WordPairList object. 
	 * Precondition: words.length>=2 
	 * @param words: the array of words from which the pairs are generated
	 * @param n: the amount of word in words
	 */
	WordPairList(string words[], int n){
		for (int i=0; i<n-1; i++){
			for (int j=i+1; j<n; j++){
				WordPair pair = WordPair(words[i], words[j]);
				allPairs.push_back(pair);
			}
		}
	}

	// methods
	/** 
     * Calculates the number of matching pairs which first and second words are the same.
     * @return: the number of matching pairs
	 */
	int numMatches(){
		int count = 0;
		for (WordPair pair: allPairs){
			if (pair.getFirst()==pair.getSecond()) count ++;
		}
		return count;
	}
};

// main
int main(){
	const int n = 5;  
	// the number n to be in [] shall be const
	string words[n] = {"the", "red", "fox", "the", "red"};
	
	WordPairList obj(words, n);
	cout << obj.numMatches() << endl;

	return 0;
}
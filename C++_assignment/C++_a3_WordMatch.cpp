/**
 * File: WordMatch.cpp
 * Author: Sanny Lin
 * 
 * The WordMatch class represents a word matching game. 
 * It allows scoring and comparison of word guesses
 * based on a secret word provided during object construction.
 */

#include <iostream>
using namespace std;

class WordMatch {
private:
	string secret;	// the answer word

public:
	// constructor
	/**
     * Constructs a WordMatch object with the given secret string of lowercase letters.
     * @param word: the answer word of the game
     */
	WordMatch(string word){
		secret = word;
	}

	// methods
	/**
     * Returns a score of the guess.
     * Precondition: 0 < guess.length() <= secret.length
     * @param guess: the word guessed by the player
     * @return: the score of the guess
     */
	int scoreGuess(string guess){
		int count = 0;
		for (int i=0; i<secret.length()-guess.length()+1; i++){
			if (secret.substr(i, guess.length())==guess) count ++;
		}
		return count * guess.length() * guess.length();
	}

	/**
     * Returns the better of two guesses. 
     * If the scores of guess1 and guess2 are the same, return the one with higher alphabetical order.
     * @param guess1: the first guess to be compared
     * @param guess2: the second guess to be compared
     * @return: the better of the two guesses
     */
	string findBetterGuess(string guess1, string guess2){
		int score1, score2;
		score1 = scoreGuess(guess1);
		score2 = scoreGuess(guess2);
		if (score1 > score2) return guess1;
		else if (score2 > score1) return guess2;
		else {
			if (guess1 > guess2) return guess1;  // compare directly!
			else return guess2;
			}
		}
};

// main
int main(){
	// WordMatch game1("mississippi");
	// cout << game1.scoreGuess("i") << endl;
	// cout << game1.scoreGuess("iss") << endl;
	// cout << game1.scoreGuess("issipp") << endl;
	// cout << game1.scoreGuess("mississippi") << endl;

	// WordMatch game2("aaaabb");
	// cout << game2.scoreGuess("a") << endl;
	// cout << game2.scoreGuess("aa") << endl;
	// cout << game2.scoreGuess("aaa") << endl;
	// cout << game2.scoreGuess("aabb") << endl;
	// cout << game2.scoreGuess("c") << endl;

	WordMatch game("concatenation");
	cout << (game.scoreGuess("ten")) << endl;
	cout << (game.scoreGuess("nation")) << endl;
	cout << (game.findBetterGuess("ten", "nation")) << endl;
	cout << (game.scoreGuess("con")) << endl;
	cout << (game.scoreGuess("cat")) << endl;
	cout << (game.findBetterGuess("cat", "con")) << endl;
	return 0;
}
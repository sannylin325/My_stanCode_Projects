/**
 * Files: HiddenWord.cpp
 * Author: Sanny Lin
 *
 * The HiddenWord class represents a hidden word puzzle game.
 * It allows players to guess the hidden word and provides a hint based on their guesses.
 */

#include <iostream>
using namespace std;

class HiddenWord {
private:
	string hiddenWord;	// the answer word

public:
	// Constructor
    /**
     * Creates a HiddenWord object with the given word as the puzzle.
     * @param puzzle: the answer word to be guessed
     */
	HiddenWord(string answer){
		hiddenWord = answer;
	}

	// methods
	/**
     * Provides a hint based on the player's guess.
     * (1) If guessed letter is in the correct position, it will be revealed.
     * (2) If guessed letter is in the word but in the wrong position, it will be represented as '+'.
     * (3) If guessed letter is not in the word, it will be represented as '*'.
     *
     * @param guess: the player's guess
     * @return: a string containing the hint
     */
	string getHint(string guess){
		string hint = "";
		for (int i=0; i<hiddenWord.length(); i++){
			if (hiddenWord[i] == guess[i]) hint += hiddenWord[i];
			else if (hiddenWord.find(guess[i]) != string::npos) hint += "+";
			else hint += "*";
		}
		return hint;
	}
};

// main
int main(){
	HiddenWord puzzle("HARPS");
	cout << "hint: " << puzzle.getHint("AAAAA") << endl;
	cout << "hint: " << puzzle.getHint("HELLO") << endl;
	cout << "hint: " << puzzle.getHint("HEART") << endl;
	cout << "hint: " << puzzle.getHint("HARMS") << endl;
	cout << "hint: " << puzzle.getHint("HARPS") << endl;
	return 0;
}
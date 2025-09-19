/**
 * Files: hangman.cpp
 * Author: Sanny Lin
 *
 * This program plays the hangman game. 
 * User will see a dashed word, and try to figure the un-dashed word out by inputting one character each round.
 * If the input character is correct, the updated word will be shown.
 * Players have N_TURNS chances to try and win this game.
 */

#include <iostream>
#include <cstdlib>
#include <time.h>

using namespace std;

const int LIVES = 7;  // the maximum turns/chances of the game

/** Get the answer word in random.*/
string getAnswerWord(){
	srand(time(NULL));  // srand: giving unsigned seed, or random number will be same
	int num = rand() % 9;

	if (num==0) return "NOTORIOUS";
	else if (num==1) return "GLAMOROUS";
	else if (num==2) return "CAUTIOUS";
	else if (num==3) return "DEMOCRACY";
	else if (num==4) return "BOYCOTT";
	else if (num==5) return "ENTHUSIASTIC";
	else if (num==6) return "HOSPITALITY";
	else if (num==7) return "BUNDLE";
	else return "REFUND";
}

/** Update current status (how the word loos like).
 * @param progress: last status
 * @param guess: new guess
 * @return: the current status
 */
string getNowGuess(string ans, string nowGuess, char guess){
	string newNowGuess = "";
	for (int i=0; i<ans.length(); i++){
		if (nowGuess == "") newNowGuess += "-";
		else if (guess == ans[i]) newNowGuess += ans[i];
		else newNowGuess += nowGuess[i];
	}
	return newNowGuess;
}

// main
int main(){
	// variables
	string ans = getAnswerWord();
	int lives = LIVES;
	string input = "-";
	string nowGuess = getNowGuess(ans, "", input[0]);

	// game start
	while (true){
		cout << "The word looks like " << nowGuess << endl;
		cout << "You have " << lives << " wrong guesses left." << endl;

		// get guess input & check format(length>1 or with number is illegal)
		while (true){
			cout << "Your guess: ";
			cin >> input;	
			if (input.length()!=1 or !isalpha(input[0])){
				cout << "Illegal format." << endl;
			}
			else break;
		}

		// check guess wrong or right
		char guess = input[0];
		guess = toupper(guess);
		if (ans.find(guess)!=-1){
			nowGuess = getNowGuess(ans, nowGuess, guess);
			cout << "You are correct!" << endl;
		}
		else {
			lives --;
			cout << "There is no " << guess << "'s in the word." << endl;
		}

		// check if win or lose
		if (nowGuess==ans){
			cout << "You win!!" << endl;
			break;
		}
		else if (!lives){
			cout << "You are completely hung :(" << endl;
			break;
		}
	}
	cout << "The word was: " << ans << endl;
	return 0;
}
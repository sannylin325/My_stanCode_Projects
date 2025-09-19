/**
 * Files: similarity.cpp
 * Author: Sanny Lin
 *
 * This program will take in two DNA sequences given by the user.
 * It will compare a short DNA sequence with sub-sequences of a long DNA sequence.
 * The approach used in this task is the same as what people are doing in the bio industry.
 */

#include <iostream>
using namespace std;

/** Make string to upper case.*/
string myToUpper(string origin){
	string upperCase = "";
	for (int i=0; i<origin.length(); i++){
		upperCase += toupper(origin[i]);
	}
	return upperCase;
}

/** Find best match DNA .
 * (Extraxt longDNA part with length of shortDNA, calculate and compare the score of each part.)
 */
string bestMatch(string longDNA, string shortDNA){
	longDNA = myToUpper(longDNA);
	shortDNA = myToUpper(shortDNA);
	string bestDNA = "";
	int bestCount = 0;
	for (int i=0; i<longDNA.length()-shortDNA.length()+1; i++){
		string subDNA = longDNA.substr(i, shortDNA.length());
		int count = 0;
		for (int j=0; j<shortDNA.length(); j++){
			if (subDNA[j] == shortDNA[j]) count++;
		}
		if (count > bestCount){
			bestDNA = subDNA;
			bestCount = count;
		}
	}
	return bestDNA;
}

// main
int main(){
	string longDNA, shortDNA;
	cout << "Please give me a DNA sequence to search: ";
	cin >> longDNA;
	cout << "What DNA sequence would you like to match? ";
	cin >> shortDNA;
	cout << "The best match is " << bestMatch(longDNA, shortDNA) << endl;
	return 0;
}
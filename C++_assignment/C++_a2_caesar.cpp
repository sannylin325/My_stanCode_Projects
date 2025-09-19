/**
 * Files: caesar.cpp
 * Author: Sanny Lin
 *
 * This program demonstrates the idea of the Caesar cipher.
 * Users will be asked to input a number to produce the shifted ALPHABET as the cipher table. 
 * After that, any strings typed in will be encrypted.
 */

#include <iostream>
using namespace std;

const string ALPHABET= "ABCDEFGHIJKLMNOPQRSTUVWXYZ";  // alphabets in usual order

/** Make string to upper case.*/
string myToUpper(string origin){
	string upperCase = "";
	for (int i=0; i<origin.length(); i++){
		upperCase += toupper(origin[i]);
	}
	return upperCase;
}

/** Decipher user's input.*/
string decipher(string ciphered, int secret){
	ciphered = myToUpper(ciphered);
	string newAlpha = ALPHABET.substr(ALPHABET.length()-secret, secret) + ALPHABET.substr(0, ALPHABET.length()-secret);
	string decipheredWord = "";

	for (int i=0; i<ciphered.length(); i++){
		if (isalpha(ciphered[i])){
			int index = newAlpha.find(ciphered[i]);
			decipheredWord += ALPHABET[index];
		}
		else {  // ex: number or punctuation mark
			decipheredWord += ciphered[i];
		}
	}
	return decipheredWord;
}

// main
int main(){
	int secret;
	char ciphered[50];  // cin.getline(var name, size) -> use char array
	// string ciphered;  // getline(cin, var name) -> use string
	cout << "Secret number: ";
	cin >> secret;
	cin.ignore();  // when cin int then string: clear inputted int first (or will cause program end when input string)
	cout << "What's the ciphered string? ";
	cin.getline(ciphered, sizeof(ciphered));  // or space will stop cin
	// getline(cin, ciphered);  // another way
	cout << "The deciphered string is: " << decipher(ciphered, secret) << endl;
	return 0;
}
/**
 * Files: rocket.cpp
 * Author: Sanny Lin
 *
 * This program will implement a console program that draws a rocket.
 * The size of the rocket is determined by a constant defined as SIZE at the top of the file.
 */

#include <iostream>
using namespace std;

const int SIZE = 3;  // the size of the rocket

// print the header part of the rocket
void head(){
	for (int i=0; i<SIZE; i++){
		for (int j=0; j<SIZE-i; j++){
			cout << " ";
		}
		for (int j=0; j<i+1; j++){
			cout << "/";
		}
		for (int j=0; j<i+1; j++){
			cout << "\\";
		}
		cout << endl;
	}
}

// print the belt part of the rocket
void belt(){
	cout << "+";
	for (int i=0; i<SIZE*2; i++){
		cout << "=";
	}
	cout << "+" << endl;
}

// print the upper part of the rocket
void upper(){
	for (int i=0; i<SIZE; i++){
		cout << "|";
		for (int j=0; j<SIZE-i-1; j++){
			cout << ".";
		}
		for (int j=0; j<i+1; j++){
			cout << "/";
		}
		for (int j=0; j<i+1; j++){
			cout << "\\";
		}
		for (int j=0; j<SIZE-i-1; j++){
			cout << ".";
		}
		cout << "|" << endl;
	}
}

// print the lower part of the rocket
void lower(){
	for (int i=0; i<SIZE; i++){
		cout << "|";
		for (int j=0; j<i; j++){
			cout << ".";
		}
		for (int j=0; j<SIZE-i; j++){
			cout << "\\";
		}
		for (int j=0; j<SIZE-i; j++){
			cout << "/";
		}
		for (int j=0; j<i; j++){
			cout << ".";
		}
		cout << "|" << endl;
	}
}

// main
int main(){
	head();
	belt();
	upper();
	lower();
	belt();
	head();
	return 0;
}
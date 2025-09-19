/**
 * Files: primeChecker.cpp
 * Author: Sanny Lin
 *
 * This program asks the user for input and checks if the input is a
 * prime number or not. The program ends when the user enters the EXIT number.
 */

#include <iostream>
#include <cmath>
using namespace std;

const int EXIT = -1;  // exit number (to end the program)

int main(){
	int num;  // the input number

	cout << "Welcome to Prime Checker!" << endl;
	while (true){
		cout << "Number: (or " << EXIT << " to quit): ";
		cin >> num;
		if (num==EXIT){
			cout << "Have a good one!" << endl;
			break;
		}
		else if (num == 1){
			cout << "Please enter a number that is bigger than 1." << endl;
		}
		
		// check if num is prime
		int checkNum = 2;
		bool isPrime = true;  // true -> false if any factor been find
		while (checkNum <= sqrt(num)){  // any factor will be smaller than sqrt(num)
			if (!(num % checkNum)){
				isPrime = false;  // factor exist
				break;
			}
			checkNum++;
		}

		// print result
		if (num != 1){
			if (isPrime) cout << "It's prime!" << endl;
			else cout << "Not prime!" << endl;
		}
	}
	return 0;
}
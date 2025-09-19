/**
 * Files: narcissisticChecker.cpp
 * Author: Sanny Lin
 *
 * This program asks the user for input and checks if the input is a
 * narcissistic number or not.
 *
 * A positive integer is called a narcissistic number if it is equal to
 * the sum of its own digits each raised to the power of the number of digits.
 *
 * The program ends when the user enters the EXIT number.
 */

#include <iostream>
#include <cmath>
using namespace std;

const int EXIT = -100;  // exit number (to end the program)

int main(){
	cout << "Welcome to narcissistic checker!" << endl;
	while (true){
		int num;
		cout << "Number (or " << EXIT << " to quit): ";
		cin >> num;
		if (num==EXIT) break;

		// (1) count digit
		int digit = 0;
		int temp = num;
		while (temp){
			digit ++;
			temp /= 10;
		}

		// (2) sum: each digit raised to the power of the number of digits
		int total = 0;
		temp = num;
		while (temp){
			total += pow(temp%10, digit);
			cout << pow(temp%10, digit) << endl;
			temp /= 10;
			cout << total << "," << temp << endl;
		}

		// check
		if (total==num) cout << num << " is a narcissistic number." << endl;
		else cout << num << " is not a narcissistic number." << endl;
	}
	cout << "Have a good one!"<< endl;
	return 0;
}
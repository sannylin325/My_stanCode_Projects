/**
 * Files: quadratic.cpp
 * Author: Sanny Lin
 *
 * This C++ program implements a console program that asks 
 * the user to enter three inputs (a, b, and c)
 * in order to compute the roots of the quadratic equation: ax^2 + bx + c = 0.
 */

#include <iostream>
#include <cmath>
using namespace std;

int main(){
	// variables
	int a, b, c;

	// introduction & get user input
	cout << "stanCode Quadratic Solver!" << endl;
	cout << "Enter a: ";  // no << at end
	cin >> a;  // no >> at end
	cout << "Enter b: ";
	cin >> b;
	cout << "Enter c: ";
	cin >> c;

	// calculate
	double discriminant = b*b-4*a*c;

	if (discriminant > 0){  // two roots
		cout << "Two real roots: ";
		cout << (-b+sqrt(discriminant)) / (2*a) << ",";
		cout << (-b-sqrt(discriminant)) / (2*a) << endl;
	}
	else if (discriminant == 0){  // one root
		cout << "One real root: " << -b / (2*a) << endl;
	}
	else{  // no real roots
		cout << "No real roots." << endl;
	}
	return 0;
}
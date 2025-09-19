/**
 * Files: weatherMaster.cpp
 * Author: Sanny Lin
 *
 * This Java program implements a console program 
 * that asks weather data from the user to compute
 * the average, highest, lowest, and cold days among the inputs.
 */

#include <iostream>
#include <limits.h>
using namespace std;

const int EXIT = -1;  // exit number (to end the program)
const int COLD = 16;  // definition of cold day (temperature < 16)

int main(){
	// variables
	int temp, maximum=INT_MIN, minimum=INT_MAX, total=0, count=0, cold=0;

	// introduction and get user input(datas)
	cout << "stanCode \"Weather Master\" 4.0!" << endl;
	while (true){
		cout << "Next temperature: (or " << EXIT << " to quit)? ";
		cin >> temp;
		if (temp==EXIT) break;

		count ++;
		total += temp;
		if (temp > maximum) maximum = temp;
		if (temp < minimum) minimum = temp;
		if (temp < COLD) cold ++;
	}

	if (!count){  // no data
		cout << "No temperatures were entered." << endl;
	}
	else {
		cout << "Highest temperature: " << maximum << endl;
		cout << "Lowest temperature: " << minimum << endl;
		cout << "Average: " << (double)total/count << endl;
		cout << "Cold day(s): " << cold << " day(s)" << endl;
	}
	return 0;
}
/**
 * Files: FrogSimulation.cpp
 * Author: Sanny Lin
 *
 * The FrogSimulation class represents a simulation of a frog attempting to reach a goal.
 * It keeps track of the goal distance, the maximum number of hops allowed, and the current
 * count of hops taken by the frog.
 */

#include <iostream>
#include <cstdlib>
using namespace std;

class FrogSimulation {
private:
	int goalDistance;	// distance from the starting position to the goal(in inches)
	int maxHops;		// the maximum number of hops allowed to reach the goal

public:
	// constructor
	/** Create FrogSimulation with dist and numHops.
     * @param dist: distance from the starting position to the goal(in inches)
     * @param numHops: the maximum number of hops allowed to reach the goal
     */
	FrogSimulation(int dist, int numHops){
		goalDistance = dist;
		maxHops = numHops;
	}

	// methods
	/**
     * The frog will hop randomly in the range from -5 to 20 inches.
     * @return: the distance to be moved when the frog hops(in inches)
     */
	int hopDistances(){
		return rand() % 10 - 4;
	}

	/**
     * Simulates a frog attempting to reach the goal.
     * @return: true if the frog successfully reached or passed the goal, false otherwise
     */
	bool simulate(){
		int location = 0;
		int step = 0;
		while (true){
			location += hopDistances();
			step ++;
			if (location >= goalDistance){
				return true;
			}
			else if (location < 0){
				return false;
			}
			else if (step >= maxHops){
				return false;
			}
		}
	}

	/**
     * Runs num times of simulations and returns the proportion of simulations
     * in which the frog successfully reached or passed the goal.
     * @param num: the number of simulations to run
     * @return: the proportion of simulations in which the frog successfully reached or passed the goal
     */
	double runSimulations(int num){
		double total = 0;
		int success = 0;
		for (int i=0; i<num; i++){
			if (simulate()) success ++;
			total ++;
		}
		return success/total;
	}
};

// main
int main(){
	FrogSimulation myFrog(24, 5);
	cout << myFrog.runSimulations(400) << endl;
	cout << myFrog.runSimulations(400) << endl;
	cout << myFrog.runSimulations(400) << endl;
	cout << myFrog.runSimulations(400) << endl;
	cout << myFrog.runSimulations(400) << endl;
	return 0;
}
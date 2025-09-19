import java.util.*;

public class FrogSimulation{
	// iVar
	private int goalDistance;
	private int maxHops;

	// constructor
	public FrogSimulation(int dist, int numHops){
		goalDistance = dist;
		maxHops = numHops;
	}

	// methods
	private int hopDistance(){
		Random myRandom = new Random();
		return myRandom.nextInt(25)-5;
	}

	public boolean simulate(){
		int locate = 0;
		int steps = 0;
		while (true){
			locate = locate + hopDistance();
			steps ++;
			if (locate>goalDistance){
				return true;
			}
			else if (locate<0){
				return false;
			}
			else if (steps>=maxHops){
				return false;
			}
		}
	}

	public double runSimulations(int num){
		double numTrue = 0;
		double total = 0;
		for (int i=0; i<num; i++){
			boolean result = simulate();
			if (result==true){
				numTrue ++;
			}
			total ++;
		}
		return numTrue/total;
	}

	// main
	public static void main(String[] args){
		FrogSimulation myFrog = new FrogSimulation(24, 5);
		System.out.println(myFrog.runSimulations(400));
		System.out.println(myFrog.runSimulations(400));
		System.out.println(myFrog.runSimulations(400));
		System.out.println(myFrog.runSimulations(400));
		System.out.println(myFrog.runSimulations(400));
	}
}
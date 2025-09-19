import java.util.Scanner;

public class WeatherMaster{
	public static final int EXIT = -1;

	public static void main(String[] args){
		int maximum = Integer.MIN_VALUE;
		int minimum = Integer.MAX_VALUE;
		double total = 0;
		int count = 0;
		int cold = 0;
		int input = EXIT-1;
		Scanner myScanner = new Scanner(System.in);

		System.out.println("stanCode \"Weather Master 4.0\"!");
		while (input != EXIT){
			System.out.print("Next Temperature: (or " + EXIT + " to quit)? ");
			input = myScanner.nextInt();
			if (input != EXIT){
				if (input > maximum){
					maximum = input;
				}
				if (input < minimum){
					minimum = input;
				}
				if (input < 16){
					cold ++;
				}
				total = total + input;
				count ++;
				}
			}
		
		if (count != 0){
			System.out.println("Highest temperature = " + maximum);
			System.out.println("Lowest temperature = " + minimum);
			System.out.println("Average: " + total/count);
			System.out.println(cold + " cold day(s)");
		}	
		else {
			System.out.println("No temperatures were entered.");
		}	
	}
}
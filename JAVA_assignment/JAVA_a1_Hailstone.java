import java.util.Scanner;

public class Hailstone{
	public static void main(String[] args){
		Scanner myScanner = new Scanner(System.in);
		int count = 0;

		System.out.println("This program computes Hailstone sequences.");
		System.out.println("");
		System.out.print("Enter a number: ");
		int n = myScanner.nextInt();

		while (n != 1){
			if (n%2 == 1){
				System.out.println(n + " is odd, so I make 3n+1: " + (3*n+1));
				n = 3*n + 1;
			}
			else {
				System.out.println(n + " is even, so I take half: " + (n/2));
				n = n/2;
			}
			count ++;
		}

		System.out.println("It took " + count + " step(s) to reach 1.");
	}
}
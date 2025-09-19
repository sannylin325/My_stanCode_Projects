import java.util.Scanner;

public class NarcissisticChecker{
	public static final int EXIT = -100;

	public static void main(String[] args){
		Scanner myScanner = new Scanner(System.in);
		int n = EXIT-1;

		System.out.println("Welcome to the narcissistic number checker!");
		while (n != EXIT){
			System.out.print("n: ");
			n = myScanner.nextInt();
			if (n != EXIT){
				int nn = n;
				int index = 0;
				while (nn>0){
					index ++;
					nn = nn/10;
				}
				nn = n;
				int total = 0;
				while (nn>0){
					total = total + (int)Math.pow(nn%10, index);
					nn = nn/10;
				}
				if (total == n){
					System.out.println(n + " is a narcissistic number.");
				}
				else {
					System.out.println(n + " is not a narcissistic number.");
				}
			}
			else {
				System.out.println("Have a good one!");
			}
		}
	}
}
import java.util.Scanner;

public class PrimeChecker{
	public static final int EXIT = -100;

	public static void main(String[] args){
		Scanner myScanner = new Scanner(System.in);
		int check = 2;

		System.out.println("Welcome to the prime checker!");
		System.out.print("n: ");
		int n = myScanner.nextInt();

		while (n != EXIT){
			while (check <= Math.sqrt(n)){
				if (n % check == 0){
					System.out.println(n + " is not a prime number.");
					break;
				}
				else {
					check ++;
				}
			}
			if (check > Math.sqrt(n)){
				System.out.println(n + " is a prime number.");	
			}

			// new run
			System.out.print("n: ");
			n = myScanner.nextInt();
			check = 2;
		}
		
		System.out.println("Have a good one!");
	}
}
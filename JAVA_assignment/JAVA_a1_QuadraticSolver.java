import java.util.Scanner;

public class QuadraticSolver{
	public static void main(String[] args){
		Scanner aScanner = new Scanner(System.in);
		Scanner bScanner = new Scanner(System.in);
		Scanner cScanner = new Scanner(System.in);

		System.out.println("stanCode Quadratic Solver!");
		System.out.print("a: ");
		int a = aScanner.nextInt();
		System.out.print("b: ");
		int b = bScanner.nextInt();
		System.out.print("c: ");
		int c = cScanner.nextInt();

		double def = Math.sqrt(Math.pow(b, 2)-4*a*c);
		if (def > 0){
			double a1 = (-b+def)/(2*a);
			double a2 = (-b-def)/(2*a);
			System.out.println("Two roots: " + a1 + " , " + a2);
		}
		else if (def == 0){
			double aa = -b/(2*a);
			System.out.println("One roots: " + aa);
		}
		else {
			System.out.println("No real roots");
		}
	}
}
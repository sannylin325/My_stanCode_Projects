import java.util.Scanner;

public class Caesar{
	public static void main(String[] args){
		Scanner numScanner = new Scanner(System.in);
		Scanner textScanner = new Scanner(System.in);
		String ans = "";

		System.out.print("Secret number: ");
		int num = numScanner.nextInt();
		System.out.print("What's the ciphered string? ");
		String ciphered = textScanner.nextLine().toUpperCase();

		for (int i=0; i<ciphered.length(); i++){
			char ch = ciphered.charAt(i);
			if (Character.isLetter(ch)){
				char new_ch = (char)(ch+num);
				if ((ch+num)>90){
					new_ch = (char)(new_ch+6);	
				}
				ans = ans + Character.toUpperCase(new_ch);
			}
			else {
				ans = ans + ch;
			}
		}

		System.out.println("The deciphered string is: " + ans);
	}
}
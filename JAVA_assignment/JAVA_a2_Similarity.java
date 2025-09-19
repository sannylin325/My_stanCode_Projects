import java.util.Scanner;

public class Similarity{
	public static void main(String[] args){
		int score = 0;
		int temp = 0;
		String temp_ans = "";
		String best_ans = "";
		Scanner longScanner = new Scanner(System.in);
		Scanner shortScanner = new Scanner(System.in);

		System.out.print("Please give me a DNA sequence to search: ");
		String long_dna = longScanner.nextLine().toUpperCase();
		System.out.print("What DNA sequence would you like to match? ");
		String short_dna = shortScanner.nextLine().toUpperCase();
		
		for (int i=0; i<long_dna.length()-short_dna.length()+1; i++){
			int short_index = 0;
			for (int j=i; j<short_dna.length()+i; j++){
				temp_ans = temp_ans + long_dna.charAt(j);
				if (long_dna.charAt(j)==short_dna.charAt(short_index)){
					temp ++;
				}
				short_index ++;
			}
			if (temp>score){
				score = temp;
				best_ans = temp_ans;				
			}
			temp = 0;
			temp_ans = "";
		}

		System.out.println("The best match is " + best_ans);
	}
}
import java.util.Random;
import java.util.Scanner;

public class Hangman{
	public static String getWord(){
		Random myRandom = new Random();	
		int num = myRandom.nextInt(9);

		if (num==0){
			return "NOTORIOUS";
		}
		else if (num==1){
			return "GLAMOROUS";
		}
		else if (num==2){
			return "CAUTIOUS";
		}
		else if (num==3){
			return "DEMOCRACY";
		}
		else if (num==4){
			return "BOYCOTT";
		}
		else if (num==5){
			return "ENTHUSIASTIC";
		}
		else if (num==6){
			return "HOSPITALITY";
		}
		else if (num==7){
			return "BUNDLE";
		}
		else {
			return "REFUND";
		}
	}

	public static String checkprogress(String progress, String guess){
		String newprogress = "";
		char ch = guess.charAt(0);
		for (int i=0; i<ANS.length(); i++){
			if (ch==ANS.charAt(i)){
				newprogress = newprogress + guess;
			}
			else if (progress==""){
				newprogress = newprogress + "-";
			}
			else {
				newprogress = newprogress + progress.charAt(i);
			}
		}
		return newprogress;
	}
	
	//
	public static final String ANS = getWord();
	public static final int LIVES = 7;

	public static void main(String[] args){
		String guess = " ";
		String progress = checkprogress("", guess);
		int lives = LIVES;
		Scanner myScanner = new Scanner(System.in);
		
		while (true){
			System.out.println("The word looks like: " + progress);
			System.out.println("You have " + lives + " wrong guess left.");
			// check input format
			while (true){
				System.out.print("Your guess: ");
				guess = myScanner.nextLine().toUpperCase();
				if (guess.length()==1){
					char ch = guess.charAt(0);
					if (Character.isLetter(ch)){
						break;
					}
					else {
						System.out.println("Illegal format.");
					}
				}
				else {
					System.out.println("Illegal format.");
				}
			}

			// check guess wrong or right
			if (ANS.indexOf(guess)==-1){
				System.out.println("There is no " + guess + "'s in the word.");
				lives --;
			}
			else {
				System.out.println("You are correct!");
				progress = checkprogress(progress, guess);
			}

			// check if win or lose
			if (ANS.equals(progress)){
				System.out.println("You win!!");
				System.out.println("The word was: " + ANS);
				break;
			}
			else if (lives==0){
				System.out.println("You are completely hung :(");
				System.out.println("The word was: " + ANS);
				break;
			}
		}
}	
}
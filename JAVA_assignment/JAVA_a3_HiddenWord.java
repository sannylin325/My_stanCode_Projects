import java.util.*;

public class HiddenWord{
	// iVar
	private String answer;

	// constructor
	public HiddenWord(String answer){
		this.answer = answer;
	}

	// methods
	public String getHint(String guess){
		if (guess.length() != answer.length()){
			return "The number of characters does not match.";
		}

		String output = "";
		for (int i=0; i<answer.length(); i++){
			char ch = guess.charAt(i);
			String sch = "" + ch;
			if (guess.charAt(i) == answer.charAt(i)){
				output = output + guess.charAt(i);
			}
			else if (answer.contains(sch)){
				output = output + '+';
			}
			else {
				output = output + '*';
			}
		}
		return output;
	}

	public static void main(String[] args){
		HiddenWord puzzle = new HiddenWord("HARPS");
		Scanner myScanner = new Scanner(System.in);

		while (true){
			System.out.print("Your guess: ");
			String result = puzzle.getHint(myScanner.nextLine().toUpperCase());
			System.out.println(result);
			if (result.equals(puzzle.answer)){
				break;
			}
		}
	}
}
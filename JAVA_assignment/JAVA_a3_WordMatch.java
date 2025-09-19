public class WordMatch{
	// iVar
	private String secret;

	// constructor
	public WordMatch(String word){
		secret = word.toLowerCase();
	}

	// methods
	public int scoreGuess(String guess){
		int count = 0;
		for (int i=0; i<secret.length()-guess.length()+1; i++){
			String subSecret = secret.substring(i, i+guess.length());
			if (subSecret.equals(guess)){
				count ++;
			}
		}
		return count * guess.length() * guess.length();
	}

	public String findBetterGuess(String guess1, String guess2){
		int score1 = scoreGuess(guess1);
		int score2 = scoreGuess(guess2);
		if (score1 > score2){
			return guess1;
		}
		else if (score2 > score1){
			return guess2;
		}
		else {
			for (int i=0; i<guess1.length(); i++){
				if (guess1.charAt(i)>guess2.charAt(i)){
					return guess1;
				}
				else if (guess2.charAt(i)>guess1.charAt(i)) {
					return guess2;
				}
			}
			return guess1;
		}
	}

	public static void main(String[] args){
		// WordMatch game1 = new WordMatch("mississippi");
		// System.out.println(game1.scoreGuess("i"));
		// System.out.println(game1.scoreGuess("iss"));
		// System.out.println(game1.scoreGuess("issipp"));
		// System.out.println(game1.scoreGuess("mississippi"));

		// WordMatch game2 = new WordMatch("aaaabb");
		// System.out.println(game2.scoreGuess("a"));
		// System.out.println(game2.scoreGuess("aa"));
		// System.out.println(game2.scoreGuess("aaa"));
		// System.out.println(game2.scoreGuess("aabb"));
		// System.out.println(game2.scoreGuess("c"));

		WordMatch game = new WordMatch("concatenation");
		System.out.println(game.scoreGuess("ten"));
		System.out.println(game.scoreGuess("nation"));
		System.out.println(game.findBetterGuess("ten", "nation"));
		System.out.println(game.scoreGuess("con"));
		System.out.println(game.scoreGuess("cat"));
		System.out.println(game.findBetterGuess("cat", "con"));
	}
}
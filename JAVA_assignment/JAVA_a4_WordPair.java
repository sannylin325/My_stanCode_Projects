public class WordPair{
	// iVar?
	private String firstWord;
	private String secondWord;

	// constructor
	public WordPair(String first, String second){
		firstWord = first;
		secondWord = second;
	}

	// methods
	public String toString(){
		return "(" + firstWord + "," + secondWord + ")";
	}

	public String getFirst(){
		return firstWord;
	}

	public String getSecond(){
		return secondWord;
	}
}
import java.util.*;

public class WordPairList{
	// iVar
	private ArrayList<WordPair> allPairs;

	// constructor
	public WordPairList(String[] words){
		allPairs = new ArrayList<>();

		for (int i=0; i<words.length; i++){
			for (int j=i+1; j<words.length; j++){
				allPairs.add(new WordPair(words[i], words[j]));
			}
		}
	}

	// methods
	public int numMatches(){
		int count = 0;
		for (int i=0; i<allPairs.size(); i++){
			if (allPairs.get(i).getFirst().equals(allPairs.get(i).getSecond())){
				count ++;
			}
		}
		return count;
	}

	// main
	public static void main(String[] args){
		String[] wordNums = {"one", "two", "three"};
		WordPairList exampleOne = new WordPairList(wordNums);
		for (int i=0; i<exampleOne.allPairs.size(); i++){
			System.out.println(exampleOne.allPairs.get(i).getFirst());
			System.out.println(exampleOne.allPairs.get(i).getSecond());
		}

		String[] moreWords = {"the", "red", "fox", "the", "red"};
		WordPairList exampleThree = new WordPairList(moreWords);
		System.out.println(exampleThree.numMatches());
	}
}
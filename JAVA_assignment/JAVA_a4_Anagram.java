import java.util.*;

public class Anagram{
	// methods
	public static boolean checkAnagram(String s, String t){
		if (s.length()!=t.length()){
			return false;
		}

		HashMap<Character, Integer> maps = new HashMap<>();
		HashMap<Character, Integer> mapt = new HashMap<>();

		for (int i=0; i<s.length(); i++){
			char ch = s.charAt(i);
			if (maps.containsKey(ch)){
				int count = maps.get(ch);
				maps.put(ch, count);
			}
			else {
				maps.put(ch, 1);
			}
		}

		for (int i=0; i<t.length(); i++){
			char ch = t.charAt(i);
			if (mapt.containsKey(ch)){
				int count = mapt.get(ch);
				mapt.put(ch, count);
			}
			else {
				mapt.put(ch, 1);
			}
		}

		if (maps.equals(mapt)){
			return true;
		}
		return false;
	}

	// main
	public static void main(String[] args){
		System.out.println(checkAnagram("anagram", "nagaram"));
		System.out.println(checkAnagram("rat", "car"));
		System.out.println(checkAnagram("mouse", "cat"));
	}
}
/**
 * Files: Anagram.cpp
 * Author: Sanny Lin
 * 
 * This Anagram class will compare two given strings
 * and return weather these two strings are anagrams or not.
 */

#include<iostream>
#include<unordered_map>
using namespace std;

class Anagram{
public:
	static bool checkAnagram(string s1, string s2);
};

/**
 * Check if two strings are anagrams or not.
 * Anagrams have the same length and the same characters with the same frequency.
 * 
 * @param s1: the first string to be compared
 * @param s2: the second string to be compared
 * @return: true if the strings are anagrams, false otherwise.
 */
bool Anagram::checkAnagram(string s1, string s2){
	if (s1.length() != s2.length()) return false;

	unordered_map<char, int> m1;
	unordered_map<char, int> m2;

	for (int i=0; i<s1.length(); i++){
		m1[s1[i]] ++;
		m2[s2[i]] ++;
	}
	return m1==m2;
}

// main
int main(){
	cout << boolalpha << Anagram::checkAnagram("tesla", "steal") << endl;
	cout << Anagram::checkAnagram("rat", "car") << endl;
	return 0;
}
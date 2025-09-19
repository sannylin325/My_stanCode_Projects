/**
 * Files: TextBook.cpp
 * Author: Sanny Lin
 *
 * The Book class represents a book with a title and a price.
 * It provides methods to retrieve the title, price, 
 * and get a formatted string containing the book's information.
 * 
 * The Textbook class is a subclass of the Book class, representing a textbook with an edition.
 * It inherits the properties and methods from the Book class 
 * and provides additional functionality specific to textbooks.
 */

#include <iostream>
using namespace std;

class Book {
private:
	string title;  // title of the book
	double price;  //price of the book

public:
	// constructor
	/**
	 * Create a new Book with the given title and price.
	 * @param bookTitle: title of the book
	 * @param bookPrice: price of the book
	 */
	Book(string bookTitle, double bookPrice){
		title = bookTitle;
		price = bookPrice;
	}

	// methods
	/** @return: title of the book*/
	string getTitle(){
		return title;
	}

	/** @return: title and price of the book*/
	string getBookInfo(){
		return title + "-" + to_string(price);
	}
};


class TextBook: public Book {
private:
	int edition;  // edition of the book

public:
	// constructor
	/**
	 * Create a new Textbook with the given title, price and editon.
	 * @param bookTitle: title of the book
	 * @param bookPrice: price of the book
	 * @param bookEdition: edition of the book
	 */
	TextBook(string bookTitle, double bookPrice, int bookEdition): Book(bookTitle, bookPrice){
		edition = bookEdition;
	}

	// methods
	/** @return: the edition of the book*/
	int getEdition(){
		return edition;
	}

	/** @return: title, price and edition of the book*/
	string getBookInfo(){
		return Book:: getBookInfo() + "-" + to_string(edition);
	}

	/**
     * Check if a textbook is a valid substitute for another.
     * @param otherBook: the other textbook to compare
     * @return: true if the textbook can substitute for the other, false otherwise
     */
	bool canSubsituteFor(TextBook bookTitle){
		if ((bookTitle.getTitle() == getTitle()) & (bookTitle.getEdition() < getEdition())){
			return true;
		}
		return false;
	}
};

// main
int main(){
	TextBook bio2015("Biology", 49.75, 2);
	TextBook bio2019("Biology", 39.75, 3);
	cout << bio2019.getEdition() << endl;
	cout << bio2019.getBookInfo() << endl;
	cout << boolalpha << bio2019.canSubsituteFor(bio2015) << endl;
	cout << bio2015.canSubsituteFor(bio2019) << endl;
	TextBook math("Calculus", 45.25, 1);
	cout << bio2015.canSubsituteFor(math) << endl;
	return 0;
}
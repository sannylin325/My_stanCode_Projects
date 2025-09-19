/**
 * Files: ReviewAnalysis.cpp
 * Author: Sanny Lin
 * 
 * The Review class represents a user review containing a rating and a comment.
 * It provides methods to access and retrieve the rating and comment of the review.
 * The class ensures that the rating is a non-negative integer (r >= 0) 
 * and the comment is not null.
 * 
 * The ReviewAnalysis class represents an analysis of user reviews.
 * It allows users to input ratings and comments, 
 * which are then stored in the allReviews array.
 * The class provides methods to calculate the average rating of 
 * all reviews and to collect selected comments.
 *
 * The allReviews array stores Review objects, 
 * which consist of a rating and a comment provided by the user.
 * The class ensures that all ratings are non-negative integers (rating >= 0), 
 * and all comments are not null.
 */

#include <iostream>
#include <list>  // arrayList
using namespace std;

class Review{
private:
	int rating;
	string comment;

public:
	// constructor
	/**
     * Constructs a Review object with the specified rating and comment.
     * @param r: the rating of the review (must be non-negative)
     * @param s: the comment of the review (must not be null)
     * 
     * Precondition: r >= 0
     *               c is not null
     */
	Review(int r, string s){
		rating = r;
		comment = s;
	}

	// methods
	/** @return: the rating of the review*/
	int getRating(){
		return rating;
	}

	/** @return: the comment of the review*/
	string getComment(){
		return comment;
	}
};


class ReviewAnalysis{
private:
	// Review array -> Review* (pointer)
	Review* allReviews[5];    // all user reviews

public:
	// constructor
	/** Initializes allRevies to contain all the Review object to be analyzed.*/
	ReviewAnalysis(){
		allReviews[0] = new Review(4, "Good! Thx");
		allReviews[1] = new Review(3, "OK site");
		allReviews[2] = new Review(5, "Great!");
		allReviews[3] = new Review(2, "Poor! Bad.");
		allReviews[4] = new Review(3, "");
	}

	// methods
	/** 
	 * @return: the average rating of allReviews
	 * Precondition: allReviews contains at least one Review
	 */
	double getAverageRating(){
		double total = 0;
		for (Review* r: allReviews){
			total += (*r).getRating();  // * get element
			// same as total += r->getRating()
		}
		return total / (sizeof(allReviews)/sizeof(allReviews[0]));  // 2 items in each *Reviews
	}

	/** 
	 * @return: comments containing formatted versions of allReviews
	 * Precondition: allReviews contains at least one Review
	 * Postcondition: allReviews is unchanged
	 */
	list<string> collectComments(){
		list<string> reviews;
		for (int i=0; i<(sizeof(allReviews)/sizeof(allReviews[0])); i++){
			string comment = (*allReviews[i]).getComment();
			if (comment.find('!')!=string::npos){
				if (comment.find('!')!=comment.length()-1 and comment[comment.length()-1]!='.'){
					comment += ".";
				}
				comment = to_string(i) + "-" + comment;
				cout << comment << endl;
				reviews.push_back(comment);
			}
		}
	}
};

// main
int main(){
	ReviewAnalysis obj;
	cout << obj.getAverageRating() << endl;
	obj.collectComments();
	return 0;
}
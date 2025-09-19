import java.util.*;

public class ReviewAnalysis{
	// iVar
	private Review[] allReviews = new Review[5];

	// constructor
	public ReviewAnalysis(){
		Review r1 = new Review(4, "Good! Thx");
		Review r2 = new Review(3, "OK site");
		Review r3 = new Review(5, "Great!");
		Review r4 = new Review(2, "Poor! Bad.");
		Review r5 = new Review(3, "");
		allReviews[0] = r1;
		allReviews[1] = r2;
		allReviews[2] = r3;
		allReviews[3] = r4;
		allReviews[4] = r5;
	}

	// methods
	public double getAverageRating(){
		double total = 0;
		int count = allReviews.length;
		for (Review r: allReviews){
			total += r.getRating();
		}
		return total/count;
	}

	public ArrayList<String> collectComments(){
		ArrayList<String> surprise = new ArrayList<>();
		for (int i=0; i<allReviews.length; i++){
			String contents = allReviews[i].getComment();
			if (contents.contains("!")){
				contents = i + "-" + contents;
				if (!contents.endsWith("!") && !contents.endsWith(".")){
					contents = contents + ".";
				}
				surprise.add(contents);
			}
		}
		return surprise;
	}

	// main
	public static void main(String[] args){
		ReviewAnalysis reviewing = new ReviewAnalysis();
		// System.out.println(reviewing.getAverageRating());
		ArrayList<String> reviewArray = reviewing.collectComments();
		System.out.println(reviewArray);
		// for (int i=0; i<reviewArray.size(); i++){
		// 	System.out.println(reviewArray.get(i));
		// }
	}	
}
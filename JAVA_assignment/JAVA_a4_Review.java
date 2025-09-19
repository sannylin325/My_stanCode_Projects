public class Review{
	// iVar
	private int rating;
	private String comment;

	// constructor
	public Review(int r, String c){
		rating = r;
		comment = c;
	}

	// methods
	public int getRating(){
		return rating;
	}

	public String getComment(){
		return comment;
	}
}
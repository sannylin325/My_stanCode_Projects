public class Textbook extends Book{
	// iVar
	private int edition;

	// constructor
	public Textbook(String bookTitle, double bookPrice){
		super(bookTitle, bookPrice);
	}
	
	public Textbook(String bookTitle, double bookPrice, int bookEdition){
		super(bookTitle, bookPrice);
		edition = bookEdition;
	}

	// methods
	public String getBookInfo(){
		return title + '-' + price + '-' + edition;
	}

	public int getEdition(){
		return edition;
	}

	public boolean canSubstituteFor(Textbook quoteBook){
		if ((title == quoteBook.title) & (edition >= quoteBook.edition)){
			return true;
		}
		else {
			return false;
		}
	}
}
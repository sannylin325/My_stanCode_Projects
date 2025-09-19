public class Book{
	// iVar
	public String title;
	public double price;

	// constructor
	public Book(String bookTitle, double bookPrice){
		title = bookTitle;
		price = bookPrice;
	}

	// methods
	public String getTitle(){
		return title;
	}

	public String getBookInfo(){
		return title + '-' + price;
	}
}